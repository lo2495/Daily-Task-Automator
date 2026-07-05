import json
import urllib.request
import logging
from config import DISCORD_WEBHOOK_URL

def send_discord_message(content):
    if not DISCORD_WEBHOOK_URL or "discord.com/api/webhooks" not in DISCORD_WEBHOOK_URL:
        logging.error("未設定正確的 Discord Webhook 網址。")
        return
    
    payload = {"content": content}
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        DISCORD_WEBHOOK_URL, 
        data=data, 
        headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 204:
                logging.info("Discord 訊息發送成功！")
    except Exception as e:
        logging.error(f"❌ 無法發送通知: {e}")