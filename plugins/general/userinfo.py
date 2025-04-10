# User info command

from pyrogram import filters from pyrogram.types import Message from bot import app from languages.get import lang from utils.helpers import extract_user

_ = lang("en")

@app.on_message(filters.command("userinfo")) async def userinfo_cmd(, message: Message): user = await extract_user(message) if not user: return await message.reply_text(("general.unknown_user"))

text = _("general.userinfo").format(
    id=user.id,
    first_name=user.first_name or "N/A",
    username="@" + user.username if user.username else "N/A",
    dc_id=user.dc_id if hasattr(user, "dc_id") else "N/A",
    is_bot=user.is_bot
)
await message.reply_text(text)

