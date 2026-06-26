import os
from topic_engine.adapters.tsv import wordstat_records, gsc_records, metrika_records

FIX = os.path.join(os.path.dirname(__file__), "fixtures")


def test_wordstat():
    recs = wordstat_records("2026-26", FIX)
    assert len(recs) == 2
    r = recs[0]
    assert r.source == "wordstat"
    assert r.metric_kind == "impressions"
    assert r.phrase == "бескаркасный диван"
    assert r.raw_metric == 29400.0
    assert r.theme == "furniture"


def test_gsc():
    recs = gsc_records("2026-26", FIX)
    assert len(recs) == 2
    assert recs[0].source == "gsc"
    assert recs[0].metric_kind == "impressions"
    assert recs[0].raw_metric == 540.0  # impressions column, not clicks


def test_metrika():
    recs = metrika_records("2026-26", FIX)
    assert recs[0].source == "metrika"
    assert recs[0].metric_kind == "visits"
    assert recs[0].raw_metric == 31.0


def test_missing_file_returns_empty():
    assert wordstat_records("1999-01", FIX) == []
