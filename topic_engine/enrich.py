from topic_engine.models import Topic
from topic_engine.intent import classify_intent
from topic_engine.translit import slugify
from topic_engine import config

_INTERIOR_HINTS = ("диван", "кресло", "пуф", "мебел", "интерьер", "гостин",
                   "террас", "лоджи", "балкон", "дача", "модул", "садов")


def _route(topic: Topic) -> tuple[int, str]:
    if topic.intent == "pet":
        return config.SECTIONS["pet"]
    if topic.intent == "info":
        return config.SECTIONS["howto"]
    # buy/compare/b2b/unknown: interior if it names furniture/space, else howto
    if any(h in topic.phrase for h in _INTERIOR_HINTS):
        return config.SECTIONS["interior"]
    return config.SECTIONS["howto"]


def enrich_topics(topics: list[Topic], media_index: set[str]) -> list[Topic]:
    for t in topics:
        if t.intent == "unknown":
            t.intent = classify_intent(t.phrase)
        tokens = set(t.phrase.split())
        t.media_available = bool(tokens & media_index) or any(
            any(m in tok for m in media_index) for tok in tokens
        )
        sid, surl = _route(t)
        t.section_id, t.section_url = sid, surl
        t.slug = slugify(t.display_phrase)
        t.h1 = t.display_phrase[:1].upper() + t.display_phrase[1:]
    return topics
