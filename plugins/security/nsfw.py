# NSFW detection module

from pyrogram import filters from pyrogram.types import Message from bot import app from nsfw.detector import detect_text_nsfw, detect_sticker_nsfw, detect_gif_nsfw, detect_video_nsfw from languages.get import lang from db.redisdb import get_toggle

_ = lang("en")

@app.on_message(filters.group, group=5) async def nsfw_filter(_, message: Message): chat_id = message.chat.id

if not await get_toggle(chat_id, "nsfw"):
    return

try:
    # Text NSFW
    if message.text and await detect_text_nsfw(message.text):
        await message.delete()
        await message.reply_text(_("security.nsfw_text_detected"))
        return

    # Sticker NSFW
    if message.sticker:
        if await detect_sticker_nsfw(message):
            await message.delete()
            await message.reply_text(_("security.nsfw_sticker_detected"))
            return

    # GIF NSFW
    if message.animation:
        if await detect_gif_nsfw(message):
            await message.delete()
            await message.reply_text(_("security.nsfw_gif_detected"))
            return

    # Video NSFW
    if message.video:
        if await detect_video_nsfw(message):
            await message.delete()
            await message.reply_text(_("security.nsfw_video_detected"))
            return

except Exception as e:
    print(f"NSFW detection error: {e}")

