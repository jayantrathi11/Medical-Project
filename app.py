# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:15:24 2020

@author: hritvik
"""


import numpy
from keras.models import load_model
import cv2
from cv2 import imread
import numpy as np
from tensorflow.keras.models import load_model
import cv2
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request, jsonify, Flask, render_template
import base64
import io
from PIL import Image
from keras.initializers import glorot_uniform

app = Flask(__name__)
       
@app.route("/")
def home():
	return render_template("home.html")










if __name__ == '__main__':
    app.run()
    
    
    
    
