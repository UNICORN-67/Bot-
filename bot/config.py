# Load config from .env or os.environ

import os
from dotenv import load_dotenv

# Load .env file if exists
load_dotenv()

# Telegram Bot Credentials
API_ID = int(os.getenv("API_ID", 12345))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# Redis Configuration
REDIS_URI = os.getenv("REDIS_URI", "redis://localhost:6379/0")

# Logging and Permissions
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", 0))  # set to 0 if not used
OWNER_ID = int(os.getenv("OWNER_ID", 123456789))  # Your Telegram user ID