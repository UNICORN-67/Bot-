# Anti-flood module

from pyrogram import Client, filters
from pyrogram.types import Message
import time

from db.redisdb import redis, get_toggle
from utils.helpers import is_admin, get_user_id, get_chat_id
from languages.get import get_string

FLOOD_LIMIT = 5  # Max messages
FLOOD_TIME = 10  # Seconds window
MUTE_DURATION = 60  # Not used here, but you can implement it

@Client.on_message(filters.group & filters.text)
async def antiflood_handler(client: Client, message: Message):
    chat_id = get_chat_id(message)
    user_id = get_user_id(message)

    if not user_id or await is_admin(client, message):
        return

    # Check toggle status
    if not await get_toggle(chat_id, "antiflood"):
        return

    key = f"flood:{chat_id}:{user_id}"

    try:
        user_data = await redis.get(key)
        now = int(time.time())

        if user_data:
            count, last_time = map(int, user_data.decode().split(":"))
            if now - last_time < FLOOD_TIME:
                count += 1
            else:
                count = 1

            if count >= FLOOD_LIMIT:
                await redis.delete(key)
                try:
                    await client.restrict_chat_member(
                        chat_id,
                        user_id,
                        permissions=client.chat_restrict_permissions()
                    )
                    await message.reply_text(
                        get_string("en", "antiflood_muted").format(user_id=user_id)
                    )
                except Exception as e:
                    print(f"Restrict Error: {e}")
                return
        else:
            count = 1

        await redis.setex(key, FLOOD_TIME, f"{count}:{now}")

    except Exception as e:
        print(f"[AntiFlood Error] {e}")
