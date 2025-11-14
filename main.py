from utils import image_to_string, config

config.is_debug_enabled = True

def main():
    image_to_string('input/tesseract_blurb.png')

if __name__ == "__main__":
    main()
