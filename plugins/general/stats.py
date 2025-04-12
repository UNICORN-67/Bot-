import platform
import psutil
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string
from utils.helpers import get_readable_time

START_TIME = time.time()


@Client.on_message(filters.command("stats"))
async def stats(client: Client, message: Message):
    chat_id = message.chat.id
    _ = get_string(chat_id)

    uptime = get_readable_time(time.time() - START_TIME)
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    total_users = len(await client.get_users())
    total_chats = len(await client.get_dialogs())

    text = (
        f"**{_('stats.bot_stats')}**\n"
        f"**{_('stats.uptime')}**: `{uptime}`\n"
        f"**{_('stats.cpu')}**: `{cpu}%`\n"
        f"**{_('stats.ram')}**: `{ram}%`\n"
        f"**{_('stats.total_users')}**: `{total_users}`\n"
        f"**{_('stats.total_chats')}**: `{total_chats}`\n"
        f"**{_('stats.python')}**: `{platform.python_version()}`\n"
        f"**{_('stats.platform')}**: `{platform.system()} {platform.release()}`"
    )

    await message.reply(text)

