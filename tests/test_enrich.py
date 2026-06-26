from topic_engine.models import Topic
from topic_engine.enrich import enrich_topics


def _t(phrase, intent="unknown", theme=None):
    return Topic(phrase=phrase, display_phrase=phrase, intent=intent, theme=theme)


def test_pet_routes_to_174():
    t = enrich_topics([_t("лежак для овчарки")], media_index=set())[0]
    assert t.intent == "pet"
    assert t.section_id == 174
    assert t.section_url == "/blog/obzory-lezhakov-dlya-zhivotnyh/"


def test_buy_model_routes_to_586():
    # commercial furniture/interior topic → 586
    t = enrich_topics([_t("угловой диван в гостиную")], media_index=set())[0]
    assert t.section_id == 586


def test_howto_routes_to_175():
    t = enrich_topics([_t("как выбрать наполнitель", intent="info")], media_index=set())[0]
    assert t.section_id == 175


def test_media_available_when_token_matches():
    t = enrich_topics([_t("лежак для лабрадора")], media_index={"лабрадор"})[0]
    assert t.media_available is True


def test_slug_and_h1_filled():
    t = enrich_topics([_t("Бескаркасный диван для дачи")], media_index=set())[0]
    assert t.slug == "beskarkasnyy-divan-dlya-dachi"
    assert t.h1.startswith("Бескаркасный диван для дачи")
