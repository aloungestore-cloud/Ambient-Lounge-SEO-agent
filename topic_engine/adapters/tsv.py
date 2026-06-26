from __future__ import annotations

"""Adapters for the weekly TSV files written by PHP collectors on prod.

Contracts (verbatim):
  wordstat: phrase   impressions  theme  week_iso
  gsc:      query    clicks  impressions  ctr_pct  position  week_iso
  metrika:  phrase   visits  theme  week_iso
"""
import csv
import os
import logging

from topic_engine.models import Record

log = logging.getLogger("topic_engine.tsv")


def read_tsv_records(path: str, source: str, phrase_col: str, metric_col: str,
                     metric_kind: str, theme_col: str | None = None) -> list[Record]:
    if not os.path.isfile(path):
        log.warning("tsv adapter %s: file not found %s", source, path)
        return []
    out: list[Record] = []
    with open(path, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            phrase = (row.get(phrase_col) or "").strip()
            if not phrase:
                continue
            try:
                metric = float(row.get(metric_col) or 0)
            except ValueError:
                metric = 0.0
            if metric <= 0:
                continue
            theme = (row.get(theme_col) or None) if theme_col else None
            out.append(Record(phrase=phrase, source=source, raw_metric=metric,
                              metric_kind=metric_kind, theme=theme))
    return out


def _path(base_dir: str, source: str, week: str) -> str:
    # Tests use a shared fixtures dir with "<source>_<week>.tsv".
    # Prod passes the per-source directory; pattern collapses to "<week>.tsv".
    prefixed = os.path.join(base_dir, f"{source}_{week}.tsv")
    if os.path.isfile(prefixed):
        return prefixed
    return os.path.join(base_dir, f"{week}.tsv")


def wordstat_records(week: str, base_dir: str) -> list[Record]:
    return read_tsv_records(_path(base_dir, "wordstat", week), "wordstat",
                            "phrase", "impressions", "impressions", "theme")


def gsc_records(week: str, base_dir: str) -> list[Record]:
    return read_tsv_records(_path(base_dir, "gsc", week), "gsc",
                            "query", "impressions", "impressions", None)


def metrika_records(week: str, base_dir: str) -> list[Record]:
    return read_tsv_records(_path(base_dir, "metrika", week), "metrika",
                            "phrase", "visits", "visits", "theme")
