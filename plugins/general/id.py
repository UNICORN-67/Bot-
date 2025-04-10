# ID command

from pyrogram import filters from pyrogram.types import Message from bot import app from languages.get import lang

_ = lang("en")

@app.on_message(filters.command("id")) async def get_id(_, message: Message): user_id = message.from_user.id if message.from_user else "Unknown" chat_id = message.chat.id reply_id = message.reply_to_message.from_user.id if message.reply_to_message else "N/A"

text = _("general.id_info").format(
    user_id=user_id,
    chat_id=chat_id,
    reply_id=reply_id
)
await message.reply_text(text)

