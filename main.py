import discord
import os
from dotenv import load_dotenv
# import trained_model as model

# model = model.Model()
# loaded_model = model.load_model()
# model.predict(loaded_model)

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
  
  #Previnir que o Bot responda a ele mesmo
  if(author == "Emplacado"):
    return

  # ------ Comandos ------

  #comando com marcador $ para reconhecer um comando
  #if message.content.startswith('$'):
  if(content == prefix + "iniciar"):
    await message.delete()
    await channel.send("Bot iniciado!")
    
    
  if (anexo):
    url = anexo[0].proxy_url
    await message.delete()
    await channel.send(url)
    print(url)


#Executar e atualizar o Bot
client.run(TOKEN)
