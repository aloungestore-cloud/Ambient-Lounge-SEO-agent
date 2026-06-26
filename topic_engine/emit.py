import json
import os


def build_queue_dict(week, generated_at, sources_used, sources_skipped,
                     total_candidates, topics) -> dict:
    return {
        "week": week,
        "generated_at": generated_at,
        "sources_used": sources_used,
        "sources_skipped": sources_skipped,
        "total_candidates": total_candidates,
        "after_dedup": len(topics),
        "topics": [
            {
                "rank": t.rank,
                "phrase": t.display_phrase,
                "score": t.score,
                "intent": t.intent,
                "section_id": t.section_id,
                "section_url": t.section_url,
                "slug": t.slug,
                "h1": t.h1,
                "sources": t.sources,
                "zero_result": t.zero_result,
                "media_available": t.media_available,
            }
            for t in topics
        ],
    }


def write_queue_json(out_dir: str, week: str, queue_dict: dict) -> str:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{week}.json")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(queue_dict, fh, ensure_ascii=False, indent=2)
    os.replace(tmp, path)
    return path


def render_calendar_section(week: str, topics: list, top_n: int = 15) -> str:
    lines = [
        f"<!-- topic-engine:{week} -->",
        f"### Темы недели {week} (auto, источник: topic-engine)",
        "",
        "| # | Тема | Интент | Раздел | Score | Источники | zero |",
        "|---|------|--------|--------|-------|-----------|------|",
    ]
    for t in topics[:top_n]:
        zr = "⚠️" if t.zero_result else ""
        lines.append(
            f"| {t.rank} | {t.display_phrase} | {t.intent} | {t.section_id} | "
            f"{t.score} | {', '.join(t.sources)} | {zr} |"
        )
    return "\n".join(lines) + "\n"
