import os
from bot.bot import app  # Import your Pyrogram app from the bot directory

# Get the port from the environment, with a default of 8080 for local testing
PORT = os.getenv("PORT", 8080)

if __name__ == "__main__":
    print(f">> Bot is starting on PORT {PORT}...")
    
    # Start the Pyrogram bot (with polling mode)
    app.run()