import discord
import os
import requests
import json

client = discord.Client()

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

  if message.content.startswith('!Hello'):
    await message.channel.send('Hello {}'.format(message.author.name))  
  
  if message.content.startswith('!hello'):
    await message.channel.send('Hello {}'.format(message.author.name)) 

  if message.content.startswith('!ChuckJoke'):
    meme = get_joke()
    await message.channel.send(meme)

  if message.content.startswith('!joke'):
    meme = get_meme()
    await message.channel.send(meme)

  if message.content.startswith('!Joke'):
    meme = get_meme()
    await message.channel.send(meme)

  if message.content.startswith('!Inspire'):
    quote = inspire()
    await message.channel.send(quote)
 
  if message.content.startswith('!inspire'):
    quote = inspire()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))
