# Anti-link module

import re from pyrogram import filters from pyrogram.types import Message from bot import app from languages.get import lang from db.redisdb import get_toggle

_ = lang("en")

LINK_REGEX = re.compile(r"https?://t.me/[\w]+|@\w+|t.me/[\w]+", re.IGNORECASE)

@app.on_message(filters.group & filters.text) async def check_antilink(_, message: Message): chat_id = message.chat.id

if not await get_toggle(chat_id, "antilink"):
    return

if message.entities:
    if any(entity.type in ["url", "text_link"] for entity in message.entities):
        await delete_and_warn(message)
        return

if LINK_REGEX.search(message.text):
    await delete_and_warn(message)

async def delete_and_warn(message: Message): try: await message.delete() await message.reply_text(_("security.antilink_triggered")) except Exception: pass

