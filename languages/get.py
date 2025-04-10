import yaml
import os

def get_string(lang_code: str, key: str) -> str:
    """
    Retrieve a translated string by language code and key from the YAML file.
    Example key: "start.welcome"
    """
    try:
        path = os.path.join("languages", f"{lang_code}.yml")
        if not os.path.isfile(path):
            return "Language file not found"

        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        keys = key.split(".")
        for k in keys:
            if isinstance(data, dict):
                data = data.get(k)
            else:
                return "Invalid key path"

        return data if isinstance(data, str) else "String not found"
    except Exception as e:
        return f"Error loading string: {e}"


# Optional helper for easier access
def lang(language: str):
    def translator(key: str) -> str:
        return get_string(language, key)
    return translator