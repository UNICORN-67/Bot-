from pyrogram import filters
from pyrogram.types import Message
from nsfw.detector import detect_text_nsfw, detect_image_nsfw
from db.redisdb import is_enabled

@filters.group & filters.incoming
async def nsfw_protect(client, message: Message):
    chat_id = message.chat.id
    if not await is_enabled(chat_id, "nsfw"):
        return

    # Text-based NSFW
    if message.text and detect_text_nsfw(message.text):
        await message.delete()
        return

    # Stickers & GIFs (as documents or animations)
    if message.sticker or message.animation or message.document:
        try:
            media = await message.download(in_memory=True)
            is_nsfw = detect_image_nsfw(media.read())
            if is_nsfw:
                await message.delete()
        except Exception:
            pass

    # Video files
    if message.video:
        # Optional: download & pass to video detector
        pass