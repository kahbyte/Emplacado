import numpy as np
import os
import cv2
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import requests


class Model: 
    classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)', 
            2:'Speed limit (50km/h)', 
            3:'Speed limit (60km/h)', 
            4:'Speed limit (70km/h)', 
            5:'Speed limit (80km/h)', 
            6:'End of speed limit (80km/h)', 
            7:'Speed limit (100km/h)', 
            8:'Speed limit (120km/h)', 
            9:'No passing', 
            10:'No passing veh over 3.5 tons', 
            11:'Right-of-way at intersection', 
            12:'Priority road', 
            13:'Yield', 
            14:'Stop', 
            15:'No vehicles', 
            16:'Veh > 3.5 tons prohibited', 
            17:'No entry', 
            18:'General caution', 
            19:'Dangerous curve left', 
            20:'Dangerous curve right', 
            21:'Double curve', 
            22:'Bumpy road', 
            23:'Slippery road', 
            24:'Road narrows on the right', 
            25:'Road work', 
            26:'Traffic signals', 
            27:'Pedestrians', 
            28:'Children crossing', 
            29:'Bicycles crossing', 
            30:'Beware of ice/snow',
            31:'Wild animals crossing', 
            32:'End speed + passing limits', 
            33:'Turn right ahead', 
            34:'Turn left ahead', 
            35:'Ahead only', 
            36:'Go straight or right', 
            37:'Go straight or left', 
            38:'Keep right', 
            39:'Keep left', 
            40:'Roundabout mandatory', 
            41:'End of no passing', 
            42:'End no passing veh > 3.5 tons' }

    def load_model(self):
        model = keras.models.load_model('model.h5')
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def predict(self, model):
        data = []
        url = "https://media.discordapp.net/attachments/639307153013866550/982866407157022750/unknown.png"
        filename = url.split("/")[-1]

        img_data = requests.get(url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)

        try: 
            # response = requests.get(url, stream = True)
            # image_bytes = BytesIO(response.content)
            # image = Image.open(image_bytes)
            # a = np.asarray(image)
            image = cv2.imread(filename)
            image_fromarray = Image.fromarray(image, 'RGB')
            resize_image = image_fromarray.resize((30, 30))
            data.append(np.array(resize_image))
        except:
            print("Error")

        test = np.array(data) / 255

        pred = model.predict(test)
        classes_x=np.argmax(pred,axis=1)
        print(self.classes[classes_x[0]])

        os.remove(filename)



    