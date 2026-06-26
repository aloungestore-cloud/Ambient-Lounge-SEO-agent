from topic_engine.notify import render_digest, send_digest


def _q():
    return {
        "week": "2026-26", "sources_used": ["mia_chat", "wordstat"],
        "total_candidates": 213, "after_dedup": 47,
        "topics": [
            {"rank": 1, "phrase": "диван для дачи", "score": 0.91, "intent": "buy", "zero_result": False},
            {"rank": 2, "phrase": "лежак для хаски", "score": 0.84, "intent": "pet", "zero_result": True},
        ],
    }


def test_render_digest_contains_counts_and_top():
    txt = render_digest(_q())
    assert "2026-26" in txt
    assert "213" in txt and "47" in txt
    assert "диван для дачи" in txt
    assert "⚠️" in txt  # zero_result topic flagged


def test_send_digest_failure_is_swallowed():
    def _boom(url, json=None, timeout=None):
        raise RuntimeError("tg down")
    assert send_digest("hi", "TOK", "123", _boom) is False


def test_send_digest_success():
    calls = {}
    def _ok(url, json=None, timeout=None):
        calls["url"] = url
        return {"ok": True}
    assert send_digest("hi", "TOK", "123", _ok) is True
    assert "TOK" in calls["url"]
