from topic_engine.models import Topic
from topic_engine import config


def _source_maxima(topics: list[Topic]) -> dict[str, float]:
    maxima: dict[str, float] = {}
    for t in topics:
        for src, val in t.raw_by_source.items():
            if val > maxima.get(src, 0.0):
                maxima[src] = val
    return maxima


def _catalog_factor(topic: Topic) -> float:
    if topic.zero_result:
        return config.CATALOG_ZERO
    avg = getattr(topic, "_avg_results", None)
    if avg is not None and avg > 0:
        return config.CATALOG_HAS
    return config.CATALOG_UNKNOWN


def score_topics(topics: list[Topic]) -> list[Topic]:
    maxima = _source_maxima(topics)
    for t in topics:
        demand = 0.0
        for src, val in t.raw_by_source.items():
            m = maxima.get(src, 0.0)
            if m > 0:
                demand += config.SOURCE_WEIGHTS.get(src, 0.5) * (val / m)
        intent_w = config.INTENT_WEIGHTS.get(t.intent, config.INTENT_WEIGHTS["unknown"])
        media = config.MEDIA_BONUS if t.media_available else 1.0
        catalog = _catalog_factor(t)
        corrob = 1.0 + config.CORROB_STEP * (len(t.sources) - 1)
        t.score = round(demand * intent_w * media * catalog * corrob, 4)
    topics.sort(key=lambda x: x.score, reverse=True)
    for i, t in enumerate(topics, start=1):
        t.rank = i
    return topics
