import platform
import psutil
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string
from utils.uptime import get_uptime
from redis.redisdb import redis

lang = get_string("en")

@Client.on_message(filters.command("stats"))
async def stats_command(client: Client, message: Message):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    os_info = f"{platform.system()} {platform.release()}"
    uptime = get_uptime()

    try:
        ping_start = time.time()
        await redis.ping()
        redis_ping = round((time.time() - ping_start) * 1000, 2)
    except:
        redis_ping = "ᴏғғʟɪɴᴇ"

    stats_text = (
        f"**{lang['general']['stats']}**\n"
        f"ᴏꜱ: {os_info}\n"
        f"ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"ᴄᴘᴜ: {cpu}%\n"
        f"ʀᴀᴍ: {ram}%\n"
        f"ʀᴇᴅɪꜱ: {redis_ping} ms"
    )
    await message.reply(stats_text)