from topic_engine.models import Record, Topic
from topic_engine import config


def test_record_defaults():
    r = Record(phrase="купить диван", source="wordstat", raw_metric=1200.0, metric_kind="impressions")
    assert r.intent is None
    assert r.zero_result is False


def test_topic_defaults():
    t = Topic(phrase="купить диван", display_phrase="Купить диван")
    assert t.section_id == 175
    assert t.sources == []
    assert t.raw_by_source == {}


def test_config_weights_present():
    assert config.SOURCE_WEIGHTS["mia_chat"] == 1.0
    assert config.INTENT_WEIGHTS["buy"] == 1.5
    assert set(config.SOURCE_WEIGHTS) == {"mia_chat", "onsite_search", "gsc", "metrika", "wordstat"}
