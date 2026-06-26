from topic_engine.models import Record, Topic
from topic_engine.normalize import normalize_phrase


def merge_records(records: list[Record]) -> list[Topic]:
    buckets: dict[str, Topic] = {}
    avg_results: dict[str, float] = {}
    for r in records:
        key = normalize_phrase(r.phrase)
        if not key:
            continue
        t = buckets.get(key)
        if t is None:
            t = Topic(phrase=key, display_phrase=r.phrase)
            buckets[key] = t
        # shortest original wins as display
        if len(r.phrase) < len(t.display_phrase):
            t.display_phrase = r.phrase
        t.raw_by_source[r.source] = t.raw_by_source.get(r.source, 0.0) + r.raw_metric
        if r.source not in t.sources:
            t.sources.append(r.source)
        if r.intent and t.intent == "unknown":
            t.intent = r.intent
        if r.theme and not t.theme:
            t.theme = r.theme
        if r.zero_result:
            t.zero_result = True
        if r.avg_results is not None and key not in avg_results:
            avg_results[key] = r.avg_results
    for t in buckets.values():
        t.sources.sort()
    # stash avg_results on topic via attribute for downstream score (catalog factor)
    for key, t in buckets.items():
        t._avg_results = avg_results.get(key)  # type: ignore[attr-defined]
    return list(buckets.values())
