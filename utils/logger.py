# Logger

from pyrogram import Client
from bot.config import LOG_CHANNEL_ID

async def log_to_channel(client: Client, text: str):
    if not LOG_CHANNEL_ID:
        return
    try:
        await client.send_message(LOG_CHANNEL_ID, text)
    except Exception as e:
        print(f"Logging failed: {e}")
