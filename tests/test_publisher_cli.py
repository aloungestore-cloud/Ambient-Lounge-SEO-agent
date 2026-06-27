from __future__ import annotations
import json
import sys
import os
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path

# We test run_for_url and run_from_queue directly (not via subprocess)
# to avoid needing real env vars.

def _make_article():
    return {
        "title": "Test",
        "preview_text": "...",
        "url": "/blog/test/",
        "preview_picture_url": "",
    }

def test_dry_run_no_post(tmp_path):
    """--dry-run must NOT call post_to_n8n."""
    import importlib, types
    # patch all IO deps
    with patch.dict(os.environ, {"SEO_AIO_API_KEY": "x", "ANTHROPIC_API_KEY": "x", "N8N_TG_WEBHOOK_URL": "https://n.example.com/w"}):
        with patch("publisher.fetch.fetch_article", return_value=_make_article()) as mock_fetch, \
             patch("publisher.generate.generate_post", return_value="пост текст") as mock_gen, \
             patch("publisher.post.post_to_n8n") as mock_post, \
             patch("anthropic.Anthropic", return_value=MagicMock()):
            # import inside patch context to pick up env
            import al_tg_pack
            importlib.reload(al_tg_pack)
            rc = al_tg_pack.run_for_url("https://ambientlounge.ru/blog/test/", dry_run=True)
    assert rc == 0
    mock_post.assert_not_called()

def test_from_queue_empty(tmp_path):
    """Empty queue.json → exit 0, no error."""
    queue_file = tmp_path / "queue.json"
    queue_file.write_text("[]", encoding="utf-8")
    with patch.dict(os.environ, {"SEO_AIO_API_KEY": "x"}):
        import al_tg_pack
        import importlib
        importlib.reload(al_tg_pack)
        al_tg_pack.QUEUE_FILE = queue_file
        rc = al_tg_pack.run_from_queue(dry_run=True)
    assert rc == 0

def test_from_queue_picks_first_pending(tmp_path):
    """run_from_queue picks the first pending item and calls run_for_url."""
    items = [
        {"slug": "test-article", "status": "pending"},
        {"slug": "other-article", "status": "done"},
    ]
    queue_file = tmp_path / "queue.json"
    queue_file.write_text(json.dumps(items), encoding="utf-8")
    with patch.dict(os.environ, {"SEO_AIO_API_KEY": "x", "ANTHROPIC_API_KEY": "x", "N8N_TG_WEBHOOK_URL": "https://n.x/w"}):
        import al_tg_pack
        import importlib
        importlib.reload(al_tg_pack)
        al_tg_pack.QUEUE_FILE = queue_file
        with patch.object(al_tg_pack, "run_for_url", return_value=0) as mock_run:
            rc = al_tg_pack.run_from_queue(dry_run=True)
    assert rc == 0
    mock_run.assert_called_once()
    called_url = mock_run.call_args[0][0]
    assert "test-article" in called_url
