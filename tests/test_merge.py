from topic_engine.models import Record
from topic_engine.merge import merge_records


def test_groups_by_normalized_phrase():
    recs = [
        Record("Купить диван", "wordstat", 1000, "impressions"),
        Record("купить диван", "onsite_search", 5, "searches", intent="buy"),
        Record("лежак для собаки", "metrika", 9, "visits", theme="pets"),
    ]
    topics = merge_records(recs)
    by = {t.phrase: t for t in topics}
    assert set(by) == {"купить диван", "лежак для собаки"}
    divan = by["купить диван"]
    assert divan.sources == ["onsite_search", "wordstat"]
    assert divan.raw_by_source == {"wordstat": 1000.0, "onsite_search": 5.0}
    assert divan.intent == "buy"
    assert divan.display_phrase == "Купить диван"


def test_sums_same_source_metric():
    recs = [
        Record("диван", "wordstat", 100, "impressions"),
        Record("диван", "wordstat", 50, "impressions"),
    ]
    t = merge_records(recs)[0]
    assert t.raw_by_source == {"wordstat": 150.0}


def test_zero_result_or():
    recs = [
        Record("pet lounge xxl", "onsite_search", 1, "searches", zero_result=True),
        Record("pet lounge xxl", "wordstat", 80, "impressions"),
    ]
    assert merge_records(recs)[0].zero_result is True
