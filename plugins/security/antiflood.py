# Anti-flood module

from pyrogram import Client, filters
from pyrogram.types import Message
from db.redisdb import redis
from languages.get import get_string
import time

lang = get_string("en")
flood_cache = {}

@Client.on_message(filters.group)
async def check_antiflood(client: Client, message: Message):
    gid = str(message.chat.id)
    uid = message.from_user.id

    enabled = await redis.get(f"antiflood:{gid}")
    if enabled != "on":
        return

    now = time.time()
    key = f"{gid}:{uid}"
    if key in flood_cache and now - flood_cache[key] < 1.5:
        try:
            await message.delete()
        except:
            pass
    flood_cache[key] = now

@Client.on_message(filters.command("antiflood") & filters.group)
async def toggle_antiflood(client: Client, message: Message):
    gid = str(message.chat.id)
    if len(message.command) < 2:
        return await message.reply(lang["security"]["antiflood_usage"])

    cmd = message.command[1].lower()
    if cmd == "on":
        await redis.set(f"antiflood:{gid}", "on")
        await message.reply(lang["security"]["antiflood_on"])
    elif cmd == "off":
        await redis.delete(f"antiflood:{gid}")
        await message.reply(lang["security"]["antiflood_off"])