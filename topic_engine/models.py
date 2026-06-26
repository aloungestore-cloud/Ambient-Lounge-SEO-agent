from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Record:
    phrase: str
    source: str
    raw_metric: float
    metric_kind: str
    intent: str | None = None
    theme: str | None = None
    zero_result: bool = False
    avg_results: float | None = None
    last_seen: str | None = None


@dataclass
class Topic:
    phrase: str
    display_phrase: str
    sources: list[str] = field(default_factory=list)
    raw_by_source: dict[str, float] = field(default_factory=dict)
    intent: str = "unknown"
    theme: str | None = None
    zero_result: bool = False
    media_available: bool = False
    section_id: int = 175
    section_url: str = "/blog/poleznye-sovety/"
    slug: str = ""
    h1: str = ""
    score: float = 0.0
    rank: int = 0
