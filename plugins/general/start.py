# Start and help command

from pyrogram import filters
from pyrogram.types import Message
from bot import app
from languages.get import lang
from utils.helpers import get_readable_time
from datetime import datetime

_ = lang("en")
START_TIME = datetime.now()

@app.on_message(filters.command("start"))
async def start_cmd(_, message: Message):
    uptime = get_readable_time((datetime.now() - START_TIME).seconds)
    user = message.from_user.first_name

    text = _(
        "general.start_full"
    ).format(
        user=user,
        uptime=uptime
    )

    await message.reply_text(text)