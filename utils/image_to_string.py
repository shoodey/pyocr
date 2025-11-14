import pytesseract
from PIL import Image
from . import config

def image_to_string(image_path: str, timeout: int = 3) -> str | None:
    try:
        image = Image.open(image_path) # Is this really needed? Tesseract can accept a file path directly
        text = pytesseract.image_to_string(image, timeout=timeout).strip()
        debug_image_to_string(image_path, text)
        return text
    except FileNotFoundError:
        print(f"❌ Image file not found at {image_path}")
    except pytesseract.TesseractNotFoundError:
        print("❌ Tesseract is not installed")
    except TimeoutError:
        print(f"❌ Timeout after {timeout} seconds")
    except Exception as e:
        print(f"❌ {e}")
    finally:
        return None


def debug_image_to_string(image_path: str, text: str):
    if not config.is_debug_enabled: return

    header = f"Processing {image_path}"
    divider = f"{'='*len(header)}"
    print(divider)
    print(header)
    print(divider)
    print(f"\n{text}\n")

