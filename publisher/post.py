from __future__ import annotations
import requests


def post_to_n8n(
    pack: dict,
    webhook_url: str,
    http_post=requests.post,
    timeout: int = 15,
) -> None:
    """POST pack dict as JSON to n8n webhook URL.
    Raises ValueError on HTTP != 2xx or requests exceptions.
    """
    try:
        resp = http_post(webhook_url, json=pack, timeout=timeout)
    except requests.exceptions.RequestException as exc:
        raise ValueError(f"post_to_n8n network error: {exc}") from exc
    if not (200 <= resp.status_code < 300):
        raise ValueError(f"n8n returned {resp.status_code}: {resp.text[:200]}")
