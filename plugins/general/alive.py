# Alive command with stats
import time
import psutil
import platform
from pyrogram import Client, filters
from pyrogram.types import Message
from db.redisdb import redis
from languages.get import get_string
from utils.uptime import get_uptime

lang = get_string("en")

@Client.on_message(filters.command("alive") & filters.private)
async def alive(client: Client, message: Message):
    uptime = get_uptime()
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    os_info = platform.system() + " " + platform.release()

    # Redis ping
    try:
        ping_start = time.time()
        await redis.ping()
        redis_ping = round((time.time() - ping_start) * 1000, 2)
    except Exception:
        redis_ping = "ᴏғғʟɪɴᴇ"

    msg = (
        f"{lang['general']['alive']}\n"
        f"ᴏs: {os_info}\n"
        f"ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"ᴄᴘᴜ: {cpu}%\n"
        f"ʀᴀᴍ: {ram}%\n"
        f"ʀᴇᴅɪs: {redis_ping} ms"
    )

    await message.reply(msg)
