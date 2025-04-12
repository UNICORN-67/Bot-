# NSFW detection module

from pyrogram import Client, filters
from pyrogram.types import Message
from nsfw.detector import detect_text_nsfw, detect_media_nsfw
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

    media = message.photo or message.video or message.animation or message.sticker
    if media:
        try:
            is_nsfw = await detect_media_nsfw(client, message)
        except Exception:
            return
        if is_nsfw:
            await message.delete()
            await message.reply_text(_("nsfw_detected"))
        return

    if message.text and detect_text_nsfw(message.text):
        await message.delete()
        await message.reply_text(_("nsfw_detected"))