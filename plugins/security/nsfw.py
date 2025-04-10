# NSFW detection module

from pyrogram import Client, filters
from pyrogram.types import Message
from nsfw.detector import detect_nsfw
from db.redisdb import redis
from languages.get import get_string

lang = get_string("en")

@Client.on_message(filters.group & (filters.photo | filters.video | filters.sticker | filters.animation | filters.text))
async def nsfw_filter(client: Client, message: Message):
    gid = str(message.chat.id)
    enabled = await redis.get(f"nsfw:{gid}")
    if enabled != "on":
        return

    result = await detect_nsfw(message)
    if result == "NSFW":
        try:
            await message.delete()
        except:
            pass

@Client.on_message(filters.command("nsfw") & filters.group)
async def toggle_nsfw(client: Client, message: Message):
    gid = str(message.chat.id)
    if len(message.command) < 2:
        return await message.reply(lang["security"]["nsfw_usage"])

    cmd = message.command[1].lower()
    if cmd == "on":
        await redis.set(f"nsfw:{gid}", "on")
        await message.reply(lang["security"]["nsfw_on"])
    elif cmd == "off":
        await redis.delete(f"nsfw:{gid}")
        await message.reply(lang["security"]["nsfw_off"])