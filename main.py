from utils import (
    config,
    DatasetType,
    write_file,
    image_to_string,
)

config.debug = True
config.dataset_type = DatasetType.BEST
# Set defaults, prefer specifying datasets explicitly per call
config.languages = ["eng", "fra", "ara"]

def main():
    images = {
        'eng_wikipedia.png': 'eng_best',
        'fra_wikipedia.png': 'fra_best',
        'ara_wikipedia.png': 'ara_best',
    }

    for source, dataset in images.items():
        text = image_to_string(f'input/{source}', dataset=dataset)
        extension = source.split('.')[-1]
        output_file = f'output/text/{source.replace(f".{extension}", ".txt")}'
        if text is None:
            print(f"❌ Failed to extract text from {source}")
            continue
        write_file(output_file, text)
        print(f"✅ Extracted text from {source}")
        print(f"Writing text to {output_file}")

if __name__ == "__main__":
    main()
