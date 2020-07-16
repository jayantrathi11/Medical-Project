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
	return render_template("predict.html")

 
@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded)) 
    # Convert RGB to BGR 
    data = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    data = cv2.resize(data,(250,250))
    data = numpy.array(data)
    data=data.reshape(-1,250,250,3)
    
    model=load_model('chestxray.h5')
    predict=model.predict_classes(data)[0][0]
    
    if predict==0:
        response = "NORMAL"
    else:
        response = "PNEUMONIA"
        
    print(response)
    return jsonify(response)
    

@app.route("/predictmalaria", methods=["POST"])
def predictmalaria():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded)) 
    # Convert RGB to BGR 
    data = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    data = cv2.resize(data,(100,100))
    data = numpy.array(data)
    data=data.reshape(-1,100,100,3)
    data = data/255.0
    model=load_model("malaria_model.h5")
    s=model.predict_proba(data)
    p=model.predict_classes(data)

    if p==0:
        response = "The cell is infected"
    else :
        response = "The cell is not infected"
        
    print(response)
    return jsonify(response)







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
    
    
    