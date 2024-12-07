# vision-ocr-extractor
This project extracts data from bill images using OCR and machine learning techniques.

## Setup
1. Clone the repo: `git@github.com:SAURABH271198/vision-ocr-extractor.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `uvicorn src.app:app --reload`

## Directory Structure

```plaintext
VISION-OCR-EXTRACTOR/
├── data/                   # Data directory
│   ├── raw/                # Raw input images
│   ├── annotated/          # Annotated training data
│   ├── train/              # Training dataset
│   ├── test/               # Test dataset
├── src/                    # Source code
│   ├── __init__.py         # Marks this as a package
│   ├── ocr/                # OCR module
│   │   ├── __init__.py
│   │   ├── tesseract.py    # Tesseract OCR logic
│   │   ├── cloud_api.py    # Cloud-based OCR logic
│   ├── ner/                # Named Entity Recognition (NER) module
│   │   ├── __init__.py
│   │   ├── model.py        # Model training and inference
│   │   ├── preprocess.py   # Data preprocessing for NER
│   ├── postprocessing.py   # Text cleaning and field mapping
│   ├── database/           # Database integration module
│   │   ├── __init__.py
│   │   ├── schema.py       # Database schema setup
│   │   ├── insert.py       # Insert data into database
│   ├── app.py              # Main application
├── tests/                  # Tests
│   ├── test_ocr.py         # Test OCR functionality
│   ├── test_ner.py         # Test NER models
│   ├── test_database.py    # Test database integration
├── models/                 # Saved models
│   ├── ner_model/          # Fine-tuned NER model
│   ├── ocr_cache/          # Cached OCR results
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore file

