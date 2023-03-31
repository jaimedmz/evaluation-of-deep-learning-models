from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import cv2 
import functions
from skimage.io import imread
from flask import jsonify

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
import keras.utils as image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# django
from django.shortcuts import render 
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

app = Flask(__name__)

#MODEL_PATH = 'Color__Model1_GTSRB.h5'

Color__Model1_GTSRB = load_model('Models Color GTSRB/Color__Model1_GTSRB.h5')
Color__Model2_GTSRB = load_model('Models Color GTSRB/Color__Model2_GTSRB.h5')
Color__Model3_GTSRB = load_model('Models Color GTSRB/Color__Model3_GTSRB.h5')
Color__Model4_GTSRB = load_model('Models Color GTSRB/Color__Model4_GTSRB.h5')
Grayscale_Model1_GTSRB = load_model('Models Grayscale GTSRB/Grayscale_Model1_GTSRB.h5')
Grayscale_Model2_GTSRB = load_model('Models Grayscale GTSRB/Grayscale_Model2_GTSRB.h5')
Grayscale_Model3_GTSRB = load_model('Models Grayscale GTSRB/Grayscale_Model3_GTSRB.h5')
Grayscale_Model4_GTSRB = load_model('Models Grayscale GTSRB/Grayscale_Model4_GTSRB.h5')


def read_image_grayscale(filename):
        img = cv2.imread(filename)
        resized = cv2.resize(img, (28, 28))
        image = cv2.cvtColor(resized, cv2.IMREAD_GRAYSCALE)
        return(image.reshape(-1,28,28,1))
         

def read_image(filename):
 
        img = cv2.imread(filename)
        resized = cv2.resize(img, (28, 28))
        rgb_image = cv2.cvtColor(resized, cv2.COLOR_RGB2BGR)
        return(rgb_image.reshape(-1,28,28,3))
          

ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/testModel', methods=['GET'])
def testModel():
    return render_template('testModel.html')

@app.route('/evaluatedModel', methods=['GET', 'POST'])
def evaluatedModel():
    return render_template('evaluatedModel.html')

@app.route('/acercaDe', methods=['GET', 'POST'])
def acercaDe():
    return render_template('acercaDe.html')

@app.route('/pruebas', methods=['GET', 'POST'])
def pruebas():
    return render_template('pruebas.html')

@app.route('/uploadCmodel', methods=['GET', 'POST'])
def uploadCmodel():
    if request.method == 'POST':
        files = request.files.getlist('files[]', None)
        i=0
        j=0
        k=0
        l=0
        for f in files:
          print (f) 
          if f and allowed_file(f.filename):
            filename = f.filename
            file_path = os.path.join('uploads', filename)
            f.save(file_path)
            img = read_image(file_path)

            class_prediction=Color__Model1_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            class_str = str(classes_x)[1:-1]
            result = class_str    

            class_prediction2=Color__Model2_GTSRB.predict(img) 
            classes_x2=np.argmax(class_prediction2,axis=1)
            class_str2 = str(classes_x2)[1:-1]
            result2 = class_str2 
            
            class_prediction3=Color__Model3_GTSRB.predict(img) 
            classes_x3=np.argmax(class_prediction3,axis=1)
            class_str3 = str(classes_x3)[1:-1]
            result3 = class_str3

            class_prediction4=Color__Model4_GTSRB.predict(img) 
            classes_x4=np.argmax(class_prediction4,axis=1)
            class_str4 = str(classes_x4)[1:-1]
            result4 = class_str4 

          print(result)
          filee= (functions.findExpectedClass('Test/'+ f.filename))
          if result == filee:
            i = i+1
          if result2 == filee:
            j = j+1
          if result3 == filee:
            k = k+1
          if result4 == filee:
            l = l+1
        precision = str((i/(len(files)))*100)
        precision2 = str((j/(len(files)))*100)
        precision3 = str((k/(len(files)))*100)
        precision4 = str((l/(len(files)))*100)
        split= functions.truncate(precision, 2)
        split2= functions.truncate(precision2, 2)   
        split3= functions.truncate(precision3, 2) 
        split4= functions.truncate(precision4, 2) 
        print('Porcentaje de precisión= '+ str(split) +'%')
        print(filee)
        print('Aciertos: '+str(i))
        print('Imágenes: '+str(len(files)))

        cadena = "Porcentaje de precisión Color__Model1_GTSRB= "+str(split)+"% \nPorcentaje de precisión Color__Model2_GTSRB= "+str(split2)+"%\nPorcentaje de precisión Color__Model3_GTSRB= "+str(split3)+"%\nPorcentaje de precisión Color__Model4_GTSRB= "+str(split4)+"%"
        result = cadena
        return result
    else:
        return result

@app.route('/uploadGSmodel', methods=['GET', 'POST'])
def uploadGSmodel():
    if request.method == 'POST':
        files = request.files.getlist('files[]', None)
        i=0
        j=0
        k=0
        l=0
        for f in files:
          print (f) 
          if f and allowed_file(f.filename):
            filename = f.filename
            file_path = os.path.join('uploads', filename)
            f.save(file_path)
            img = read_image_grayscale(file_path)

            class_prediction=Grayscale_Model1_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction)
            class_str = str(classes_x)[1:-1]
            result = class_str     

            class_prediction2=Grayscale_Model2_GTSRB.predict(img) 
            classes_x2=np.argmax(class_prediction2)
            class_str2 = str(classes_x2)[1:-1]
            result2 = class_str2
            
            class_prediction3=Grayscale_Model3_GTSRB.predict(img) 
            classes_x3=np.argmax(class_prediction3)
            class_str3 = str(classes_x3)[1:-1]
            result3 = class_str3 

            class_prediction4=Grayscale_Model4_GTSRB.predict(img) 
            classes_x4=np.argmax(class_prediction4)
            class_str4 = str(classes_x4)[1:-1]
            result4 = class_str4 

          print(result)
          filee= (functions.findExpectedClass('Test/'+ f.filename))
          if result == filee:
            i = i+1
          if result2 == filee:
            j = j+1
          if result3 == filee:
            k = k+1
          if result4 == filee:
            l = l+1
        precision = str((i/(len(files)))*100)
        precision2 = str((j/(len(files)))*100)
        precision3 = str((k/(len(files)))*100)
        precision4 = str((l/(len(files)))*100)
        split= functions.truncate(precision, 2)
        split2= functions.truncate(precision2, 2)   
        split3= functions.truncate(precision3, 2) 
        split4= functions.truncate(precision4, 2) 
        print('Porcentaje de precisión= '+ str(split) +'%')
        print(filee)
        print('Aciertos: '+str(i))
        print('Imágenes: '+str(len(files)))

        cadena = "Porcentaje de precisión Grayscale_Model1_GTSRB= "+str(split)+"% \nPorcentaje de precisión Grayscale_Model2_GTSRB= "+str(split2)+"%\nPorcentaje de precisión Grayscale_Model3_GTSRB= "+str(split3)+"%\nPorcentaje de precisión Grayscale_Model4_GTSRB= "+str(split4)+"%"
        result = cadena
        return result
    else:
        return result



@app.route('/predictColor__Model1_GTSRB', methods=['GET', 'POST'])
def uploadColor__Model1_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            img = read_image(file_path)
            class_prediction=Color__Model1_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            class_str = str(classes_x)[1:-1]
            result = class_str 
            print("Clase: "+class_str)       
        return result
    return None

@app.route('/predictColor__Model2_GTSRB', methods=['GET', 'POST'])
def uploadColor__Model2_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            img = read_image(file_path)
            class_prediction=Color__Model2_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            class_str = str(classes_x)[1:-1]
            result = class_str        
        return result
    return None

@app.route('/predictColor__Model3_GTSRB', methods=['GET', 'POST'])
def uploadColor__Model3_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            img = read_image(file_path)
            class_prediction=Color__Model3_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            class_str = str(classes_x)[1:-1]
            result = class_str        
        return result
    return None


    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            result = str(functions.findExpectedClass('Test/'+filename))
        return result      
    return result
     
@app.route('/predictColor__Model4_GTSRB', methods=['GET', 'POST'])
def uploadColor__Model4_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            img = read_image(file_path)
            class_prediction=Color__Model4_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            class_str = str(classes_x)[1:-1]
            result = class_str        
        return result
    return None

@app.route('/predictGrayscale_Model1_GTSRB', methods=['GET', 'POST'])
def uploadGrayscale_Model1_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            img = read_image_grayscale(file_path)
            class_prediction=Grayscale_Model1_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction, axis=1)
            class_str = str(classes_x)[1:-1]
            result = class_str    
            print("clase en escala de grises "+result)   
        if result =='':
            result ="Clase no encontrada"
        return result
    return None

@app.route('/predictGrayscale_Model2_GTSRB', methods=['GET', 'POST'])
def uploadGrayscale_Model2_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            img = read_image_grayscale(file_path)
            class_prediction=Grayscale_Model2_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction)
            class_str = str(classes_x)[1:-1]
            result = class_str
        if result =='':
            result ="Clase no encontrada"        
        return result
    return None

@app.route('/predictGrayscale_Model3_GTSRB', methods=['GET', 'POST'])
def uploadGrayscale_Model3_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            img = read_image_grayscale(file_path)
            class_prediction=Grayscale_Model3_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction)
            class_str = str(classes_x)[1:-1]
            result = class_str  
        if result =='':
            result ="Clase no encontrada"      
        return result
    return None

@app.route('/predictGrayscale_Model4_GTSRB', methods=['GET', 'POST'])
def uploadGrayscale_Model4_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('uploads', filename)
            file.save(file_path)
            img = read_image_grayscale(file_path)
            class_prediction=Grayscale_Model4_GTSRB.predict(img) 
            classes_x=np.argmax(class_prediction)
            class_str = str(classes_x)[1:-1]
            result = class_str 
        if result =='':
            result ="Clase no encontrada"       
        return result
    return None

@app.route('/predictExpectedModels_GTSRB', methods=['GET', 'POST'])
def getPredictExpectedModels_GTSRB():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            separator = '.'
            splitString = filename.split(separator, 1)[0]
            result = str(functions.findExpectedClass('Test/'+splitString+'.png'))
        print("file")
        print (splitString)
        return result      
    return result

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app")
    app.run(debug=True)

