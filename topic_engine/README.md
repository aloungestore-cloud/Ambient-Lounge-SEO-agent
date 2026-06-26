# topic_engine — SP-A unified topic mining

Collects demand signals from 5 sources → ranked weekly topic queue.

## Run
    python3 al_topic_engine.py --dry-run            # print, no writes
    python3 al_topic_engine.py --week 2026-26       # specific week
    python3 al_topic_engine.py                       # current ISO week, full run

## Sources (graceful degradation — any may be absent)
| name | input | needs |
|---|---|---|
| mia_chat | Google Sheet (Mia dialogs) | GOOGLE_SERVICE_ACCOUNT_JSON, GOOGLE_SHEETS_ID |
| onsite_search | mia_queries API | SEO_AIO_API_KEY |
| wordstat | /upload/al_seo_aio/wordstat-weekly/<week>.tsv | (collector token) |
| gsc | .../gsc-weekly/<week>.tsv | (collector token) |
| metrika | .../metrika-weekly/<week>.tsv | (collector token) |

## Output
- outputs/topics/<week>.json  (machine queue for the writer / future n8n)
- docs/content_calendar.md     (section `<!-- topic-engine:<week> -->`)
- Telegram digest to owner

## Tests
    python3 -m pytest -q
