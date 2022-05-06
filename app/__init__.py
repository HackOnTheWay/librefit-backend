from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

from flask_jwt_extended import JWTManager

import tensorflow.compat.v2 as tf
import tensorflow_hub as hub

m = hub.KerasLayer('https://tfhub.dev/google/aiy/vision/classifier/food_V1/1')

import numpy as np
import pandas as pd
import cv2
from skimage import io

#app config
app = Flask(__name__)

app.config.from_object(Config)

#database config
db = SQLAlchemy(app)

#jwt object
# jwt = JWTManager(app)
    
from app.auth import routes
from app.workout import routes
from app.awards import routes
from app.predict import routes