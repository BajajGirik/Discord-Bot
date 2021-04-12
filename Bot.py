import discord
import os
import requests
import json
import random
from Keep_alive import keep_alive

client = discord.Client()

f_hriday = ["Hriday U Fking....\nU Bloody Bastard",  "Hriday is as useless as ueue in the word queue.", "The world is a better place when Hriday is asleep.", "Hriday U Stupid?....Sorry that was an inappropriate question for a born baka.", "Tauba Tauba subha subha hriday ko dekhke mood kharab ho gaya.", "Hriday ye le tu gari chala......o wait u failed ur driving license.", "I seriously hate fridays", "#ChangeEx-Monorach", "Hey Look at my dp.....isn't it awful"]

def get_joke():
  response = requests.get("https://api.chucknorris.io/jokes/random")
  json_data = json.loads(response.text)
  meme = json_data["value"]
  return meme

def get_meme():
  response = requests.get("https://official-joke-api.appspot.com/random_joke")
  json_data = json.loads(response.text)
  meme = json_data["setup"] + '\n' + json_data["punchline"]
  return meme

def inspire():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + '\n-' + json_data[0]["a"]
  return quote

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return  
  
  if message.content.lower().startswith('!hello'):
    if message.author.name == 'ICTOAE1321':
      await message.channel.send('Chalo Chalo aage bado....')
    
    else:  
      await message.channel.send('Moshi Moshi {} sama'.format(message.author.name)) 

  if message.content.lower().startswith('!chuckjoke'):
    meme = get_joke()
    await message.channel.send(meme)

  if message.content.lower().startswith('!joke'):
    meme = get_meme()
    await message.channel.send(meme)
 
  if message.content.lower().startswith('!inspire'):
    quote = inspire()
    await message.channel.send(quote)

  if 'hriday' in message.content.lower():
    await message.channel.send(random.choice(f_hriday))

keep_alive()
client.run(os.getenv('TOKEN'))