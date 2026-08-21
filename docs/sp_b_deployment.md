# SP-B Deployment Runbook

Comprehensive deployment guide for the SEO-AIO SP-B Telegram Channel Publisher system.

## Prerequisites

Before starting deployment, ensure you have:

- **Docker** installed and running on the server (version 20.10+)
- **certbot** installed for TLS certificate management
- **n8n account** (free tier sufficient)
- **Telegram BotFather** access to create and manage bots
- **Existing Bitrix API key** (for Bitrix REST API integration)
- **SSH access** to server 157.22.207.183 as user `bitrix`
- **nginx** configured with proxy_pass capabilities

## Step 1: Deploy n8n with Docker

SSH into the server as user `bitrix`:

```bash
ssh bitrix@157.22.207.183
```

Create n8n directories and configuration:

```bash
mkdir -p /home/bitrix/n8n
cd /home/bitrix/n8n
```

Create the Docker Compose file:

```bash
cat > /home/bitrix/n8n/docker-compose.yml << 'EOF'
services:
  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped
    ports:
      - "127.0.0.1:5678:5678"
    volumes:
      - /home/bitrix/n8n_data:/home/node/.n8n
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=${N8N_ADMIN_PASSWORD}
      - WEBHOOK_URL=https://n8n.ambientlounge.ru/
      - GENERIC_TIMEZONE=Europe/Moscow
      - N8N_LOG_LEVEL=info
EOF
```

Start the n8n container:

```bash
docker compose -f /home/bitrix/n8n/docker-compose.yml up -d
```

Verify n8n is running:

```bash
docker ps | grep n8n
docker logs n8n
```

## Step 2: nginx vhost + TLS

Create nginx configuration for n8n.ambientlounge.ru. Add this to your nginx configuration (e.g., `/etc/nginx/sites-available/n8n`):

```nginx
upstream n8n_backend {
    server 127.0.0.1:5678;
}

server {
    listen 80;
    server_name n8n.ambientlounge.ru;
    
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
    
    location / {
        return 301 https://$server_name$request_uri;
    }
}

server {
    listen 443 ssl http2;
    server_name n8n.ambientlounge.ru;
    
    ssl_certificate /etc/letsencrypt/live/n8n.ambientlounge.ru/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/n8n.ambientlounge.ru/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    # Webhook endpoint - open to all
    location /webhook/ {
        proxy_pass http://n8n_backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # API endpoints - IP whitelisted
    location /rest/ {
        allow 127.0.0.1;
        allow 192.168.0.0/16;  # Adjust to your internal IP range
        deny all;
        
        proxy_pass http://n8n_backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # UI and other endpoints - IP whitelisted
    location / {
        allow 127.0.0.1;
        allow 192.168.0.0/16;  # Adjust to your internal IP range
        deny all;
        
        proxy_pass http://n8n_backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 90;
    }
}
```

Enable the nginx site and test configuration:

```bash
sudo ln -s /etc/nginx/sites-available/n8n /etc/nginx/sites-enabled/n8n
sudo nginx -t
sudo systemctl reload nginx
```

Generate TLS certificate using certbot:

```bash
sudo certbot certonly --webroot -w /var/www/certbot \
  -d n8n.ambientlounge.ru \
  --email smokva.ais@gmail.com \
  --agree-tos --non-interactive
```

Set up certificate auto-renewal:

```bash
sudo certbot renew --dry-run
```

## Step 3: Create Telegram bot and channel

### Create bot via BotFather

1. Open Telegram and search for `@BotFather`
2. Send command `/newbot`
3. Follow the prompts to choose a name and username
4. Copy the bot **API token** (looks like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

### Create Telegram channel

1. Create a new Telegram channel (or use existing)
2. Add the bot as admin with **Post Messages** permission
3. Make sure channel is set to private or restricted

### Get owner chat_id

Send a message to the bot (e.g., `/start`), then retrieve updates:

```bash
curl "https://api.telegram.org/bot{YOUR_BOT_TOKEN}/getUpdates"
```

Find `message.chat.id` from the response. This is your **owner chat_id**.

### Get channel_id

Use the getChat method with your channel username or ID:

```bash
curl "https://api.telegram.org/bot{YOUR_BOT_TOKEN}/getChat?chat_id=@your_channel_username"
```

The `id` field in the response is your **channel_id** (negative number for groups/channels).

## Step 4: Import n8n workflows

1. Open n8n UI: https://n8n.ambientlounge.ru/ (use admin credentials from Step 1)
2. Click **Workflows** → **Import from file**
3. Select `n8n/al-tg-receive.json` and import
4. Repeat for `n8n/al-tg-callback.json`

For each workflow:

1. Open the workflow
2. Edit **Telegram nodes** (receive, send message, answer callback):
   - Click on the Telegram node
   - Select **Credentials** dropdown
   - Choose or create new Telegram credentials
   - Paste your bot **API token**
3. Save the workflow

## Step 5: Set n8n environment variables

Access n8n container and set required variables:

```bash
docker exec -it n8n bash
```

Inside the container, set:

```bash
export TG_OWNER_CHAT_ID="<owner_chat_id>"
export TG_CHANNEL_ID="<channel_id>"
export CONTENT_BOT_TOKEN="<bot_api_token>"
export N8N_ENCRYPTION_KEY="$(openssl rand -base64 32)"
```

These can also be set in the `docker-compose.yml` environment section or via n8n UI credentials.

## Step 6: Register Telegram webhook

Register the webhook URL with Telegram. Replace `{TOKEN}` with your bot API token:

```bash
curl -X POST "https://api.telegram.org/bot{TOKEN}/setWebhook" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://n8n.ambientlounge.ru/webhook/al-tg-receive",
    "allowed_updates": ["message", "callback_query"]
  }'
```

Expected response:

```json
{"ok":true,"result":true,"description":"Webhook was set"}
```

Verify webhook is configured:

```bash
curl "https://api.telegram.org/bot{TOKEN}/getWebhookInfo"
```

## Step 7: Configure server environment

Add or update n8n configuration in the server environment file:

```bash
cat >> /home/bitrix/cron/al_seo_aio.env << 'EOF'
N8N_TG_WEBHOOK_URL=https://n8n.ambientlounge.ru/webhook/al-tg-receive
N8N_ADMIN_PASSWORD=$(openssl rand -base64 32)
EOF
```

Apply permissions:

```bash
chmod 600 /home/bitrix/cron/al_seo_aio.env
```

## Step 8: Activate workflows

1. In n8n UI, open **al-tg-receive** workflow
2. Toggle the **Active** switch (top-right) to **ON**
3. Repeat for **al-tg-callback** workflow
4. Save workflows

Both workflows are now listening for Telegram updates.

## Step 9: E2E Test Checklist

### Test 1: Dry run pack generation

```bash
cd /home/bitrix/www/sp_b
python3 -u publisher/al_tg_pack.py \
  --article-url "https://ambientlounge.ru/blog/golden-retriever-lounge/" \
  --dry-run
```

Expected output:

- Pack dictionary printed to stdout
- No message sent to Telegram
- No errors in logs

### Test 2: Send preview message

```bash
cd /home/bitrix/www/sp_b
python3 -u publisher/al_tg_pack.py \
  --article-url "https://ambientlounge.ru/blog/golden-retriever-lounge/"
```

Expected behavior:

- Preview message appears in your Telegram DM (owner chat)
- Message contains article title, image, and 2 buttons:
  - ✅ Опубликовать (Publish)
  - ❌ Отклонить (Reject)

### Test 3: Publish via callback

1. In Telegram DM, tap **✅ Опубликовать**
2. Expected:
   - Post immediately appears in the channel
   - Button callback responds with "Опубликовано ✅"
   - Event logged to n8n execution list

### Test 4: Duplicate publication protection

1. Tap the same button again
2. Expected:
   - Callback responds with "уже обработано" (already processed)
   - No duplicate post in channel

### Test 5: Queue processing

```bash
cd /home/bitrix/www/sp_b
python3 -u publisher/al_tg_pack.py \
  --from-queue \
  --dry-run
```

Expected output:

- If queue has items: first pending item data printed
- If queue is empty: "Queue empty"
- No messages sent

## Troubleshooting

### n8n logs

View n8n container logs in real-time:

```bash
docker logs -f n8n
```

Look for errors related to Telegram API, webhook execution, or credential issues.

### Python execution logs

Monitor Python script execution:

```bash
tail -f /var/log/bitrix/seo_aio_tg.log
```

(Log file to be configured in production setup)

### n8n Execution List

Access the n8n execution history (IP-gated):

```
https://n8n.ambientlounge.ru/executions
```

Shows:

- Workflow execution status
- Input/output data
- Error messages
- Execution duration

Filter by workflow name or status to debug specific issues.

### Telegram webhook status

Check if Telegram can reach your webhook:

```bash
curl "https://api.telegram.org/bot{TOKEN}/getWebhookInfo"
```

Response details:

- `pending_update_count`: updates waiting to be processed
- `last_error_date`: timestamp of last connection error
- `last_error_message`: reason for webhook failure
- `ip_address`: Telegram's last known IP (useful for firewall debugging)

### Common issues

**Issue: "Webhook was not set"**

- Verify nginx is accessible from Telegram servers
- Check firewall allows HTTPS (port 443)
- Ensure TLS certificate is valid: `sudo certbot renew --dry-run`
- Verify webhook URL format: `https://n8n.ambientlounge.ru/webhook/{workflow_trigger_id}`

**Issue: "n8n webhook endpoint not found (404)"**

- Verify workflow is imported and active
- Check webhook path matches workflow trigger ID
- Ensure n8n UI can access the workflow execution logs

**Issue: "Telegram credentials invalid"**

- Verify bot token copied correctly from BotFather
- Check token hasn't been regenerated
- Ensure no whitespace in token string

**Issue: "Message send failed"**

- Verify channel_id is correct (should be negative number)
- Confirm bot is admin in the channel
- Check bot has "Post Messages" permission

**Issue: "nginx 502 Bad Gateway"**

- Verify n8n container is running: `docker ps`
- Check n8n logs: `docker logs n8n`
- Verify upstream address in nginx config (127.0.0.1:5678)

## Rollback procedures

### Disable webhook (emergency pause)

```bash
curl -X POST "https://api.telegram.org/bot{TOKEN}/deleteWebhook"
```

This stops Telegram from sending updates. Workflows will not trigger until webhook is re-registered.

### Stop n8n container

```bash
docker compose -f /home/bitrix/n8n/docker-compose.yml down
```

### Restore from backup

n8n data is persisted in `/home/bitrix/n8n_data`. If you need to restore:

```bash
# Backup current state
cp -r /home/bitrix/n8n_data /home/bitrix/n8n_data.backup

# Restore from archive (if available)
tar -xzf /path/to/n8n_data.tar.gz -C /home/bitrix/
docker compose -f /home/bitrix/n8n/docker-compose.yml restart n8n
```

## Post-deployment checklist

- [ ] n8n container running and accessible
- [ ] nginx vhost configured and TLS certificate valid
- [ ] Telegram bot created and token saved
- [ ] Bot added as admin to channel
- [ ] Owner chat_id and channel_id documented
- [ ] n8n workflows imported and active
- [ ] Telegram webhook registered and verified
- [ ] Environment variables set in /home/bitrix/cron/al_seo_aio.env
- [ ] E2E test checklist completed successfully
- [ ] Monitoring and logging configured
- [ ] Backup strategy implemented

## Support and maintenance

- Review n8n execution logs weekly
- Monitor Telegram webhook info for pending updates or errors
- Update Docker images monthly: `docker pull n8nio/n8n:latest && docker compose up -d`
- Renew TLS certificate 30 days before expiration (certbot auto-renews with cron)
- Test webhook connectivity monthly: `curl https://api.telegram.org/bot{TOKEN}/getWebhookInfo`
