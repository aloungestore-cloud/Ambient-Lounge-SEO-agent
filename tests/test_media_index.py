import json
import os
from topic_engine.media_index import load_media_index


def test_builds_index(tmp_path):
    breeds = tmp_path / "breed.json"
    heroes = tmp_path / "heroes.json"
    breeds.write_text(json.dumps({"labrador": {"folder": "Labrador"}, "haski": {}}), encoding="utf-8")
    heroes.write_text(json.dumps({"XXL": [{"name": "Blue Dream Sheep"}]}), encoding="utf-8")
    idx = load_media_index(str(breeds), str(heroes))
    assert "labrador" in idx
    assert "haski" in idx
    assert "blue" in idx  # hero name tokenized


def test_missing_files_no_raise():
    assert load_media_index("/no/a.json", "/no/b.json") == set()
