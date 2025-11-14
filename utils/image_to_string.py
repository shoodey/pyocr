import arabic_reshaper
import pytesseract
from PIL import Image
from bidi.algorithm import get_display

from .config import config

def image_to_string(image_path: str, dataset: str | None = None, timeout: int | None = None) -> str | None:
    if dataset is None:
        dataset = config.datasets
    if timeout is None:
        timeout = config.timeout
    
    try:
        image = Image.open(image_path) # Is this really needed? Tesseract can accept a file path directly
        text = pytesseract.image_to_string(image, lang=dataset, timeout=timeout).strip()
        debug_image_to_string(image_path, text)
        return text
    except FileNotFoundError:
        print(f"❌ Image file not found at {image_path}")
        return None
    except pytesseract.TesseractNotFoundError:
        print("❌ Tesseract is not installed")
        return None
    except TimeoutError:
        print(f"❌ Timeout after {timeout} seconds")
        return None
    except Exception as e:
        print(f"❌ {e}")
        return None


def debug_image_to_string(image_path: str, text: str):
    if not config.debug: return

    header = f"Processing {image_path}"
    divider = f"{'='*len(header)}"
    print(divider)
    print(header)
    print(divider)
    
    formatted_text = format_rtl_text(text)
    print(f"\n{formatted_text}\n")


def format_rtl_text(text: str) -> str:
    """
    Detects and formats right-to-left text (Arabic, Hebrew, etc.) for proper terminal display.
    Uses arabic-reshaper and python-bidi for proper bidirectional text handling.
    """
    has_arabic = any('\u0600' <= char <= '\u06FF' or '\u0750' <= char <= '\u077F' or '\u08A0' <= char <= '\u08FF' for char in text)
    has_hebrew = any('\u0590' <= char <= '\u05FF' for char in text)
    
    if has_arabic:
        # Reshape Arabic text (connects letters properly)
        reshaped_text = arabic_reshaper.reshape(text)
        # Apply bidirectional algorithm for RTL display
        return get_display(reshaped_text)
    elif has_hebrew:
        # Hebrew doesn't need reshaping, just bidi algorithm
        return get_display(text)
    
    return text

