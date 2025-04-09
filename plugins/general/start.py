# Start and help command

from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string

lang = get_string("en")  # You can modify this to be dynamic per user/group

@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    text = lang["general"]["start_text"]
    await message.reply(text)
