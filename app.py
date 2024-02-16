from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.densenet import preprocess_input, decode_predictions
import cv2
import numpy as np

app = Flask(__name__)

# Load your saved DenseNet201 model
#model_path = 'C:/Users/ocapo/Desktop/CellSentry/saved_model/densenet201.h5'
#model = load_model(model_path)

@app.route('/')
def index():
    return render_template('index.html')

