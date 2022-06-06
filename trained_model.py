from urllib import response
import numpy as np
import os
import cv2
from tensorflow import keras
from PIL import Image
import requests
import random


class Model: 
    def load_model(self):
        model = keras.models.load_model('model.h5')
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def predict(self, model, url):
        data = []
        url = url
        filename = url.split("/")[-1]
        
        if not self.is_valid_format(filename):
            supported_formats = 'Formatos suportados: jpg, jpeg, png, etc.'
            return f"{random.choice(self.rude_responses)} `" + supported_formats + "`"

        self.save_image(url, filename)

        try: 
            data.append(self.prepare_image(filename))
        except:
            print("Error preparing image")

        result = self.test_image(data, model)
        response = f"{self.random_response()} `" + self.classes[result[0]] + "`"
        return response
         
    def save_image(self, url, filename):
        img_data = requests.get(url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)

    def prepare_image(self, filename):
        image = cv2.imread(filename)
        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((30, 30))
        os.remove(filename)
        return np.array(resize_image)
    
    def test_image(self, data, model):
        test = np.array(data) / 255

        pred = model.predict(test)
        classes_x=np.argmax(pred,axis=1)
        return classes_x

    def is_valid_format(self, filename): 
        format = filename.split(".")[-1]
        return format == "jpg" or format == 'png' or format == "jpeg"
    
    def random_response(self):
        return random.choice(self.sign_responses)
    
    rude_responses = [
        'Deve ser a sua mãe.',
        'Manda a mãe para ver se classifica.',
        'Você não vai me pegar tão fácil.',
        'Que feio, mandando imagem nada a ver para tirar nota de aluno'
    ]

    sign_responses = [
        'isso me parece uma placa de:',
        'meio torto, acho que é:', 
        'Vendo por esse ângulo, parece:',
        'Definitivamente é:',
        'Se eu tivesse que perguntar pro Celso, ele diria que é:',
        'Na rua, o Thiago vê isso como:',
        'Olhando por esse lado, é:',
        'Alguem do grupo digitou rapidinho que é:',
        'Celso, me da um 10 por esse acerto:',
        'Valendo uma pizza:',
        'Já vi essa umas 50mil vezes enquanto treinava:',
        'Sabia que eu levei 15min pra aprender essa numa GPU?',
        'As CPUs do Senac levariam umas 30 horas pra aprender essa ai:'
    ]

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