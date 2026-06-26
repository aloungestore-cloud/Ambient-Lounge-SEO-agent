import json
import logging
import os

log = logging.getLogger("topic_engine.media_index")


def _load(path: str):
    if not os.path.isfile(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError) as e:
        log.warning("media_index: skip %s (%s)", path, e)
        return None


def load_media_index(breed_photos_path: str, product_heroes_path: str) -> set[str]:
    idx: set[str] = set()
    breeds = _load(breed_photos_path)
    if isinstance(breeds, dict):
        idx.update(k.lower() for k in breeds.keys())
    heroes = _load(product_heroes_path)
    if isinstance(heroes, dict):
        for items in heroes.values():
            for it in (items or []):
                name = (it.get("name") or "") if isinstance(it, dict) else ""
                idx.update(tok.lower() for tok in name.split() if len(tok) > 2)
    return idx
