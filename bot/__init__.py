from pyrogram import Client
from bot.config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "GroupManagerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"}
)