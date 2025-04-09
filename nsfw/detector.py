from PIL import Image
import io

# Stub NSFW detection functions (replace with your real models)
def detect_text_nsfw(text: str) -> bool:
    return any(word in text.lower() for word in ["nude", "xxx", "porn"])

def detect_image_nsfw(image_bytes: bytes) -> bool:
    # Replace with real NSFW image classifier
    return False

def detect_video_nsfw(video_path: str) -> bool:
    # Placeholder for NSFW video classification
    return False