# Load config from .env or os.environ

import os
from dotenv import load_dotenv

# Load .env file if exists
load_dotenv()

# Telegram Bot Credentials
API_ID = int(os.getenv("API_ID", 9683694))
API_HASH = os.getenv("API_HASH", "c426d9f7087744afdafc961a620b6338")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8146545438:AAFoq4cmKkhnkNAz9x65-8F_HxeeSy-hWBA")

# Redis Configuration
REDIS_URI = os.getenv("REDIS_URI", "redis-cli -u redis://default:pR2c50esNfwPGODo0gn7Zvokbxwdg0t1@redis-17260.c73.us-east-1-2.ec2.redns.redis-cloud.com:17260")

# Logging and Permissions
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", -1002621770250))  # set to 0 if not used
OWNER_ID = int(os.getenv("OWNER_ID", 7661577681))  # Your Telegram user ID