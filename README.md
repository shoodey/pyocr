# PyOCR

Playing around with OCR.

## Prerequisites

1. Install Tesseract OCR

## Tesseract Languages

Make sure to read up on the documentation https://tesseract-ocr.github.io/tessdoc/Data-Files.html

You can use `scripts/tessdata.sh` to download the datasets on MacOS.

```bash
./scripts/tessdata.sh
```

> [!NOTE]
> Adding custom suffixes to the datasets affects the `languages` configuration in `utils/config.py`.
