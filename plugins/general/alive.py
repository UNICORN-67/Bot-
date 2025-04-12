# Alive command with stats
from pyrogram import Client, filters
import time
import platform
import psutil
from datetime import datetime
from utils.helpers import mention_user
from languages.get import get_string

# Load translation function
_ = get_string("en")

start_time = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4 and seconds > 0:
        remainder, result = divmod(seconds, 60) if count < 2 else divmod(seconds, 24) if count == 2 else (seconds, 0)
        time_list.append(f"{int(remainder)}{time_suffix_list[count]}")
        seconds = result
        count += 1
    return " ".join(reversed(time_list))

@Client.on_message(filters.command("alive"))
async def alive(_, message):
    current_time = time.time()
    uptime = get_readable_time(int(current_time - start_time))

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    user = mention_user(message.from_user)

    text = (
        f"{_('alive.hello').format(user=user)}\n"
        f"{_('alive.uptime')}: {uptime}\n"
        f"{_('alive.cpu')}: {cpu}%\n"
        f"{_('alive.ram')}: {ram}%\n"
        f"{_('alive.disk')}: {disk}%\n"
        f"{_('alive.python')}: {platform.python_version()}\n"
        f"{_('alive.pyrogram')}: {Client.__version__}"
    )

    await message.reply(text)