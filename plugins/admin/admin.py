# All admin commands: ban, gban, warn, etc.

from pyrogram import Client, filters
from pyrogram.types import Message
from db.redisdb import redis
from bot.config import OWNER_ID
from languages.get import get_string

# Load localized text
lang = get_string("en")

def is_admin():
    return filters.group & filters.user(OWNER_ID)

@Client.on_message(filters.command("ban") & is_admin())
async def ban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    user_id = message.reply_to_message.from_user.id
    await client.kick_chat_member(message.chat.id, user_id)
    await message.reply(lang["admin"]["ban"])

@Client.on_message(filters.command("unban") & is_admin())
async def unban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    user_id = message.reply_to_message.from_user.id
    await client.unban_chat_member(message.chat.id, user_id)
    await message.reply(lang["admin"]["unban"])

@Client.on_message(filters.command("kick") & is_admin())
async def kick_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    user_id = message.reply_to_message.from_user.id
    await client.ban_chat_member(message.chat.id, user_id)
    await client.unban_chat_member(message.chat.id, user_id)
    await message.reply(lang["admin"]["kick"])

@Client.on_message(filters.command("gban") & is_admin())
async def gban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    user_id = message.reply_to_message.from_user.id
    await redis.set(f"gban:{user_id}", "true")
    await message.reply(lang["admin"]["gban"])

@Client.on_message(filters.command("ungban") & is_admin())
async def ungban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    user_id = message.reply_to_message.from_user.id
    await redis.delete(f"gban:{user_id}")
    await message.reply(lang["admin"]["ungban"])

@Client.on_message(filters.command("gpromote") & is_admin())
async def gpromote(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    await client.promote_chat_member(
        message.chat.id,
        message.reply_to_message.from_user.id,
        can_change_info=True,
        can_delete_messages=True,
        can_invite_users=True,
        can_restrict_members=True,
        can_pin_messages=True,
        can_promote_members=False,
    )
    await message.reply(lang["admin"]["promote"])

@Client.on_message(filters.command("gdemote") & is_admin())
async def gdemote(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    await client.promote_chat_member(
        message.chat.id,
        message.reply_to_message.from_user.id,
        can_change_info=False,
        can_delete_messages=False,
        can_invite_users=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
    )
    await message.reply(lang["admin"]["demote"])

@Client.on_message(filters.command("warn") & is_admin())
async def warn_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    warn_key = f"warn:{chat_id}:{user_id}"
    warns = int(await redis.get(warn_key) or 0) + 1
    await redis.set(warn_key, warns)
    await message.reply(f"{lang['admin']['warn']} ({warns}/3)")
    if warns >= 3:
        await client.kick_chat_member(chat_id, user_id)
        await redis.delete(warn_key)

@Client.on_message(filters.command("unwarn") & is_admin())
async def unwarn_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply(lang["admin"]["user_not_found"])
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    await redis.delete(f"warn:{chat_id}:{user_id}")
    await message.reply(lang["admin"]["unwarn"])