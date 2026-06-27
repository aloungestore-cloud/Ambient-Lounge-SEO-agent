from __future__ import annotations
import requests


def fetch_article(
    article_url: str,
    api_url: str,
    api_key: str,
    http_get=requests.get,
) -> dict:
    """GET {api_url}?action=get_article&url={article_url} with X-API-Key header.

    Returns dict with keys: title, preview_text, detail_text, url, preview_picture_url.
    Raises ValueError on HTTP != 200 or ok != True in response JSON.
    """
    params = {
        "action": "get_article",
        "url": article_url,
    }
    headers = {
        "X-API-Key": api_key,
    }

    response = http_get(api_url, params=params, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"HTTP {response.status_code} from API")

    data = response.json()

    if not data.get("ok", False):
        error_msg = data.get("error", "unknown error")
        raise ValueError(f"API error: {error_msg}")

    return data
