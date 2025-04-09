import asyncio
from pyrogram import idle
from bot.bot import app  # Import the Pyrogram Client

async def main():
    print("[INFO] Starting bot...")
    await app.start()
    print("[INFO] Bot is online.")
    await idle()  # Keeps the bot running
    await app.stop()
    print("[INFO] Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())