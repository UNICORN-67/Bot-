# User info command

from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string

lang = get_string("en")

@Client.on_message(filters.command("userinfo"))
async def user_info(client: Client, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user

    text = (
        f"**{lang['general']['user_info']}**\n"
        f"**ɴᴀᴍᴇ:** {user.first_name or '---'}\n"
        f"**ɪᴅ:** `{user.id}`\n"
        f"**ᴜsᴇʀɴᴀᴍᴇ:** @{user.username if user.username else 'ɴᴏɴᴇ'}\n"
        f"**ʟᴀɴɢᴜᴀɢᴇ:** `{user.language_code or 'ɴ/ᴀ'}`\n"
        f"**ʙᴏᴛ:** {'ʏᴇs' if user.is_bot else 'ɴᴏ'}"
    )
    await message.reply(text)
