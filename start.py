import logging
from bot.bot import app  # Import your Pyrogram Client from the bot folder
from utils.logger import setup_logger  # Import custom logger setup if you have one
from config import API_ID, API_HASH, BOT_TOKEN  # Import bot credentials from config (if needed)

def start_bot():
    # Setting up the logger
    setup_logger()

    # Log the bot startup
    logging.info("Starting the bot...")

    # Log the API credentials check (useful for debugging)
    logging.debug(f"Using API_ID: {API_ID}, API_HASH: {API_HASH}")

    # Run the bot
    app.run()

if __name__ == "__main__":
    start_bot()