from __future__ import annotations


def generate_post(
    article: dict,
    claude_client,
    model: str = "claude-haiku-4-5-20251001",
) -> str:
    """Call Claude API to generate Telegram post text from article dict.
    article keys used: title, preview_text.
    Raises ValueError("empty response from Claude") if response text is empty.
    Returns raw text string (no URLs, no hashtags - those are added by pack.py).
    """
    title = article.get("title", "")
    preview_text = article.get("preview_text", "")

    prompt = f"""Ты — SMM-редактор бренда Ambient Lounge (дизайнерская бескаркасная мебель, лежаки для животных).
Напиши пост для Telegram-канала по статье блога.

Заголовок статьи: {title}
Краткое описание: {preview_text}

Требования:
- Структура AIDA (внимание → интерес → желание → действие)
- Тон: живой, экспертный, без пафоса
- Без нумерованных списков и маркеров — только прозаические абзацы
- Один призыв к действию в конце (читать статью)
- Длина: 800–1000 символов
- Без эмодзи в тексте (хэштеги добавит другой модуль)
- Не повторять URL — его добавит другой модуль

Верни ТОЛЬКО текст поста, без пояснений."""

    response = claude_client.messages.create(
        model=model,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()

    if not text:
        raise ValueError("empty response from Claude")

    return text
