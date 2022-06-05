import discord
import os
from dotenv import load_dotenv
#import trained_model as model


# --------- Modelo --------
#Passagem da url da imagem para o modelo analizar

#model = model.Model()
#loaded_model = model.load_model()

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
  if(content == prefix + "iniciar"):
    #await message.delete()
    await channel.send("Bot iniciado!")
    
  #if (anexo and (content == prefix + "emp")):
   

  if (content == prefix + "emp"):
    if (anexo):
      url = anexo[0].proxy_url
      #await message.delete()
      print(url)
      
    else:
      img = content.split()
      url = img[1]
      print(img)
      print(url)
    

  if (content == prefix + "sobre"):
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


  if (content == prefix + "help"):
    help = """Comandos:
    $emp - para reconhecer uma placa
    $sobre - para saber mais referente ao projeto
    """
    await channel.send(help)
     
  if (content == prefix + "site"):
    await message.delete()
    await channel.send("regra do senac é seu c*")

  #response = model.predict(loaded_model, url)
  #await channel.send("A sua placa é: `" + response + "`")


#Executar e atualizar o Bot
client.run(TOKEN)