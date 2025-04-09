from pyrogram.types import User


def mention_user(user: User) -> str:
    """Mention a user with markdown link."""
    return f"[{user.first_name}](tg://user?id={user.id})"


def get_user_id(message):
    """Get user ID from reply or command argument."""
    if message.reply_to_message:
        return message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        if message.command[1].isdigit():
            return int(message.command[1])
    return None


def get_chat_id(message):
    """Get chat ID from message."""
    return message.chat.id if message.chat else None


def get_command_arg(message):
    """Get text argument after command."""
    return message.text.split(None, 1)[1] if len(message.command) > 1 else None