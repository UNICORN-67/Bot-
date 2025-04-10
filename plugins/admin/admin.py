# All admin commands: ban, gban, warn, etc.

from pyrogram import filters from pyrogram.types import Message from bot import app from languages.get import lang from utils.helpers import extract_user from pyrogram.enums import ChatMemberStatus

_ = lang("en")

@app.on_message(filters.command("ban") & filters.group) async def ban_user(, message: Message): user = await extract_user(message) if not user: return await message.reply_text(("admin.no_user")) await message.chat.ban_member(user.id) await message.reply_text(_("admin.banned"))

@app.on_message(filters.command("unban") & filters.group) async def unban_user(, message: Message): user = await extract_user(message) if not user: return await message.reply_text(("admin.no_user")) await message.chat.unban_member(user.id) await message.reply_text(_("admin.unbanned"))

@app.on_message(filters.command("kick") & filters.group) async def kick_user(, message: Message): user = await extract_user(message) if not user: return await message.reply_text(("admin.no_user")) await message.chat.ban_member(user.id) await message.chat.unban_member(user.id) await message.reply_text(_("admin.kicked"))

@app.on_message(filters.command("gban") & filters.group) async def gban_user(, message: Message): await message.reply_text(("admin.gban"))

@app.on_message(filters.command("ungban") & filters.group) async def ungban_user(, message: Message): await message.reply_text(("admin.ungban"))

@app.on_message(filters.command("gpromote") & filters.group) async def gpromote_user(, message: Message): user = await extract_user(message) if not user: return await message.reply_text(("admin.no_user")) await message.chat.promote_member(user.id, can_manage_chat=True, can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True) await message.reply_text(_("admin.promoted"))

@app.on_message(filters.command("gdemote") & filters.group) async def gdemote_user(, message: Message): user = await extract_user(message) if not user: return await message.reply_text(("admin.no_user")) await message.chat.promote_member(user.id, is_anonymous=False, can_manage_chat=False, can_change_info=False, can_invite_users=False, can_delete_messages=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False) await message.reply_text(_("admin.demoted"))

@app.on_message(filters.command("warn") & filters.group) async def warn_user(, message: Message): await message.reply_text(("admin.warned"))

@app.on_message(filters.command("unwarn") & filters.group) async def unwarn_user(, message: Message): await message.reply_text(("admin.unwarned"))

