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
from http.server import BaseHTTPRequestHandler, HTTPServer

class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def keep_alive():
    port = int(os.environ.get("PORT", 10000))  # Render provides PORT env var
    server = HTTPServer(("0.0.0.0", port), KeepAliveHandler)
    print(f"Keep-alive server running on port {port}")
    server.serve_forever()

# Run bot and keep-alive server
if __name__ == "__main__":
    import threading
    t = threading.Thread(target=keep_alive)
    t.start()
    app.run()  # Your Pyrogram Client