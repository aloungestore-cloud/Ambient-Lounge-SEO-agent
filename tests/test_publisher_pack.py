from __future__ import annotations
from publisher.pack import pack_post

ARTICLE = {
    "title": "Лежак для собаки",
    "preview_text": "...",
    "url": "/blog/lezhak-dlya-sobaki/",
    "preview_picture_url": "https://img.jpg",
}

def test_pack_short_text():
    result = pack_post("x" * 200, ARTICLE)
    assert len(result["text"]) <= 1200
    assert result["text"].startswith("x")

def test_pack_long_text():
    result = pack_post("y" * 2000, ARTICLE)
    assert len(result["text"]) <= 1200
    assert "…" in result["text"]
    assert "utm_source=tg" in result["text"]

def test_pack_id_format():
    result = pack_post("abc", ARTICLE)
    assert "-" in result["pack_id"]
    assert "lezhak-dlya-sobaki" in result["pack_id"]

def test_utm_in_url():
    result = pack_post("abc", ARTICLE)
    assert "utm_source=tg" in result["url"]
    assert "utm_medium=social" in result["url"]

def test_hashtag_brand():
    result = pack_post("abc", ARTICLE)
    assert "#ambientlounge" in result["hashtags"]
