import logging

log = logging.getLogger("topic_engine.notify")

_EMOJI = {"buy": "🔥", "b2b": "🏨", "compare": "⚖️", "pet": "🐾", "info": "💡", "unknown": "•"}


def render_digest(queue_dict: dict, top_n: int = 10) -> str:
    week = queue_dict.get("week", "?")
    used = ", ".join(queue_dict.get("sources_used", []))
    lines = [
        f"📊 Темы недели {week} (источники: {used})",
        f"Кандидатов: {queue_dict.get('total_candidates', 0)} → после дедупа: {queue_dict.get('after_dedup', 0)}",
        "",
        f"ТОП-{top_n}:",
    ]
    zeros = []
    for t in queue_dict.get("topics", [])[:top_n]:
        e = _EMOJI.get(t.get("intent", "unknown"), "•")
        flag = " ⚠️" if t.get("zero_result") else ""
        lines.append(f"{t['rank']}. {e} [{t.get('intent')}] {t['phrase']} — {t['score']}{flag}")
        if t.get("zero_result"):
            zeros.append(t["phrase"])
    if zeros:
        lines += ["", "⚠️ zero_result (искали, товара нет): " + "; ".join(zeros)]
    lines += ["", f"Полный список → outputs/topics/{week}.json"]
    return "\n".join(lines)


def send_digest(text: str, bot_token: str, chat_id: str, http_post) -> bool:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        http_post(url, json={"chat_id": chat_id, "text": text}, timeout=20)
        return True
    except Exception as e:  # noqa: BLE001
        log.warning("telegram digest failed: %s", e)
        return False
