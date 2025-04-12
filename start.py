import asyncio
from bot.bot import app  # Your Pyrogram Client
from utils.plugin_loader import load_plugins
from utils.logger import setup_logger

logger = setup_logger("start")

async def start_bot():
    logger.info("Starting the bot...")
    await app.start()
    load_plugins("plugins")  # Ensure this path is correct
    logger.info("Bot is now running.")
    await app.idle()

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")