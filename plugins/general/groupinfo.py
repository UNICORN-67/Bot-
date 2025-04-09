# Group info command

from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string

lang = get_string("en")

@Client.on_message(filters.command("groupinfo") & filters.group)
async def group_info(client: Client, message: Message):
    chat = message.chat
    text = (
        f"**{lang['general']['group_info']}**\n"
        f"**ɴᴀᴍᴇ:** {chat.title}\n"
        f"**ɪᴅ:** `{chat.id}`\n"
        f"**ᴜsᴇʀɴᴀᴍᴇ:** @{chat.username if chat.username else 'ɴᴏɴᴇ'}\n"
        f"**ᴛʏᴘᴇ:** {chat.type.capitalize()}\n"
        f"**ᴍᴇᴍʙᴇʀs:** `{await client.get_chat_members_count(chat.id)}`"
    )
    await message.reply(text)