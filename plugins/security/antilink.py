# Anti-link module

from pyrogram import Client, filters
from pyrogram.types import Message
import re

from db.redisdb import get_toggle
from utils.helpers import is_admin, get_chat_id
from languages.get import get_string

LINK_PATTERN = re.compile(r"(https?://\S+|t\.me/\S+|telegram\.me/\S+)", re.IGNORECASE)

@Client.on_message(filters.group & filters.text )
async def antilink_handler(client: Client, message: Message):
    chat_id = get_chat_id(message)

    # Don't act if user is admin or the feature is off
    if await is_admin(client, message):
        return

    if not await get_toggle(chat_id, "antilink"):
        return

    # If any link is detected
    if LINK_PATTERN.search(message.text):
        try:
            await message.delete()
            await message.reply_text(
                get_string("en", "antilink_detected").format(user_id=message.from_user.id)
            )
        except Exception as e:
            print(f"[AntiLink Error] {e}")