# Anti-flood module

from pyrogram import filters from pyrogram.types import Message from bot import app from languages.get import lang from db.redisdb import get_toggle

_ = lang("en")

@app.on_message(filters.group) async def check_flood(_, message: Message): chat_id = message.chat.id user_id = message.from_user.id if message.from_user else None

if not user_id:
    return

if not await get_toggle(chat_id, "antiflood"):
    return

# Simplified anti-flood logic (example):
if not hasattr(app, "flood_control"):
    app.flood_control = {}

key = f"{chat_id}:{user_id}"
now = message.date.timestamp()

if key in app.flood_control:
    last_time = app.flood_control[key]
    if now - last_time < 1.5:
        try:
            await message.delete()
            await app.restrict_chat_member(chat_id, user_id, permissions={})
            await message.reply_text(_("security.antiflood_triggered"))
        except Exception:
            pass
app.flood_control[key] = now

