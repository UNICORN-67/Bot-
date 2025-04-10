# Group info command

from pyrogram import filters from pyrogram.types import Message from bot import app from languages.get import lang

_ = lang("en")

@app.on_message(filters.command("groupinfo") & filters.group) async def group_info(_, message: Message): chat = message.chat text = _("general.group_info").format( title=chat.title, id=chat.id, type=chat.type.name, members=chat.members_count if hasattr(chat, 'members_count') else "Unknown", username=f"@{chat.username}" if chat.username else "None" ) await message.reply_text(text)

