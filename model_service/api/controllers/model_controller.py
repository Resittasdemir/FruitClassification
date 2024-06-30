from fastapi import APIRouter, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

classes = ['acai', 'cupuacu', 'graviola', 'guarana', 'pupunha', 'tucuma']

model = load_model('model.keras')

img_width = 250
img_height = 250

model_router = APIRouter()

@model_router.post("/predict")
async def get_result(file: UploadFile = File(...)) -> dict:
    img_bytes = await file.read()
    img = Image.open(io.BytesIO(img_bytes))
    img = img.convert("RGB")  
    img = img.resize((img_width, img_height))
    img_array = np.array(img) / 255.0  

    img_array = np.expand_dims(img_array, axis=0)  
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = classes[predicted_class_index]
    confidence = float(prediction[0][predicted_class_index])

    return {"predicted_class": predicted_class, "confidence": confidence}
