import yaml
import os

LANGUAGE_DIR = os.path.join(os.path.dirname(__file__))
FONTS_FILE = os.path.join(LANGUAGE_DIR, "fonts.yml")

_languages = {}
_fonts = {}

def load_languages():
    for filename in os.listdir(LANGUAGE_DIR):
        if filename.endswith(".yml") and filename != "fonts.yml":
            lang_code = filename.replace(".yml", "")
            with open(os.path.join(LANGUAGE_DIR, filename), "r", encoding="utf-8") as f:
                _languages[lang_code] = yaml.safe_load(f)

def load_fonts():
    if os.path.exists(FONTS_FILE):
        with open(FONTS_FILE, "r", encoding="utf-8") as f:
            global _fonts
            _fonts = yaml.safe_load(f)

def get_string(lang_code: str, key: str) -> str:
    lang = _languages.get(lang_code, {})
    return lang.get(key, key)

def get_font(style: str, text: str) -> str:
    mapping = _fonts.get(style, {})
    return "".join(mapping.get(c, c) for c in text)

# Load on module import
load_languages()
load_fonts()