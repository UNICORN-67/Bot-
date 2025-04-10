import yaml
import os

# Load all available language files into memory (e.g., en.yml)
LANGUAGES = {}

LANGUAGE_DIR = os.path.join(os.path.dirname(__file__))

for file in os.listdir(LANGUAGE_DIR):
    if file.endswith(".yml"):
        lang_code = file.replace(".yml", "")
        with open(os.path.join(LANGUAGE_DIR, file), "r", encoding="utf-8") as f:
            LANGUAGES[lang_code] = yaml.safe_load(f)

# Get translated string
def get_string(lang: str, key: str) -> str:
    return LANGUAGES.get(lang, LANGUAGES.get("en", {})).get(key, key)