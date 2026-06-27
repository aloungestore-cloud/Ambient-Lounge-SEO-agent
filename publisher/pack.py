from __future__ import annotations
import re
from datetime import datetime, timezone


def _current_week() -> str:
    """Return current ISO week as YYYY-WW (e.g. 2026-27)."""
    now = datetime.now(tz=timezone.utc)
    return now.strftime("%G-%V")


def pack_post(
    raw_text: str,
    article: dict,
    utm_source: str = "tg",
    max_len: int = 1200,
) -> dict:
    """Pack raw generated text with UTM URL, hashtags, and length limit.

    Returns dict with keys:
      pack_id: str  (e.g. "2026-27-lezhak-dlya-sobaki")
      text: str     (raw_text + footer, total ≤ max_len chars)
      url: str      (article url + UTM params)
      hashtags: str (e.g. "#ambientlounge #lezhakdlyasobaki")
      preview_url: str (from article.get("preview_picture_url", ""))
    """
    # 1. Extract slug from article["url"]: last non-empty path segment
    url = article.get("url", "")
    slug = url.rstrip("/").split("/")[-1]

    # 2. Build UTM URL
    base_url = url.rstrip("/")
    if "?" in base_url:
        utm_url = base_url + f"&utm_source={utm_source}&utm_medium=social&utm_campaign=sp-b"
    else:
        utm_url = base_url + f"?utm_source={utm_source}&utm_medium=social&utm_campaign=sp-b"

    # 3. Build hashtags
    hashtags = "#ambientlounge #" + slug.replace("-", "")

    # 4. Build footer
    footer = f"\n\n{utm_url}\n{hashtags}"

    # 5. Calculate available space
    available = max_len - len(footer)

    # 6. Truncate raw_text if needed
    if len(raw_text) > available:
        text_part = raw_text[:available - 1] + "…"
    else:
        text_part = raw_text

    # 7. Combine text and footer
    full_text = text_part + footer

    # 8. Build pack_id
    pack_id = _current_week() + "-" + slug

    # 9. Return the dict
    return {
        "pack_id": pack_id,
        "text": full_text,
        "url": utm_url,
        "hashtags": hashtags,
        "preview_url": article.get("preview_picture_url", ""),
    }
