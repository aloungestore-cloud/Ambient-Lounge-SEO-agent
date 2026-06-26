import os
from topic_engine.models import Topic
from topic_engine.dedup import published_slugs, dedup_topics

FIX = os.path.join(os.path.dirname(__file__), "fixtures")


def _t(slug):
    return Topic(phrase=slug.replace("-", " "), display_phrase=slug, slug=slug)


def test_published_slugs_from_sitemap():
    with open(os.path.join(FIX, "sitemap_sample.xml"), encoding="utf-8") as f:
        slugs = published_slugs(f.read())
    assert "kak-vybrat-lezhak-dlya-mastifa" in slugs
    assert "olefin-dlya-ulichnoy-mebeli" in slugs
    # non-blog URLs excluded
    assert "catalog" not in slugs


def test_drops_exact_published():
    out = dedup_topics([_t("olefin-dlya-ulichnoy-mebeli")],
                       published={"olefin-dlya-ulichnoy-mebeli"}, seen_slugs=set())
    assert out == []


def test_drops_seen_history():
    out = dedup_topics([_t("novaya-tema")], published=set(), seen_slugs={"novaya-tema"})
    assert out == []


def test_keeps_fresh():
    out = dedup_topics([_t("svezhaya-unikalnaya-tema")], published=set(), seen_slugs=set())
    assert len(out) == 1
