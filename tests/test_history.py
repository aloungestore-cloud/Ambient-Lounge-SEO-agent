import json
import os
from topic_engine.history import load_seen_slugs

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "topics_history")


def test_collects_slugs():
    seen = load_seen_slugs(FIX)
    assert "lezhak-dlya-haski" in seen


def test_missing_dir_empty():
    assert load_seen_slugs("/no/such/dir") == set()


def test_malformed_topics_no_raise(tmp_path):
    # null topics — previously raised TypeError
    (tmp_path / "null_topics.json").write_text(json.dumps({"topics": None}), encoding="utf-8")
    # string topics — previously raised TypeError/AttributeError
    (tmp_path / "str_topics.json").write_text(json.dumps({"topics": "x"}), encoding="utf-8")
    # valid file with one real slug
    (tmp_path / "valid.json").write_text(
        json.dumps({"topics": [{"slug": "lezhak-dlya-haski"}]}), encoding="utf-8"
    )
    seen = load_seen_slugs(str(tmp_path))
    assert seen == {"lezhak-dlya-haski"}
