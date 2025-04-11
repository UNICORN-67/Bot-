# Logger

import logging

# Logger setup
def setup_logger(name: str = "bot", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger

# Log action to a log file or console
def log_action(action: str, user: str = "", chat: str = ""):
    logger = logging.getLogger("bot")
    logger.info(f"Action: {action} | User: {user} | Chat: {chat}")