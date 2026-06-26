from topic_engine.models import Topic
from topic_engine.score import score_topics


def _t(phrase, raw_by_source, intent="info", **kw):
    return Topic(phrase=phrase, display_phrase=phrase, intent=intent,
                 sources=sorted(raw_by_source), raw_by_source=dict(raw_by_source), **kw)


def test_buy_outranks_info_same_demand():
    topics = score_topics([
        _t("a", {"wordstat": 100}, intent="info"),
        _t("b", {"wordstat": 100}, intent="buy"),
    ])
    assert topics[0].phrase == "b"  # buy weight 1.5 > info 1.0


def test_corroboration_bonus():
    # same demand contribution but more sources → higher score
    one = _t("one", {"wordstat": 100}, intent="info")
    two = _t("two", {"wordstat": 100, "metrika": 100}, intent="info")
    topics = score_topics([one, two])
    assert topics[0].phrase == "two"


def test_zero_result_penalty():
    base = _t("x", {"onsite_search": 10}, intent="buy")
    zero = _t("y", {"onsite_search": 10}, intent="buy", zero_result=True)
    topics = score_topics([base, zero])
    assert topics[0].phrase == "x"


def test_rank_is_set():
    topics = score_topics([
        _t("low", {"wordstat": 1}),
        _t("high", {"wordstat": 1000}),
    ])
    assert topics[0].rank == 1
    assert topics[1].rank == 2
