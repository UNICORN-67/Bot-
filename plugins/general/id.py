# ID command

from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string

lang = get_string("en")

@Client.on_message(filters.command("id"))
async def id_command(client: Client, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        reply_text = (
            f"**{lang['general']['id_info']}**\n"
            f"ᴜꜱᴇʀ ɪᴅ: `{user.id}`\n"
            f"ᴄʜᴀᴛ ɪᴅ: `{message.chat.id}`\n"
            f"ᴍꜱɢ ɪᴅ: `{message.reply_to_message.id}`"
        )
    else:
        reply_text = (
            f"**{lang['general']['id_info']}**\n"
            f"ʏᴏᴜʀ ɪᴅ: `{message.from_user.id}`\n"
            f"ᴄʜᴀᴛ ɪᴅ: `{message.chat.id}`\n"
            f"ᴍꜱɢ ɪᴅ: `{message.id}`"
        )
    await message.reply(reply_text)