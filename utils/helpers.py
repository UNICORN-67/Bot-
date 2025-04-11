pyrogram import filters
from pyrogram.types import Message
from bot import app
from utils.helpers import extract_user
from utils.logger import log_action
from db.redisdb import is_toggle_enabled
from languages.get import get_string

lang_key = "en"

@app.on_message(filters.command(["ban", "unban", "kick", "warn", "unwarn", "gban", "ungban", "gpromote", "gdemote"]))
async def admin_commands(client, message: Message):
    if not message.reply_to_message:
        await message.reply(get_string(lang_key, "reply_user"))
        return

    user = await extract_user(message)
    if not user:
        await message.reply(get_string(lang_key, "user_not_found"))
        return

    cmd = message.command[0].lower()
    chat_id = message.chat.id

    if cmd == "ban":
        await app.ban_chat_member(chat_id, user.id)
        await message.reply(get_string(lang_key, "banned"))
        await log_action("ban", chat_id, user.id)

    elif cmd == "unban":
        await app.unban_chat_member(chat_id, user.id)
        await message.reply(get_string(lang_key, "unbanned"))
        await log_action("unban", chat_id, user.id)

    elif cmd == "kick":
        await app.ban_chat_member(chat_id, user.id)
        await app.unban_chat_member(chat_id, user.id)
        await message.reply(get_string(lang_key, "kicked"))
        await log_action("kick", chat_id, user.id)

    elif cmd == "warn":
        await message.reply(get_string(lang_key, "warned"))
        await log_action("warn", chat_id, user.id)

    elif cmd == "unwarn":
        await message.reply(get_string(lang_key, "unwarned"))
        await log_action("unwarn", chat_id, user.id)

    elif cmd == "gban":
        await message.reply(get_string(lang_key, "gbanned"))
        await log_action("gban", chat_id, user.id)

    elif cmd == "ungban":
        await message.reply(get_string(lang_key, "ungbanned"))
        await log_action("ungban", chat_id, user.id)

    elif cmd == "gpromote":
        await app.promote_chat_member(
            chat_id, user.id,
            can_change_info=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=False,
        )
        await message.reply(get_string(lang_key, "promoted"))
        await log_action("gpromote", chat_id, user.id)

    elif cmd == "gdemote":
        await app.promote_chat_member(
            chat_id, user.id,
            can_change_info=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
        )
        await message.reply(get_string(lang_key, "demoted"))
        await log_action("gdemote", chat_id, user.id)


