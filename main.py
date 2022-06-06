from statistics import mode
import discord
import os
from dotenv import load_dotenv
import trained_model as model


# --------- Modelo --------
#Passagem da url da imagem para o modelo analizar

model = model.Model()
loaded_model = model.load_model()

load_dotenv()

#Definição do nosso cliente do discord
client = discord.Client()

#Token de segurança do nosso discord
TOKEN = os.getenv("TOKEN")
#Executar em caso de perca do TOKEN
#print(TOKEN)

prefix = '$'

@client.event
async def on_ready():
  print ("BOT ONLINE")

@client.event
async def on_message(message):
  content = message.content.lower()
  channel = message.channel
  author = message.author.name
  anexo = message.attachments
  mention = message.author.mention

  #Previnir que o Bot responda a ele mesmo
  if(author == "Emplacado"):
    return

  # ------ Comandos ------

  #comando com marcador $ para reconhecer um comando
  #if message.content.startswith('$'):

  if (content.startswith(prefix)):
    if(content == prefix + "iniciar"):
      await channel.send("Bot iniciado!")
      return
    
    elif content.startswith(prefix + "emp"):
      print("recebi emp")
      if (anexo):
        print("imagem anexada")
        url = anexo[0].proxy_url
        print(url)
        
      else:
        print("imagem com link")
        img = content.split()
        url = img[1]
        print(img)
        print(url)
      response = model.predict(loaded_model, url)
      await channel.send(f"{model.random_response()} `" + response + "`")
      return
      
    elif (content == prefix + "sobre"):
      sobre = """
      Projeto Integrador 5 - Aplicação de Inteligência Artificial

      Alunos:
        * Gabriel Kenji
        * Kauê Sales
        * Thiago Felix
        * Vinycius Zanardi

      Web-site:
      Artigo Científico: 
      Para mais informações: https://github.com/kahbyte/Emplacado 
      """
      await channel.send(sobre)
    
    elif (content == prefix + "site"):
      await message.delete()
      await channel.send("regra do senac é seu c*")
    
    elif (content == prefix + "classes"):
      classes = model.classes.items()

      list = """"""

      for key, value in classes:
        list += (f"{key}: {value}") + "\n"
      print(list) 

      await channel.send("`" + list + "`")

    elif (content == prefix + "help"):
      help = """Comandos:
      $emp - e adicione uma imagem via link ou anexo para reconhecer uma placa
      $sobre - para mais informações referentes ao projeto
      $classes - para conhecer as placas que podem ser reconhecidas
      """
      await channel.send(help)
    
    else:
      error = "comando invalido. Digite $help."
      await channel.send(error)

#Executar e atualizar o Bot
client.run(TOKEN)