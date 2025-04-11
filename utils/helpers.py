from pyrogram.types import Message
from pyrogram.errors import PeerIdInvalid

async def extract_user(message: Message):
    if message.reply_to_message:
        return message.reply_to_message.from_user

    if len(message.command) > 1:
        user_id = message.command[1]
        try:
            if user_id.isdigit():
                return await message._client.get_users(int(user_id))
            elif user_id.startswith("@"):  # username
                return await message._client.get_users(user_id)
        except PeerIdInvalid:
            return None
        except Exception:
            return None

    return None


def get_user_id(user):
    return user.id if hasattr(user, "id") else user


def get_username(user):
    if hasattr(user, "username") and user.username:
        return f"@{user.username}"
    return user.first_name if hasattr(user, "first_name") else str(user)


def get_mention(user):
    name = user.first_name if hasattr(user, "first_name") else str(user)
    return f"[{name}](tg://user?id={user.id})" if hasattr(user, "id") else name


def get_command_args(message: Message):
    return message.text.split()[1:] if message.text else []


def get_mention_user(message: Message):
    if message.reply_to_message:
        return get_mention(message.reply_to_message.from_user)
    if len(message.command) > 1:
        return message.command[1]
    return ""


def get_chat_id(message: Message):
    return message.chat.id if message.chat else None
