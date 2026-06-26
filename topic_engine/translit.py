import re

_MAP = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ж": "zh",
    "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f",
    "х": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "", "ы": "y",
    "ь": "", "э": "e", "ю": "yu", "я": "ya",
}
_NONWORD = re.compile(r"[^a-z0-9-]+")
_HYPHENS = re.compile(r"-+")


def slugify(text: str) -> str:
    t = (text or "").lower().replace("ё", "е")
    t = "".join(_MAP.get(ch, ch) for ch in t)
    t = t.replace(" ", "-")
    t = _NONWORD.sub("-", t)
    t = _HYPHENS.sub("-", t).strip("-")
    return t
