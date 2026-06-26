from topic_engine.intent import classify_intent


def test_pet():
    assert classify_intent("лежак для овчарки") == "pet"
    assert classify_intent("подстилка для щенка лабрадора") == "pet"


def test_b2b():
    assert classify_intent("мебель для отеля horeca") == "b2b"
    assert classify_intent("кресла для лаунж зоны оптом") == "b2b"


def test_buy():
    assert classify_intent("купить бескаркасный диван") == "buy"
    assert classify_intent("угловой диван цена доставка") == "buy"


def test_compare():
    assert classify_intent("hi-lux или so-lux что лучше") == "compare"
    assert classify_intent("олефин vs оксфорд сравнение") == "compare"


def test_info():
    assert classify_intent("что такое бескаркасная мебель") == "info"
    assert classify_intent("как выбрать наполнитель") == "info"


def test_unknown():
    assert classify_intent("амбиент лаунж") == "unknown"


def test_pet_beats_buy():
    # pet has highest priority even with commercial words
    assert classify_intent("купить лежак для собаки") == "pet"
