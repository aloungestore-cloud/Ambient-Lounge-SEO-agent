import json
import os
from topic_engine.models import Topic
from topic_engine.emit import build_queue_dict, write_queue_json, render_calendar_section


def _t(rank, phrase, slug, score, intent="buy", sid=586):
    return Topic(phrase=phrase, display_phrase=phrase, slug=slug, score=score,
                 rank=rank, intent=intent, section_id=sid,
                 section_url="/blog/idei-dlya-interera/", sources=["wordstat"],
                 h1=phrase.capitalize())


def test_build_queue_dict_shape():
    q = build_queue_dict("2026-26", "2026-06-28T10:00:00+03:00",
                         ["wordstat"], ["gsc", "metrika"], 200,
                         [_t(1, "диван для дачи", "divan-dlya-dachi", 0.9)])
    assert q["week"] == "2026-26"
    assert q["sources_used"] == ["wordstat"]
    assert q["sources_skipped"] == ["gsc", "metrika"]
    assert q["total_candidates"] == 200
    assert q["after_dedup"] == 1
    assert q["topics"][0]["slug"] == "divan-dlya-dachi"
    assert q["topics"][0]["section_id"] == 586


def test_write_queue_json(tmp_path):
    q = build_queue_dict("2026-26", "t", ["wordstat"], [], 1,
                         [_t(1, "диван", "divan", 0.5)])
    path = write_queue_json(str(tmp_path), "2026-26", q)
    assert path.endswith("2026-26.json")
    with open(path, encoding="utf-8") as f:
        assert json.load(f)["week"] == "2026-26"


def test_render_calendar_section_has_marker_and_rows():
    md = render_calendar_section("2026-26", [_t(1, "диван для дачи", "d", 0.9)])
    assert "<!-- topic-engine:2026-26 -->" in md
    assert "диван для дачи" in md
    assert "| 1 |" in md
