# ID command

from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string
from utils.helpers import get_chat_id, mention_user, extract_user


@Client.on_message(filters.command("id"))
async def id_info(client: Client, message: Message):
    chat_id = get_chat_id(message)
    _ = get_string(chat_id)

    target_user, _ = await extract_user(message)

    user_id = target_user.id if target_user else message.from_user.id
    mention = mention_user(target_user or message.from_user)
    msg_id = message.reply_to_message.id if message.reply_to_message else message.id

    text = (
        f"**{_('id.user')}**: `{user_id}`\n"
        f"**{_('id.chat')}**: `{message.chat.id}`\n"
        f"**{_('id.message')}**: `{msg_id}`\n"
        f"**{_('id.mention')}**: {mention}"
    )

    await message.reply(text)