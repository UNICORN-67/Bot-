# Start and help command

from pyrogram import filters from pyrogram.types import Message from bot import app from languages.get import lang

_ = lang("en")

@app.on_message(filters.command("start")) async def start_cmd(, message: Message): await message.reply_text(("general.start"))

