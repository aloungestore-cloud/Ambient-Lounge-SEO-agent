"""Keyword intent classifier mirroring the Bitrix mia_queries breakdown.

Priority order (first match wins): pet > b2b > compare > buy > info > unknown.
pet/b2b are checked first so commercial words ("купить лежак для собаки")
still resolve to their domain bucket.
"""

PET = ("лежак", "лежанк", "подстилк", "собак", "собаки", "кошк", "щен", "порода",
       "овчарк", "лабрадор", "питом", "pet lounge", "когот", "антикогот")
B2B = ("horeca", "хорека", "отель", "ресторан", "коворкинг", "лаунж зон", "опт",
       "проект", "дизайнер", "контракт", "шоурум", "бар ", "офис", "spa", "спа-центр")
COMPARE = (" vs ", " или ", "сравнен", "что лучше", "разниц", "чем отлич", "против")
BUY = ("купить", "заказать", "цена", "цены", "стоимость", "недорого", "доставка",
       "со склада", "в наличии", "акция", "скидка", "руб")
INFO = ("что такое", "как ", "почему", "зачем", "можно ли", "гид", "инструкц",
        "уход", "чистка", "сколько", "какой", "какую", "какие")


def _has(text: str, needles) -> bool:
    return any(n in text for n in needles)


def classify_intent(phrase: str) -> str:
    t = f" {phrase.lower().strip()} "
    if _has(t, PET):
        return "pet"
    if _has(t, B2B):
        return "b2b"
    if _has(t, COMPARE):
        return "compare"
    if _has(t, BUY):
        return "buy"
    if _has(t, INFO):
        return "info"
    return "unknown"
