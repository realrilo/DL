import tensorflow as tf
import json
import os

MODEL_PATH = "models/tomato_model_final.h5"
LABEL_PATH = "app/class_indices.json"

def load_tomato_model():
    return tf.keras.models.load_model(MODEL_PATH)

def load_labels():
    if os.path.exists(LABEL_PATH):
        with open(LABEL_PATH, 'r') as f:
            return json.load(f)
    # Fallback json belum ada
    return ["Label tidak ditemukan"]