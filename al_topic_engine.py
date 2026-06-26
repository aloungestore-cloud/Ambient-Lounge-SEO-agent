"""SP-A topic engine CLI.

Usage:
    python3 al_topic_engine.py [--dry-run] [--week YYYY-WW]

Env (server .env): SEO_AIO_API_KEY, GOOGLE_SHEETS_ID, GOOGLE_SERVICE_ACCOUNT_JSON,
GOOGLE_SHEETS_GID, TG_BOT_TOKEN, TG_OWNER_CHAT_ID.
"""
import argparse
import datetime
import os
import subprocess

import requests

from topic_engine import config
from topic_engine.adapters.tsv import wordstat_records, gsc_records, metrika_records
from topic_engine.adapters.onsite_search import onsite_search_records
from topic_engine.adapters.mia_chat import fetch_sheet_rows, mia_chat_records
from topic_engine.media_index import load_media_index
from topic_engine.dedup import published_slugs
from topic_engine.history import load_seen_slugs
from topic_engine.engine import run

REPO = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(REPO, "outputs", "topics")
CALENDAR = os.path.join(REPO, "docs", "content_calendar.md")


def _http_get(url, params=None, headers=None):
    r = requests.get(url, params=params, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()


def _current_week() -> str:
    d = datetime.date.today() - datetime.timedelta(days=3)
    while d.isoweekday() != 7:
        d -= datetime.timedelta(days=1)
    iso = d.isocalendar()
    return f"{iso[0]}-{iso[1]:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--week", default=None)
    args = ap.parse_args()
    week = args.week or _current_week()

    api_key = os.getenv("SEO_AIO_API_KEY", "")
    sheets_key = os.getenv("GOOGLE_SHEETS_ID", "")
    gid = int(os.getenv("GOOGLE_SHEETS_GID", "421239372"))
    sa_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")

    def _mia_chat():
        rows = fetch_sheet_rows(sheets_key, gid, sa_json)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return mia_chat_records(rows, days=7, now_iso=now)

    adapters = {
        "mia_chat": _mia_chat,
        "onsite_search": lambda: onsite_search_records(config.MIA_QUERIES_URL, api_key, _http_get),
        "wordstat": lambda: wordstat_records(week, config.WORDSTAT_DIR),
        "gsc": lambda: gsc_records(week, config.GSC_DIR),
        "metrika": lambda: metrika_records(week, config.METRIKA_DIR),
    }

    try:
        sitemap = requests.get(config.SITEMAP_URL, timeout=30).text
    except Exception:  # noqa: BLE001
        sitemap = ""

    def _git_push():
        subprocess.run(["git", "add", "outputs/topics", "docs/content_calendar.md"], cwd=REPO, check=False)
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO).returncode != 0:
            subprocess.run(["git", "commit", "-m", f"chore(topics): weekly queue {week}"], cwd=REPO, check=False)
            subprocess.run(["git", "push", "origin", "main"], cwd=REPO, check=False)

    tg_token = os.getenv("TG_BOT_TOKEN")
    tg_chat = os.getenv("TG_OWNER_CHAT_ID")

    deps = {
        "adapters": adapters,
        "media_index": load_media_index(
            os.path.join(REPO, "data", "breed_photos.json"),
            os.path.join(REPO, "data", "product_heroes.json"),
        ),
        "published": published_slugs(sitemap),
        "seen_slugs": load_seen_slugs(OUT_DIR),
        "generated_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "out_dir": OUT_DIR,
        "calendar_path": CALENDAR if not args.dry_run else None,
        "git_push": _git_push if not args.dry_run else None,
        "telegram": ({"bot_token": tg_token, "chat_id": tg_chat,
                      "http_post": lambda url, json=None, timeout=None: requests.post(url, json=json, timeout=timeout)}
                     if (tg_token and tg_chat and not args.dry_run) else None),
    }

    queue = run(deps, week=week, dry_run=args.dry_run)
    print(f"week={week} used={queue['sources_used']} skipped={queue['sources_skipped']} "
          f"candidates={queue['total_candidates']} after_dedup={queue['after_dedup']}")


if __name__ == "__main__":
    main()
