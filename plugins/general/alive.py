# Alive command with stats
import platform
import psutil
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from bot import app, START_TIME
from languages.get import lang
from utils.helpers import get_readable_time

_ = lang("en")

@app.on_message(filters.command("alive"))
async def alive(_, message: Message):
    uptime = get_readable_time((datetime.now() - START_TIME).seconds)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    platform_info = platform.system() + " " + platform.release()
    python_version = platform.python_version()

    text = _(
        "general.alive_full"
    ).format(
        uptime=uptime,
        cpu=cpu_usage,
        ram=ram_usage,
        platform=platform_info,
        python=python_version
    )

    await message.reply_text(text)