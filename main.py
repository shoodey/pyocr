from utils import image_to_string, config

config.is_debug_enabled = True

def main():
    image_to_string('input/eng_wikipedia.png')
    image_to_string('input/fra_wikipedia.png')
    image_to_string('input/ara_wikipedia.png', 10)

if __name__ == "__main__":
    main()
