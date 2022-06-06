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

prefix = '\\'

@client.event
async def on_ready():
  print ("BOT ONLINE")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=prefix+"help"))

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

  #comando utilizando o prefixo para reconhecer um comando

  if (content.startswith(prefix)):
    if(content == prefix + "iniciar"):
      await channel.send("Bot iniciado!")
      return
    
    elif content.startswith(prefix + "emp"):
      if (anexo):
        url = anexo[0].proxy_url
      else:
        img = content.split()
        url = img[1]
      response = model.predict(loaded_model, url)
      await channel.send(response)
      if ("Pare" in response):
        await message.add_reaction("🛑")
      return
      
    elif (content == prefix + "sobre"):
      sobre = """
      Projeto Integrador 5 - Aplicação de Inteligência Artificial

      Alunos:
        * Gabriel Kenji
        * Kauê Sales
        * Thiago Felix
        * Vinycius Zanardi

      Web-site: [Em construção] ⚠️
      Artigo Científico: [Em construção] ⚠️
      Para mais informações: https://github.com/kahbyte/Emplacado 🖥️
      """
      await channel.send(sobre)
    
    #elif (content == prefix + "site"):
      #await message.delete()
      #await channel.send("regra do senac é seu c*")
    
    #Novo comando de piada
    #elif (content == )

    elif (content == prefix + "classes"):
      classes = model.classes.items()

      list = """"""

      for key, value in classes:
        list += (f"{key}: {value}") + "\n" 

      await channel.send("`" + list + "`")

    elif (content == prefix + "help"):
      help = """Comandos:
      """+prefix+"""emp - e adicione uma imagem via link ou anexo para reconhecer uma placa
      """+prefix+"""sobre - para mais informações referentes ao projeto
      """+prefix+"""classes - para conhecer as placas que podem ser reconhecidas
      """
      await channel.send(help)
    
    elif (content == prefix + "celso"):
      await channel.send("Esse professor é show!")

    else:
      error = mention + "Comando invalido. Digite "+prefix+"help."
      #error = "Comando invalido. Digite "+prefix+"help."
      await channel.send(error)

#Executar e atualizar o Bot
client.run(TOKEN)