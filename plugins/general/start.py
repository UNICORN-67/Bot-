# Start and help command

from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string
from config import OWNER_ID

@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    chat_id = message.chat.id
    _ = get_string(chat_id)

    if message.chat.type == "private":
        text = _(
            "start.private"
        ).format(mention=message.from_user.mention, owner=f"[Owner](tg://user?id={OWNER_ID})")

        await message.reply(text, disable_web_page_preview=True)
    else:
        await message.reply(_("start.group"))