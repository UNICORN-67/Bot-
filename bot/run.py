"""
import logging
from bot.bot import app  # Import your Pyrogram Client from bot folder
from utils.logger import setup_logger  # Import logger setup if you have custom logging

def start_bot():
    # Setting up the logger
    setup_logger()

    # Logging the bot startup
    logging.info("Bot is starting...")

    # Start the bot
    app.run()

if __name__ == "__main__":
    start_bot()
"""

import os
from bot.bot import app  # Your Pyrogram client instance

PORT = os.getenv("PORT", 8080)

if __name__ == "__main__":
    print(f">> Starting bot using polling on PORT {PORT}...")
    app.run()