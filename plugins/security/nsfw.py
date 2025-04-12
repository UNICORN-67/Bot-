# NSFW detection module

from pyrogram import Client, filters
from pyrogram.types import Message
from nsfw.detector import detect_text_nsfw, detect_image_nsfw, detect_video_nsfw
from db.redisdb import get_toggle
from languages.get import get_string
from utils.helpers import get_user_id
from config import OWNER_ID

lang = "en"
def _(key: str) -> str:
    return get_string(lang, key)

@Client.on_message(filters.group, group=6)
async def nsfw_protection(client: Client, message: Message):
    if not await get_toggle(message.chat.id, "nsfw"):
        return

    if message.from_user and message.from_user.id in OWNER_ID:
        return

    # Text detection
    if message.text and detect_text_nsfw(message.text):
        await message.delete()
        await message.reply_text(_("nsfw_detected"))
        return

    # Image detection (photo or sticker)
    if message.photo or (message.sticker and not message.sticker.is_animated):
        try:
            is_nsfw = await detect_image_nsfw(client, message)
            if is_nsfw:
                await message.delete()
                await message.reply_text(_("nsfw_detected"))
        except Exception as e:
            print("Image NSFW detection error:", e)
        return

    # Video or animated sticker detection
    if message.video or message.animation or (message.sticker and message.sticker.is_animated):
        try:
            is_nsfw = await detect_video_nsfw(client, message)
            if is_nsfw:
                await message.delete()
                await message.reply_text(_("nsfw_detected"))
        except Exception as e:
            print("Video NSFW detection error:", e)
        return