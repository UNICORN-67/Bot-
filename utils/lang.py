# Language handler

import yaml
from db.redisdb import redis

def load_yaml(lang_code: str = "en") -> dict:
    path = f"languages/{lang_code}.yml"
    try:
        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        with open("languages/en.yml", "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

async def get_lang_code(chat_id: int) -> str:
    lang = await redis.get(f"lang:{chat_id}")
    return lang if lang else "en"

async def get_string(chat_id: int) -> dict:
    lang_code = await get_lang_code(chat_id)
    return load_yaml(lang_code)