# Alive command with stats
from pyrogram import Client, filters
from datetime import datetime
import time
import platform
import psutil

from utils.helpers import mention_user
from utils.lang import get_lang
from utils.logger import log_action

start_time = time.time()


def get_readable_time(seconds: int) -> str:
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    time_str = ""
    if days:
        time_str += f"{days}d "
    if hours:
        time_str += f"{hours}h "
    if minutes:
        time_str += f"{minutes}m "
    if seconds:
        time_str += f"{seconds}s"
    return time_str.strip()


@Client.on_message(filters.command("alive"))
async def alive(_, message):
    user = message.from_user
    chat_id = message.chat.id
    lang = await get_lang(chat_id)
    _ = lambda key: lang.get(key, key)

    uptime = get_readable_time(time.time() - start_time)
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    text = (
        f"{_('alive.hello').format(user=mention_user(user))}\n\n"
        f"⏱️ {_('alive.uptime')}: {uptime}\n"
        f"🖥️ {_('alive.cpu')}: {cpu}%\n"
        f"💾 {_('alive.ram')}: {ram}%\n"
        f"🗂️ {_('alive.disk')}: {disk}%\n"
        f"⚙️ {_('alive.python')}: {platform.python_version()}\n"
        f"📦 {_('alive.pyrogram')}: {Client.__version__}"
    )

    await message.reply(text)
    await log_action("alive", chat_id, user.id)