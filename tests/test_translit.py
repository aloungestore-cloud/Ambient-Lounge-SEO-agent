from topic_engine.translit import slugify


def test_basic():
    assert slugify("Бескаркасный диван для дачи") == "beskarkasnyy-divan-dlya-dachi"


def test_keeps_latin_and_digits():
    assert slugify("Pet Lounge XXL 90см") == "pet-lounge-xxl-90sm"


def test_collapses_hyphens():
    assert slugify("hi-lux  vs  so-lux") == "hi-lux-vs-so-lux"
