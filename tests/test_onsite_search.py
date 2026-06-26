import json
import os
from topic_engine.adapters.onsite_search import onsite_search_records

FIX = os.path.join(os.path.dirname(__file__), "fixtures")


def _fake_get(payload):
    def _get(url, params=None, headers=None):
        return payload
    return _get


def test_maps_queries_to_records():
    with open(os.path.join(FIX, "mia_queries.json"), encoding="utf-8") as f:
        payload = json.load(f)
    recs = onsite_search_records("http://x", "KEY", _fake_get(payload))
    assert len(recs) == 2
    r = recs[0]
    assert r.source == "onsite_search"
    assert r.metric_kind == "searches"
    assert r.phrase == "кресло на балкон"
    assert r.raw_metric == 12.0
    assert r.intent == "info"
    assert r.zero_result is False
    assert r.avg_results == 55.0


def test_zero_result_flagged():
    with open(os.path.join(FIX, "mia_queries.json"), encoding="utf-8") as f:
        payload = json.load(f)
    recs = onsite_search_records("http://x", "KEY", _fake_get(payload))
    z = [r for r in recs if r.phrase == "pet lounge medium 90см"][0]
    assert z.zero_result is True


def test_api_failure_returns_empty():
    def _boom(url, params=None, headers=None):
        raise RuntimeError("network down")
    assert onsite_search_records("http://x", "KEY", _boom) == []
