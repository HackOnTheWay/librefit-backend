from flask import request, jsonify

import tensorflow.compat.v2 as tf
import tensorflow_hub as hub

m = hub.KerasLayer('https://tfhub.dev/google/aiy/vision/classifier/food_V1/1')
from app import app

import numpy as np
import cv2
from skimage import io
import pandas as pd

input_shape = (224, 224)
labelmap_url = "https://www.gstatic.com/aihub/tfhub/labelmaps/aiy_food_V1_labelmap.csv"


@app.route('/api/predict', methods=['POST'])
def predict():

    data = request.files['ip_img']
    print(data)
    if data is None:
        return jsonify({'msg': 'No data received'}), 401
    image = np.asarray(io.imread(data), dtype="float")
    image = cv2.resize(image, dsize=input_shape, interpolation=cv2.INTER_CUBIC)
    # img = Image.open(file.stream)
    # Scale values to [0, 1].
    image = image / image.max()
    # The model expects an input of (?, 224, 224, 3).
    images = np.expand_dims(image, 0)
    # This assumes you're using TF2.
    output = m(images)
    predicted_index = output.numpy().argmax()
    classes = list(pd.read_csv(labelmap_url)["name"])
    return jsonify(classes[predicted_index])