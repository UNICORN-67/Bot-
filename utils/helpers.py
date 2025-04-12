import re
from pyrogram import Client
from pyrogram.types import Message

def extract_user(message: Message):
    """
    Extract the user from a message, either from mentions, user id or username.
    """
    user = None
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif message.entities:
        for entity in message.entities:
            if entity.type == "mention":
                user = message.text[entity.offset: entity.offset + entity.length]
                break
    elif message.from_user:
        user = message.from_user
    return user

def get_user_id(message: Message):
    """
    Get the user ID from a message, either from reply or sender.
    """
    user = extract_user(message)
    if user:
        return user.id
    return None

def get_chat_id(message: Message):
    """
    Get the chat ID from a message.
    """
    return message.chat.id

def mention_user(user):
    """
    Get the user mention string for a user.
    """
    return f"[{user.first_name}](tg://user?id={user.id})" if user else None

def get_readable_time(seconds: int):
    """
    Convert seconds into a human-readable format like: "2 days, 3 hours, 45 minutes, 10 seconds".
    """
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

def is_admin(user_id: int, chat_id: int, client: Client):
    """
    Check if a user is an admin of a chat.
    """
    try:
        admins = client.get_chat_administrators(chat_id)
        return any(admin.user.id == user_id for admin in admins)
    except Exception:
        return False

def is_owner(user_id: int, owner_id: int):
    """
    Check if the user is the owner of the bot (typically defined in the config).
    """
    return user_id == owner_id

def get_chat_members_count(chat_id: int, client: Client):
    """
    Get the number of members in a chat.
    """
    chat = client.get_chat(chat_id)
    return chat.members_count if chat else 0

def get_message_text(message: Message):
    """
    Get the text of the message, properly handling entities.
    """
    if message.text:
        return message.text
    return ''

def get_command_args(message: Message):
    """
    Extract command arguments from the message (after the command).
    """
    args = message.text.split()[1:] if message.text else []
    return args

def is_nsfw_content(message: Message):
    """
    Check if the message contains NSFW content.
    (You should replace this logic with actual detection methods.)
    """
    nsfw_keywords = ["nsfw", "porn", "sex", "adult", "nude", "explicit"]
    if any(keyword in message.text.lower() for keyword in nsfw_keywords):
        return True
    return False