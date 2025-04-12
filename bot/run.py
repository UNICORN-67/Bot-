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
