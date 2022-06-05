import numpy as np
import os
import cv2
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import requests


class Model: 
    def load_model(self):
        model = keras.models.load_model('model.h5')
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def predict(self, model, url):
        data = []
        url = url
        filename = url.split("/")[-1]

        self.save_image(url, filename)

        try: 
            data.append(self.prepare_image(filename))
        except:
            print("Error preparing image")

        test = np.array(data) / 255

        pred = model.predict(test)
        classes_x=np.argmax(pred,axis=1)
        print(self.classes[classes_x[0]])

        os.remove(filename)
         
    def save_image(self, url, filename):
        img_data = requests.get(url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)

    def prepare_image(self, filename):
        image = cv2.imread(filename)
        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((30, 30))
        return np.array(resize_image)

    classes = { 0:'Limite de velocidade (20km/h)',
            1:'Limite de velocidade (30km/h)', 
            2:'Limite de velocidade (50km/h)', 
            3:'Limite de velocidade (60km/h)', 
            4:'Limite de velocidade (70km/h)', 
            5:'Limite de velocidade (80km/h)', 
            6:'Fim do Limite de velocidade (80km/h)', 
            7:'Limite de velocidade (100km/h)', 
            8:'Limite de velocidade (120km/h)', 
            9:'Proibido ultrapassar', 
            10:'Nenhum veículo com mais de 3.5 tons.', 
            11:'Direito de passagem no cruzamento', 
            12:'Estrada prioritária', 
            13:'Rendimento', 
            14:'Pare', 
            15:'Sem veículos', 
            16:'Veículos > 3.5tons proibidos', 
            17:'Entrada Probida', 
            18:'Cuidado geral', 
            19:'Curva perigosa a esquerda', 
            20:'Curva perigosa a direita', 
            21:'Curva dupla', 
            22:'Estrada esburacada', 
            23:'Estrada escorregadia', 
            24:'Estrada estreita à direita', 
            25:'Obras na estrada', 
            26:'Placas de trânsito', 
            27:'Pedestres', 
            28:'Crianças atravessando', 
            29:'Bicicletas atravessando', 
            30:'Cuidado com gelo/neve',
            31:'Animais selvagens atravessando', 
            32:'Velocidade final + limites de ultrapassagem', 
            33:'Vire à direita', 
            34:'Vire à esquerda', 
            35:'Siga em frente', 
            36:'Vá direto ou para a direita', 
            37:'Vá direto ou para a esquerda', 
            38:'Permaneça a direita', 
            39:'Permaneça a esquerda', 
            40:'Rotatória obrigatória', 
            41:'Fim de não ultrapassar', 
            42:'Fim de não ultrapassar veículos > 3.5 tons' 
            }   