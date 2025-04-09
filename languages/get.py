import yaml
from pathlib import Path

LANGUAGE_DIR = Path(__file__).parent
LOADED_LANGS = {}

def get_lang(lang_code="en"):
    lang_file = LANGUAGE_DIR / f"{lang_code.lower()}.yml"
    if lang_file.exists():
        if lang_code not in LOADED_LANGS:
            with open(lang_file, "r", encoding="utf-8") as file:
                LOADED_LANGS[lang_code] = yaml.safe_load(file)
        return LOADED_LANGS[lang_code]
    else:
        raise FileNotFoundError(f"Language file not found: {lang_file}")