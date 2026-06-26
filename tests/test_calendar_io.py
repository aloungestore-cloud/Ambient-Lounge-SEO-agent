from topic_engine.calendar_io import upsert_calendar

BASE = """# Content Calendar

## Банк тем (scored, ещё не выбраны)
x

## Идеи из реальных вопросов клиентов (источник: чаты, май 2026)
y
"""


def test_inserts_before_ideas_section():
    out = upsert_calendar(BASE, "2026-26", "<!-- topic-engine:2026-26 -->\nNEW\n")
    assert out.index("NEW") < out.index("## Идеи из реальных")
    assert "## Банк тем" in out


def test_replaces_existing_same_week():
    seeded = BASE.replace(
        "## Идеи из реальных",
        "<!-- topic-engine:2026-26 -->\nOLD\n\n## Идеи из реальных",
    )
    out = upsert_calendar(seeded, "2026-26", "<!-- topic-engine:2026-26 -->\nNEW\n")
    assert "OLD" not in out
    assert "NEW" in out
    assert out.count("<!-- topic-engine:2026-26 -->") == 1
