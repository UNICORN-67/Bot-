import asyncio
from bot.bot import app
from pyrogram import idle
from utils.logger import log_action

async def main():
    print(">> Bot is starting...")
    await app.start()
    log_action("Bot started successfully.")
    print(">> Bot is now running...")
    await idle()
    await app.stop()
    print(">> Bot stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(">> Bot shutdown manually.")