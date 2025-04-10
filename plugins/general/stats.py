import platform import psutil from datetime import datetime from pyrogram import filters from pyrogram.types import Message from bot import app, START_TIME from languages.get import lang from utils.helpers import get_readable_time

_ = lang("en")

@app.on_message(filters.command("stats")) async def stats_cmd(_, message: Message): uptime = get_readable_time((datetime.now() - START_TIME).seconds) cpu = psutil.cpu_percent() ram = psutil.virtual_memory().percent disk = psutil.disk_usage("/").percent platform_info = platform.system() + " " + platform.release()

text = _("general.stats_full").format(
    uptime=uptime,
    cpu=cpu,
    ram=ram,
    disk=disk,
    platform=platform_info
)

await message.reply_text(text)

