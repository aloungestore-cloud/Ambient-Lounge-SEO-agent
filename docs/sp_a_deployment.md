# SP-A Deployment Runbook (prod 157.22.207.183)

## 1. Code
    sudo install -d -o bitrix -g bitrix /opt/al-seo
    sudo -u bitrix git clone git@github-seo:aloungestore-cloud/Ambient-Lounge-SEO-agent.git /opt/al-seo
    cd /opt/al-seo && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

## 2. Secrets — append to /home/bitrix/cron/al_seo_aio.env (chmod 600, owner bitrix)
    SEO_AIO_API_KEY=...            # already present
    GOOGLE_SHEETS_ID=1xq0J0hyWBl_kSKuURIAtRPS3Ea8xbOwRDq82jeorGxc
    GOOGLE_SHEETS_GID=421239372
    GOOGLE_SERVICE_ACCOUNT_JSON=/opt/al-agent/credentials/service_account.json
    TG_BOT_TOKEN=...               # Mia's bot
    TG_OWNER_CHAT_ID=...
    # collectors (add as approvals land):
    YANDEX_DIRECT_OAUTH_TOKEN=...
    METRIKA_OAUTH_TOKEN=...
    METRIKA_COUNTER_ID=...

## 3. Collectors on Bitrix server
    sudo cp /opt/al-seo/scripts/al_metrika_weekly.php /home/bitrix/cron/
    sudo -u bitrix php /home/bitrix/cron/al_metrika_weekly.php --dry-run   # smoke test
    sudo -u bitrix php /home/bitrix/cron/al_wordstat_weekly.php --dry-run
    sudo -u bitrix php /home/bitrix/cron/al_gsc_weekly.php --dry-run

## 4. Cron (crontab -u bitrix -e)
    0 5 * * 0 /usr/bin/php /home/bitrix/cron/al_gsc_weekly.php
    0 5 * * 0 /usr/bin/php /home/bitrix/cron/al_metrika_weekly.php
    0 6 * * 0 /usr/bin/php /home/bitrix/cron/al_wordstat_weekly.php
    0 10 * * 0 cd /opt/al-seo && .venv/bin/python al_topic_engine.py >> /var/log/bitrix/seo_aio_topics.log 2>&1

## 5. First run (after secrets) — dry then live
    cd /opt/al-seo && .venv/bin/python al_topic_engine.py --dry-run
    .venv/bin/python al_topic_engine.py

## 6. Retire harvester (after 1 successful engine cycle)
    crontab -u bitrix -l | grep -v seo_idea_harvester | crontab -u bitrix -
    # mark tools/seo_idea_harvester.py deprecated (header comment), keep as reference 1 cycle
