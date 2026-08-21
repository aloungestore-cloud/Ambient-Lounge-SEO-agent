from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

def _load_env(env_file: str = "/home/bitrix/cron/al_seo_aio.env") -> None:
    p = Path(env_file)
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k:
            os.environ.setdefault(k, v)  # don't overwrite already-set env

_load_env()

import anthropic
from publisher.fetch import fetch_article
from publisher.generate import generate_post
from publisher.pack import pack_post
from publisher.post import post_to_n8n

API_URL     = os.getenv("BITRIX_API_URL", "https://ambientlounge.ru/api/catalog.php")
API_KEY     = os.getenv("SEO_AIO_API_KEY", "")
WEBHOOK_URL = os.getenv("N8N_TG_WEBHOOK_URL", "")
BLOG_BASE   = os.getenv("BITRIX_BLOG_BASE", "https://ambientlounge.ru/blog")
QUEUE_FILE  = Path(__file__).parent / "data" / "queue.json"


def run_for_url(article_url: str, dry_run: bool) -> int:
    if not API_KEY:
        print("ERROR: SEO_AIO_API_KEY not set", file=sys.stderr)
        return 1
    article = fetch_article(article_url, API_URL, API_KEY)
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    raw = generate_post(article, client)
    pack = pack_post(raw, article)
    if dry_run:
        print(json.dumps(pack, ensure_ascii=False, indent=2))
        return 0
    if not WEBHOOK_URL:
        print("ERROR: N8N_TG_WEBHOOK_URL not set", file=sys.stderr)
        return 1
    post_to_n8n(pack, WEBHOOK_URL)
    print(f"Sent: {pack['pack_id']}")
    return 0


def run_from_queue(dry_run: bool) -> int:
    if not QUEUE_FILE.exists():
        print("Queue empty (queue.json not found)")
        return 0
    with open(QUEUE_FILE, encoding="utf-8") as f:
        queue = json.load(f)
    items = queue if isinstance(queue, list) else queue.get("topics", [])
    pending = [t for t in items if t.get("status", "pending") == "pending"]
    if not pending:
        print("Queue empty")
        return 0
    first = pending[0]
    slug = first.get("slug", "")
    if not slug:
        print(f"ERROR: first queue item has no slug: {first}", file=sys.stderr)
        return 1
    article_url = f"{BLOG_BASE.rstrip('/')}/{slug}/"
    return run_for_url(article_url, dry_run)


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish article to Telegram channel via n8n")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--article-url", metavar="URL")
    group.add_argument("--from-queue", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--week", metavar="YYYY-WW", help="Override ISO week (unused in MVP, reserved)")
    args = parser.parse_args()

    if args.article_url:
        sys.exit(run_for_url(args.article_url, args.dry_run))
    else:
        sys.exit(run_from_queue(args.dry_run))


if __name__ == "__main__":
    main()
