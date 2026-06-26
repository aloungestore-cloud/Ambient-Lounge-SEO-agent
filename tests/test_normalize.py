from topic_engine.normalize import normalize_phrase


def test_lowercase_and_trim():
    assert normalize_phrase("  Купить Диван  ") == "купить диван"


def test_yo_to_e():
    assert normalize_phrase("лёжак") == "лежак"


def test_collapse_spaces():
    assert normalize_phrase("диван   для    дачи") == "диван для дачи"


def test_strip_punctuation():
    assert normalize_phrase("hi-lux или so-lux?") == "hi-lux или so-lux"


def test_idempotent():
    once = normalize_phrase("Лёжак,  для Собаки!")
    assert normalize_phrase(once) == once
