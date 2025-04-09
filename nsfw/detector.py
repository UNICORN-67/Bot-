import re
import numpy as np
import cv2
from PIL import Image
from io import BytesIO

# Optional: Add image classification or ML model loading here
# For simplicity, basic keyword and pixel-based checks are used

NSFW_KEYWORDS = [
    "porn", "sex", "nude", "xxx", "boobs", "fuck", "naked", "bitch", "dick", "pussy", "horny"
]

def detect_text_nsfw(text: str) -> bool:
    """
    Detect NSFW in text content using keyword matching.
    """
    return any(re.search(rf"\b{word}\b", text.lower()) for word in NSFW_KEYWORDS)


def detect_image_nsfw(image_bytes: bytes) -> bool:
    """
    Detect NSFW in images (used for photos, stickers, gifs).
    Currently placeholder — replace with actual model detection if needed.
    """
    try:
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        np_img = np.array(image)

        # Placeholder: if mean pixel value is too red, mark NSFW
        r_mean = np.mean(np_img[:, :, 0])
        if r_mean > 170:
            return True
        return False
    except Exception as e:
        print(f"[Image NSFW Error] {e}")
        return False


def detect_video_nsfw(video_bytes: bytes) -> bool:
    """
    Detect NSFW in videos — process first frame only.
    """
    try:
        np_video = np.frombuffer(video_bytes, np.uint8)
        video = cv2.imdecode(np_video, cv2.IMREAD_COLOR)
        if video is not None:
            frame = video[0:1]
            r_mean = np.mean(frame[:, :, 0])
            if r_mean > 170:
                return True
        return False
    except Exception as e:
        print(f"[Video NSFW Error] {e}")
        return False