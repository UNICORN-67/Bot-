# Initializes bot, loads plugins

import asyncio
from bot import app
from utils.logger import setup_logger

# Setup logger
logger = setup_logger("Bot")

# Main run function
async def run_bot():
    logger.info("Starting bot...")
    await app.start()
    logger.info("Bot started successfully.")
    await idle()

# Pyrogram idle import
from pyrogram.idle import idle

if __name__ == "__main__":
    asyncio.run(run_bot())
