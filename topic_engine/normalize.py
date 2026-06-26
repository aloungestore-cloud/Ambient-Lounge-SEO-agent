import re

# keep word chars, spaces and hyphen (hi-lux); drop other punctuation
_PUNCT = re.compile(r"[^\w\s-]", re.UNICODE)
_SPACES = re.compile(r"\s+")


def normalize_phrase(phrase: str) -> str:
    t = (phrase or "").lower().replace("ё", "е")
    t = _PUNCT.sub("", t)
    t = _SPACES.sub(" ", t).strip()
    return t
