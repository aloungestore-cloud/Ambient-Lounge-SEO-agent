import re

from topic_engine.models import Topic

_BLOG_LOC = re.compile(r"<loc>\s*(https?://[^<]*?/blog/[^<]*?)\s*</loc>", re.IGNORECASE)


def published_slugs(sitemap_xml: str) -> set[str]:
    slugs: set[str] = set()
    for url in _BLOG_LOC.findall(sitemap_xml or ""):
        seg = url.rstrip("/").rsplit("/", 1)[-1]
        if seg and seg != "blog":
            slugs.add(seg.lower())
    return slugs


def _tokens(slug: str) -> set[str]:
    return {p for p in slug.split("-") if len(p) > 2}


def dedup_topics(topics: list[Topic], published: set[str], seen_slugs: set[str]) -> list[Topic]:
    pub_token_sets = [_tokens(s) for s in published]
    out: list[Topic] = []
    for t in topics:
        if t.slug in published or t.slug in seen_slugs:
            continue
        cand = _tokens(t.slug)
        if cand and any(cand <= pts for pts in pub_token_sets):
            continue  # candidate fully covered by an existing article's slug
        out.append(t)
    return out
