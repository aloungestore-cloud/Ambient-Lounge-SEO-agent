from __future__ import annotations
import pytest
import requests
from unittest.mock import MagicMock, patch
from publisher.post import post_to_n8n

PACK = {"pack_id": "2026-27-test", "text": "hello", "url": "https://x.ru"}

def test_post_ok():
    mock_http = MagicMock(return_value=MagicMock(status_code=200, text="ok"))
    post_to_n8n(PACK, "https://n8n.example.com/webhook/test", http_post=mock_http)
    mock_http.assert_called_once()
    call_kwargs = mock_http.call_args
    assert call_kwargs[1]["json"] == PACK  # keyword arg json=

def test_post_non2xx():
    mock_http = MagicMock(return_value=MagicMock(status_code=500, text="error"))
    with pytest.raises(ValueError, match="500"):
        post_to_n8n(PACK, "https://n8n.example.com/webhook/test", http_post=mock_http)

def test_post_network_error():
    def bad_http(*a, **kw):
        raise requests.exceptions.Timeout("timed out")
    with pytest.raises(ValueError, match="network error"):
        post_to_n8n(PACK, "https://n8n.example.com/webhook/test", http_post=bad_http)
