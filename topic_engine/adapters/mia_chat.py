"""Mia chat adapter — ported from tools/seo_idea_harvester.py (fetch_new_questions).

Pure function over already-fetched sheet rows; fetch_sheet_rows() is the only
I/O part and is covered by integration, not unit, tests.
"""
import logging
from datetime import datetime, timedelta

from topic_engine.models import Record

log = logging.getLogger("topic_engine.mia_chat")

SKIP_INTENTS = {"irrelevant_spam", "skipped_bot_source", "attachment",
                "attachment_escalated", "spam_closed", "channel_linked"}
MIN_MSG_LEN = 10


def mia_chat_records(rows: list[list[str]], days: int, now_iso: str) -> list[Record]:
    if not rows or len(rows) < 2:
        return []
    now = datetime.strptime(now_iso[:19], "%Y-%m-%d %H:%M:%S")
    cutoff = now - timedelta(days=days)

    counts: dict[str, int] = {}
    display: dict[str, str] = {}
    for row in rows[1:]:
        if len(row) < 4:
            continue
        ts_str, _, msg, intent = row[0], row[1], row[2], row[3]
        if not ts_str or not msg:
            continue
        if intent in SKIP_INTENTS:
            continue
        msg = msg.strip()
        if len(msg) < MIN_MSG_LEN or msg.startswith("["):
            continue
        try:
            ts = datetime.strptime(ts_str[:19], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
        if ts < cutoff:
            continue
        key = msg.lower().strip()
        counts[key] = counts.get(key, 0) + 1
        display.setdefault(key, msg)

    return [Record(phrase=display[k], source="mia_chat", raw_metric=float(c),
                   metric_kind="mentions") for k, c in counts.items()]


def fetch_sheet_rows(sheets_key: str, gid: int, sa_json_path: str) -> list[list[str]]:
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        creds = Credentials.from_service_account_file(
            sa_json_path,
            scopes=["https://spreadsheets.google.com/feeds",
                    "https://www.googleapis.com/auth/drive"],
        )
        gc = gspread.authorize(creds)
        ws = gc.open_by_key(sheets_key).get_worksheet_by_id(gid)
        return ws.get_all_values()
    except Exception as e:  # noqa: BLE001
        log.warning("mia_chat fetch_sheet_rows failed: %s", e)
        return []
