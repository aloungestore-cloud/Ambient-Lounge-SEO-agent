from topic_engine.models import Record
from topic_engine.engine import run, safe_fetch


def test_safe_fetch_isolates_failure():
    name, recs, ok = safe_fetch("boom", lambda: (_ for _ in ()).throw(RuntimeError("x")))
    assert name == "boom" and recs == [] and ok is False


def _deps(adapters):
    return {
        "adapters": adapters,  # dict name -> callable() -> list[Record]
        "media_index": set(),
        "published": set(),
        "seen_slugs": set(),
        "generated_at": "2026-06-28T10:00:00+03:00",
        "out_dir": "/tmp/ignored",
        "calendar_path": None,   # None => skip calendar write
        "git_push": None,        # None => skip
        "telegram": None,        # None => skip
    }


def test_run_end_to_end_dry():
    adapters = {
        "wordstat": lambda: [Record("купить диван для дачи", "wordstat", 1000, "impressions", theme="furniture")],
        "onsite_search": lambda: [Record("купить диван для дачи", "onsite_search", 8, "searches", intent="buy")],
        "metrika": lambda: (_ for _ in ()).throw(RuntimeError("no token")),  # fails → skipped
    }
    q = run(_deps(adapters), week="2026-26", dry_run=True)
    assert q["week"] == "2026-26"
    assert "metrika" in q["sources_skipped"]
    assert set(q["sources_used"]) == {"wordstat", "onsite_search"}
    assert q["topics"][0]["slug"] == "kupit-divan-dlya-dachi"
    assert q["topics"][0]["section_id"] == 586  # interior (диван) commercial


def test_run_dedup_removes_published():
    adapters = {"wordstat": lambda: [Record("олефин для уличной мебели", "wordstat", 500, "impressions")]}
    deps = _deps(adapters)
    deps["published"] = {"olefin-dlya-ulichnoy-mebeli"}
    q = run(deps, week="2026-26", dry_run=True)
    assert q["after_dedup"] == 0
