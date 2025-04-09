# Anti-link module

from pyrogram import Client, filters
from pyrogram.types import Message
from redis.redisdb import redis
from languages.get import get_string
import re

lang = get_string("en")

link_pattern = re.compile(r"(t\.me|telegram\.me|http[s]?://)")

@Client.on_message(filters.group & filters.text)
async def check_antilink(client: Client, message: Message):
    gid = str(message.chat.id)
    if not link_pattern.search(message.text or ""):
        return

    enabled = await redis.get(f"antilink:{gid}")
    if enabled == "on" and not message.from_user.id in [client.me.id, message.chat.id]:
        try:
            await message.delete()
        except:
            pass

@Client.on_message(filters.command("antilink") & filters.group)
async def toggle_antilink(client: Client, message: Message):
    gid = str(message.chat.id)
    if len(message.command) < 2:
        return await message.reply(lang["security"]["antilink_usage"])

    cmd = message.command[1].lower()
    if cmd == "on":
        await redis.set(f"antilink:{gid}", "on")
        await message.reply(lang["security"]["antilink_on"])
    elif cmd == "off":
        await redis.delete(f"antilink:{gid}")
        await message.reply(lang["security"]["antilink_off"])