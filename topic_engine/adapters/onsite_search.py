import logging

from topic_engine.models import Record

log = logging.getLogger("topic_engine.onsite_search")


def onsite_search_records(api_url: str, api_key: str, http_get,
                          period_days: int = 7, limit: int = 500) -> list[Record]:
    params = {"action": "mia_queries", "period_days": period_days, "limit": limit}
    headers = {"X-API-Key": api_key}
    try:
        data = http_get(api_url, params=params, headers=headers)
    except Exception as e:  # noqa: BLE001 - adapter isolation
        log.warning("onsite_search adapter failed: %s", e)
        return []
    if not isinstance(data, dict) or not data.get("ok"):
        log.warning("onsite_search adapter: bad payload")
        return []
    out: list[Record] = []
    for q in data.get("queries", []):
        phrase = (q.get("phrase") or "").strip()
        if not phrase:
            continue
        out.append(Record(
            phrase=phrase,
            source="onsite_search",
            raw_metric=float(q.get("count") or 0),
            metric_kind="searches",
            intent=q.get("intent"),
            zero_result=bool(q.get("zero_result")),
            avg_results=(float(q["avg_results"]) if q.get("avg_results") is not None else None),
            last_seen=q.get("last_seen"),
        ))
    return out
