from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus


async def extract_user(message: Message):
    """Extract user from a command message or reply."""
    user_id = None
    reason = None

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif message.command and len(message.command) > 1:
        user_id = message.command[1]
        if user_id.startswith("@"):
            user_id = user_id[1:]
        if len(message.command) > 2:
            reason = " ".join(message.command[2:])
    return int(user_id) if user_id and str(user_id).isdigit() else user_id, reason


def get_command_arg(message: Message) -> str:
    """Return argument after command."""
    if message.text:
        parts = message.text.split(maxsplit=1)
        return parts[1] if len(parts) > 1 else ""
    return ""


def get_chat_id(message: Message) -> int:
    """Returns chat ID from message."""
    return message.chat.id


async def mention_user(message: Message):
    """Return a mention string for a user in reply or via text_mention."""
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        return user.mention if user else None
    elif message.entities:
        for entity in message.entities:
            if entity.type == "text_mention":
                return entity.user.mention
    return None


def get_user_id(message: Message) -> int | None:
    """Get the user ID from message if available."""
    if message.reply_to_message:
        return message.reply_to_message.from_user.id
    elif message.from_user:
        return message.from_user.id
    return None


def get_chat_type(message: Message) -> str:
    """Return type of chat: private, group, supergroup, or channel."""
    return message.chat.type.name if hasattr(message.chat, "type") else "unknown"


async def is_admin(client, chat_id: int, user_id: int) -> bool:
    """Check if user is admin in a chat."""
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    except:
        return False


async def is_owner(client, chat_id: int, user_id: int) -> bool:
    """Check if user is the group owner."""
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status == ChatMemberStatus.OWNER
    except:
        return False