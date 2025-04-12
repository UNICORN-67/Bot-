# User info command

from pyrogram import Client, filters
from pyrogram.types import Message
from languages.get import get_string
from utils.helpers import extract_user, mention_user, get_chat_id


@Client.on_message(filters.command("userinfo"))
async def user_info(client: Client, message: Message):
    chat_id = get_chat_id(message)
    _ = get_string(chat_id)

    user, _ = await extract_user(message)
    if not user:
        return await message.reply(_("userinfo.no_user"))

    mention = mention_user(user)
    text = (
        f"**{_('userinfo.name')}**: {user.first_name or '-'}\n"
        f"**{_('userinfo.id')}**: `{user.id}`\n"
        f"**{_('userinfo.dc')}**: `{user.dc_id or 'N/A'}`\n"
        f"**{_('userinfo.mention')}**: {mention}\n"
        f"**{_('userinfo.bot')}**: `{user.is_bot}`\n"
        f"**{_('userinfo.restricted')}**: `{user.is_restricted}`\n"
        f"**{_('userinfo.language_code')}**: `{user.language_code or 'N/A'}`"
    )

    await message.reply(text)