# Group info command

from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember
from languages.get import get_string
from utils.helpers import get_chat_id, mention_user


@Client.on_message(filters.command("groupinfo"))
async def group_info(client: Client, message: Message):
    chat = message.chat
    chat_id = get_chat_id(message)
    _ = get_string(chat_id)

    title = chat.title or "Private Chat"
    username = f"@{chat.username}" if chat.username else "None"
    chat_type = chat.type.capitalize()
    chat_id = chat.id
    dc_id = chat.dc_id if hasattr(chat, 'dc_id') else "Unknown"

    # Fetch chat members count
    members = await client.get_chat_members_count(chat.id)

    # Fetch admins count
    admins = await client.get_chat_members(chat.id, filter="administrators")
    admin_count = len(list(admins))

    # Fetch owner
    owner = "Not Found"
    async for member in client.get_chat_members(chat.id, filter="administrators"):
        if member.status == "owner":
            owner = mention_user(member.user)
            break

    info_text = (
        f"**{_('groupinfo.title')}**: {title}\n"
        f"**{_('groupinfo.username')}**: {username}\n"
        f"**{_('groupinfo.id')}**: `{chat_id}`\n"
        f"**{_('groupinfo.dc')}**: `{dc_id}`\n"
        f"**{_('groupinfo.type')}**: {chat_type}\n"
        f"**{_('groupinfo.members')}**: {members}\n"
        f"**{_('groupinfo.admins')}**: {admin_count}\n"
        f"**{_('groupinfo.owner')}**: {owner}"
    )

    await message.reply(info_text)