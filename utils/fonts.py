# Font converter

import yaml

with open("languages/font.yml", "r", encoding="utf-8") as f:
    font_data = yaml.safe_load(f)

def stylize(text: str, style: str = "smallcaps") -> str:
    if style not in font_data:
        return text  # Fallback

    mapping = font_data[style]
    styled_text = ""
    for char in text:
        styled_text += mapping.get(char, char)
    return styled_text