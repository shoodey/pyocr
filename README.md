# PyOCR

Playing around with OCR.

## Prerequisites

1. Install Tesseract OCR
2. Install dependencies
3. ???
4. Profit

## Tesseract Languages

Make sure to read up on the documentation https://tesseract-ocr.github.io/tessdoc/Data-Files.html

You can use `scripts/tessdata.sh` to download the datasets on MacOS.

```bash
./scripts/tessdata.sh
```

> [!NOTE]
> Adding custom suffixes to the datasets affects the `languages` configuration in `utils/config.py`.

## Installing dependencies

Recommending using [uv](https://docs.astral.sh/uv/) to install dependencies, but also manage everything Python!

```bash
uv sync
```

## Running the script

```bash
uv run main.py
```
