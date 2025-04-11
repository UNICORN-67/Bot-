# All admin commands: ban, gban, warn, etc.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from utils.helpers import extract_user, get_command_arg, mention_user, get_chat_id
from db.redisdb import get_toggle, set_toggle
from utils.logger import log_action
from languages.get import get_string

lang_code = "en"
_ = lambda key: get_string(lang_code, key)


@app.on_message(filters.command("ban") & filters.group)
async def ban_user(_, message: Message):
    if not message.from_user:
        return
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    await message.chat.ban_member(user.id)
    await message.reply_text(_("ban_success").format(user=mention_user(user)))
    await log_action(message, f"Banned {mention_user(user)}")


@app.on_message(filters.command("unban") & filters.group)
async def unban_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    await message.chat.unban_member(user.id)
    await message.reply_text(_("unban_success").format(user=mention_user(user)))
    await log_action(message, f"Unbanned {mention_user(user)}")


@app.on_message(filters.command("kick") & filters.group)
async def kick_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    await message.chat.ban_member(user.id)
    await message.chat.unban_member(user.id)
    await message.reply_text(_("kick_success").format(user=mention_user(user)))
    await log_action(message, f"Kicked {mention_user(user)}")


@app.on_message(filters.command("gban") & filters.user(OWNER_ID))
async def gban_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    # Add gban logic here
    await message.reply_text(_("gban_success").format(user=mention_user(user)))
    await log_action(message, f"Globally Banned {mention_user(user)}")


@app.on_message(filters.command("ungban") & filters.user(OWNER_ID))
async def ungban_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    # Add ungban logic here
    await message.reply_text(_("ungban_success").format(user=mention_user(user)))
    await log_action(message, f"Globally Unbanned {mention_user(user)}")


@app.on_message(filters.command("gpromote") & filters.group)
async def promote_admin(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    await message.chat.promote_member(
        user.id,
        can_change_info=True,
        can_delete_messages=True,
        can_invite_users=True,
        can_restrict_members=True,
        can_pin_messages=True,
        can_promote_members=False,
    )
    await message.reply_text(_("promote_success").format(user=mention_user(user)))
    await log_action(message, f"Promoted {mention_user(user)}")


@app.on_message(filters.command("gdemote") & filters.group)
async def demote_admin(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    await message.chat.promote_member(user.id)
    await message.reply_text(_("demote_success").format(user=mention_user(user)))
    await log_action(message, f"Demoted {mention_user(user)}")


@app.on_message(filters.command("warn") & filters.group)
async def warn_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    # Add warning logic (e.g., count in Redis)
    await message.reply_text(_("warn_success").format(user=mention_user(user)))
    await log_action(message, f"Warned {mention_user(user)}")


@app.on_message(filters.command("unwarn") & filters.group)
async def unwarn_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_("no_user_found"))
    # Remove warning logic here
    await message.reply_text(_("unwarn_success").format(user=mention_user(user)))
    await log_action(message, f"Unwarned {mention_user(user)}")


@app.on_message(filters.command("settoggle") & filters.user(OWNER_ID))
async def set_toggle_cmd(_, message: Message):
    args = get_command_arg(message)
    if not args or "=" not in args:
        return await message.reply_text("Usage: /settoggle <key>=<value>")
    key, value = args.split("=", 1)
    await set_toggle(key.strip(), value.strip())
    await message.reply_text(f"Toggled {key.strip()} set to {value.strip()}")


@app.on_message(filters.command("gettoggle") & filters.user(OWNER_ID))
async def get_toggle_cmd(_, message: Message):
    key = get_command_arg(message)
    if not key:
        return await message.reply_text("Usage: /gettoggle <key>")
    value = await get_toggle(key.strip())
    await message.reply_text(f"{key.strip()} = {value}")