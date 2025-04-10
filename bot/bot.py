# Initializes bot, loads plugins

from pyrogram import Client
from bot.config import API_ID, API_HASH, BOT_TOKEN
from utils.logger import setup_logger
from db.redisdb import redis  # Optional: If you want to test Redis connection

log = setup_logger("bot")

# Initialize Pyrogram Client
app = Client(
    "tg_group_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"},  # Automatically loads all plugin .py files
    workers=20,
    in_memory=True
)

# Optional: Check Redis connection at startup
try:
    redis.ping()
    log.info("✅ Connected to Redis.")
except Exception as e:
    log.warning(f"❌ Redis not connected: {e}")
