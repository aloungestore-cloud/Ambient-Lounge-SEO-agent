from topic_engine.adapters.mia_chat import mia_chat_records

HEADER = ["ts", "chat_id", "msg", "intent", "a", "b", "c"]


def _row(ts, msg, intent="info"):
    return [ts, "c1", msg, intent, "", "", ""]


def test_filters_spam_and_short():
    rows = [
        HEADER,
        _row("2026-06-25 10:00:00", "какой наполнитель лучше для кресла мешка"),
        _row("2026-06-25 10:01:00", "ok"),                      # too short
        _row("2026-06-25 10:02:00", "спам", "irrelevant_spam"),  # spam intent
        _row("2026-06-25 10:03:00", "[вложение]"),               # starts with [
    ]
    recs = mia_chat_records(rows, days=7, now_iso="2026-06-26 12:00:00")
    phrases = [r.phrase for r in recs]
    assert phrases == ["какой наполнитель лучше для кресла мешка"]
    assert recs[0].source == "mia_chat"
    assert recs[0].metric_kind == "mentions"


def test_dedup_counts_repeats():
    rows = [
        HEADER,
        _row("2026-06-25 10:00:00", "лежак для хаски какой размер"),
        _row("2026-06-25 11:00:00", "Лежак для хаски какой размер"),  # case-dup
    ]
    recs = mia_chat_records(rows, days=7, now_iso="2026-06-26 12:00:00")
    assert len(recs) == 1
    assert recs[0].raw_metric == 2.0


def test_respects_cutoff():
    rows = [
        HEADER,
        _row("2026-05-01 10:00:00", "старое сообщение про диваны для дачи"),
    ]
    recs = mia_chat_records(rows, days=7, now_iso="2026-06-26 12:00:00")
    assert recs == []
