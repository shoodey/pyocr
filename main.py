from utils import image_to_string, config, DatasetType

config.debug = True
config.dataset_type = DatasetType.BEST
# Set defaults, prefer specifying datasets explicitly per call
config.languages = ["eng", "fra", "ara"]

def main():
    image_to_string('input/eng_wikipedia.png', dataset="eng_best")
    image_to_string('input/fra_wikipedia.png', dataset="fra_best")
    image_to_string('input/ara_wikipedia.png', dataset="ara_best")

if __name__ == "__main__":
    main()
