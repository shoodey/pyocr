#!/bin/bash

# Tesseract tessdata download script for macOS
# Downloads trained data files from tessdata, tessdata_best, and tessdata_fast repos

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "Error: This script is designed to run on macOS only."
    echo "Current OS: $OSTYPE"
    exit 1
fi

# Define languages to download
LANGS=("eng" "fra" "ara")

# Target directory (macOS homebrew default)
TESSDATA_DIR="/opt/homebrew/share/tessdata"

# Base URLs for the three repositories
TESSDATA_LEGACY_URL="https://raw.githubusercontent.com/tesseract-ocr/tessdata/main"
TESSDATA_BEST_URL="https://raw.githubusercontent.com/tesseract-ocr/tessdata_best/main"
TESSDATA_FAST_URL="https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main"

# Check if tessdata directory exists
if [ ! -d "$TESSDATA_DIR" ]; then
    echo "Error: Tessdata directory does not exist: $TESSDATA_DIR"
    echo "Please install Tesseract first (brew install tesseract)"
    exit 1
fi

download_file() {
    local url=$1
    local output_file=$2
    local display_name=$3
    
    # Check if file already exists
    if [ -f "$output_file" ]; then
        echo "⊙ Skipping $display_name (already exists)"
        return 0
    fi
    
    echo "Downloading $display_name..."
    if curl -# -L -o "$output_file" "$url"; then
        echo "✓ Successfully downloaded $display_name"
    else
        echo "✗ Failed to download $display_name"
    fi
}

# Loop through each language
for lang in "${LANGS[@]}"; do
    echo ""
    echo "======================================"
    echo "Processing language: $lang"
    echo "======================================"
    
    # Download from tessdata (legacy)
    download_file \
        "$TESSDATA_LEGACY_URL/${lang}.traineddata" \
        "$TESSDATA_DIR/${lang}_legacy.traineddata" \
        "${lang}_legacy.traineddata"
    
    # Download from tessdata_best
    download_file \
        "$TESSDATA_BEST_URL/${lang}.traineddata" \
        "$TESSDATA_DIR/${lang}_best.traineddata" \
        "${lang}_best.traineddata"
    
    # Download from tessdata_fast
    download_file \
        "$TESSDATA_FAST_URL/${lang}.traineddata" \
        "$TESSDATA_DIR/${lang}_fast.traineddata" \
        "${lang}_fast.traineddata"
done

