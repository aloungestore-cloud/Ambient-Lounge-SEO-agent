import glob
import json
import logging
import os

log = logging.getLogger("topic_engine.history")


def load_seen_slugs(topics_dir: str) -> set[str]:
    seen: set[str] = set()
    if not os.path.isdir(topics_dir):
        return seen
    for path in glob.glob(os.path.join(topics_dir, "*.json")):
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
            topics = data.get("topics")
            if not isinstance(topics, list):
                continue
            for t in topics:
                if not isinstance(t, dict):
                    continue
                slug = (t.get("slug") or "").strip().lower()
                if slug:
                    seen.add(slug)
        except (OSError, ValueError) as e:
            log.warning("history: skip %s (%s)", path, e)
    return seen
