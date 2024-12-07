from fastapi import FastAPI
# from src.ocr.tesseract import extract_text
# from src.ner.model import load_ner_model, extract_entities

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Bill Data Extractor!"}

# @app.post("/process/")
# def process_bill(image_path: str):
#     text = extract_text(image_path)
#     model = load_ner_model()
#     entities = extract_entities(text, model)
#     return {"entities": entities}
