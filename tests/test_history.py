import os
from topic_engine.history import load_seen_slugs

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "topics_history")


def test_collects_slugs():
    seen = load_seen_slugs(FIX)
    assert "lezhak-dlya-haski" in seen


def test_missing_dir_empty():
    assert load_seen_slugs("/no/such/dir") == set()
