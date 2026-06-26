import re

IDEAS_HEADING = "## Идеи из реальных вопросов клиентов"


def upsert_calendar(calendar_text: str, week: str, section_md: str) -> str:
    marker = f"<!-- topic-engine:{week} -->"
    if marker in calendar_text:
        # replace from marker up to next "## " heading or EOF
        pattern = re.compile(
            re.escape(marker) + r".*?(?=\n## |\Z)", re.DOTALL)
        return pattern.sub(section_md.rstrip() + "\n", calendar_text, count=1)
    if IDEAS_HEADING in calendar_text:
        idx = calendar_text.index(IDEAS_HEADING)
        return calendar_text[:idx] + section_md.rstrip() + "\n\n" + calendar_text[idx:]
    return calendar_text.rstrip() + "\n\n" + section_md.rstrip() + "\n"
