import logging

from topic_engine.merge import merge_records
from topic_engine.enrich import enrich_topics
from topic_engine.score import score_topics
from topic_engine.dedup import dedup_topics
from topic_engine.emit import build_queue_dict, write_queue_json, render_calendar_section
from topic_engine.calendar_io import upsert_calendar
from topic_engine.notify import render_digest, send_digest

log = logging.getLogger("topic_engine.engine")


def safe_fetch(name, fn):
    try:
        recs = fn() or []
        return name, recs, True
    except Exception as e:  # noqa: BLE001
        log.warning("adapter %s failed: %s", name, e)
        return name, [], False


def run(deps: dict, week: str, dry_run: bool) -> dict:
    sources_used, sources_skipped, all_records = [], [], []
    for name, fn in deps["adapters"].items():
        nm, recs, ok = safe_fetch(name, fn)
        if ok and recs:
            sources_used.append(nm)
            all_records.extend(recs)
        else:
            sources_skipped.append(nm)

    topics = merge_records(all_records)
    total_candidates = len(topics)
    topics = enrich_topics(topics, deps["media_index"])
    topics = score_topics(topics)
    topics = dedup_topics(topics, deps["published"], deps["seen_slugs"])
    # re-rank after dedup so ranks are contiguous
    for i, t in enumerate(topics, start=1):
        t.rank = i

    queue = build_queue_dict(week, deps["generated_at"], sorted(sources_used),
                             sorted(sources_skipped), total_candidates, topics)

    if dry_run:
        return queue

    write_queue_json(deps["out_dir"], week, queue)

    if deps.get("calendar_path"):
        section = render_calendar_section(week, topics)
        with open(deps["calendar_path"], encoding="utf-8") as fh:
            cal = fh.read()
        cal = upsert_calendar(cal, week, section)
        with open(deps["calendar_path"], "w", encoding="utf-8") as fh:
            fh.write(cal)

    if deps.get("git_push"):
        deps["git_push"]()

    tg = deps.get("telegram")
    if tg:
        send_digest(render_digest(queue), tg["bot_token"], tg["chat_id"], tg["http_post"])

    return queue
