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
from keras.models import load_model
import cv2
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request, jsonify, Flask
import base64
import io
from PIL import Image
 
app = Flask(__name__)
       


 
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
    

if __name__ == '__main__':
    app.run()
    
    
    
    