SOURCE_WEIGHTS = {"mia_chat": 1.0, "onsite_search": 1.0, "gsc": 0.8, "metrika": 0.8, "wordstat": 0.7}
INTENT_WEIGHTS = {"buy": 1.5, "b2b": 1.4, "compare": 1.2, "pet": 1.1, "info": 1.0, "unknown": 0.8}
MEDIA_BONUS = 1.15
CATALOG_HAS = 1.1
CATALOG_ZERO = 0.85
CATALOG_UNKNOWN = 1.0
CORROB_STEP = 0.15
NORMALIZE_MODE = "minmax"  # "minmax" | "percentile"

UPLOAD_BASE = "/home/bitrix/www/upload/al_seo_aio"
WORDSTAT_DIR = f"{UPLOAD_BASE}/wordstat-weekly"
GSC_DIR = f"{UPLOAD_BASE}/gsc-weekly"
METRIKA_DIR = f"{UPLOAD_BASE}/metrika-weekly"

SITEMAP_URL = "https://ambientlounge.ru/sitemap.xml"
MIA_QUERIES_URL = "https://ambientlounge.ru/api/catalog.php"

SECTIONS = {
    "pet": (174, "/blog/obzory-lezhakov-dlya-zhivotnyh/"),
    "interior": (586, "/blog/idei-dlya-interera/"),
    "howto": (175, "/blog/poleznye-sovety/"),
}
