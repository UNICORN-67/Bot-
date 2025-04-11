# All admin commands: ban, gban, warn, etc.

from pyrogram import filters
from pyrogram.types import Message
from bot.bot import app
from utils.helpers import extract_user, get_command_arg
from db.redisdb import get_toggle, set_toggle
from utils.logger import log_action
from languages.get import get_string

_ = get_string("en")

@app.on_message(filters.command("ban") & filters.group)
async def ban_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("ban_no_user"))
    try:
        await message.chat.ban_member(user.id)
        await message.reply_text(_("ban_success").format(user.mention))
        await log_action(message, f"Banned {user.mention}")
    except Exception as e:
        await message.reply_text(str(e))

@app.on_message(filters.command("unban") & filters.group)
async def unban_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("unban_no_user"))
    try:
        await message.chat.unban_member(user.id)
        await message.reply_text(_("unban_success").format(user.mention))
        await log_action(message, f"Unbanned {user.mention}")
    except Exception as e:
        await message.reply_text(str(e))

@app.on_message(filters.command("kick") & filters.group)
async def kick_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("kick_no_user"))
    try:
        await message.chat.ban_member(user.id)
        await message.chat.unban_member(user.id)
        await message.reply_text(_("kick_success").format(user.mention))
        await log_action(message, f"Kicked {user.mention}")
    except Exception as e:
        await message.reply_text(str(e))

@app.on_message(filters.command("warn") & filters.group)
async def warn_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("warn_no_user"))
    # You can integrate warnings DB logic here
    await message.reply_text(_("warn_success").format(user.mention))
    await log_action(message, f"Warned {user.mention}")

@app.on_message(filters.command("unwarn") & filters.group)
async def unwarn_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("unwarn_no_user"))
    # Remove warning from DB here
    await message.reply_text(_("unwarn_success").format(user.mention))
    await log_action(message, f"Unwarned {user.mention}")

@app.on_message(filters.command("gban") & filters.user(YOUR_OWNER_ID))
async def gban_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("gban_no_user"))
    # Add user to GBAN database here
    await message.reply_text(_("gban_success").format(user.mention))
    await log_action(message, f"Globally banned {user.mention}")

@app.on_message(filters.command("ungban") & filters.user(YOUR_OWNER_ID))
async def ungban_user(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("ungban_no_user"))
    # Remove user from GBAN database
    await message.reply_text(_("ungban_success").format(user.mention))
    await log_action(message, f"Globally unbanned {user.mention}")

@app.on_message(filters.command("gpromote") & filters.group)
async def gpromote(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("promote_no_user"))
    try:
        await message.chat.promote_member(user.id, can_manage_chat=True)
        await message.reply_text(_("promote_success").format(user.mention))
        await log_action(message, f"Promoted {user.mention}")
    except Exception as e:
        await message.reply_text(str(e))

@app.on_message(filters.command("gdemote") & filters.group)
async def gdemote(_, message: Message):
    user = await extract_user(message)
    if not user:
        return await message.reply(_("demote_no_user"))
    try:
        await message.chat.promote_member(user.id, can_manage_chat=False)
        await message.reply_text(_("demote_success").format(user.mention))
        await log_action(message, f"Demoted {user.mention}")
    except Exception as e:
        await message.reply_text(str(e))

@app.on_message(filters.command("toggle") & filters.group)
async def toggle_feature(_, message: Message):
    arg = get_command_arg(message)
    if not arg:
        return await message.reply(_("toggle_no_arg"))
    current = await get_toggle(message.chat.id, arg)
    await set_toggle(message.chat.id, arg, not current)
    await message.reply_text(_("toggle_on" if not current else "toggle_off").format(arg))
    await log_action(message, f"Toggled {arg} to {'ON' if not current else 'OFF'}")