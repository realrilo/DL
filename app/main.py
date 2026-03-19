from fastapi import FastAPI, File, UploadFile
from app.utils import preprocess_image
from app.model_loader import load_tomato_model, load_labels
import numpy as np

app = FastAPI(title="Tomato Leaf Disease API")

# Load startup (Global)
model = load_tomato_model()
CLASS_NAMES = load_labels()

@app.get("/")
def health_check():
    return {"status": "ready", "model": "EfficientNetB0"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    input_data = preprocess_image(image_bytes)
    
    predictions = model.predict(input_data)
    idx = np.argmax(predictions[0])
    
    return {
        "filename": file.filename,
        "prediction": CLASS_NAMES[idx],
        "confidence": float(np.max(predictions[0])),
        "details": {name: float(p) for name, p in zip(CLASS_NAMES, predictions[0])}
    }