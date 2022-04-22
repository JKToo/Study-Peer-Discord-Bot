import discord
import os
import requests
import json
import random
import re
client = discord.Client()

def translate(text): #google translate

    converted = text.replace(" ", "%20")
    
    url = "https://google-translate20.p.rapidapi.com/translate"
    
    querystring = {"text":text,"tl":"zh-TW","sl":"en"}
    
    headers = {
        'x-rapidapi-host': "google-translate20.p.rapidapi.com",
        'x-rapidapi-key': ""
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    text = response.json()
   # print(response.text)
    datas = text['data']
    translation = datas['translation']
    pinyin = datas['pronunciation']
    endOutput = "Translation: " + translation + ", " + pinyin

    return (endOutput)


    
arr = []
arrHolder = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    number = 0
    msg = message.content
    if message.author == client.user:
    	return            

    if msg.startswith("!new"):
        questionContent = msg.split("!new ", 1) [1]
        arr.append(questionContent)
        await message.channel.send("Added question")
            
    if msg.startswith("!list"):
        size = len(arr)
        await message.channel.send("These are all the questions:")
        await message.channel.send(arr)

    if msg.startswith("!start") or msg.startswith("!Start"):
        size = len(arr)
        if size == 0:
            await message.channel.send("You have no questions stored")

        else:
            await message.channel.send("Starting. . . Please do !q")
            
    if msg.startswith("!q") or msg.startswith("!Q"): 
        size = len(arr)        
        if size == 0:
            await message.channel.send("There are no more questions")
        else:
            value = arr[number]
            arrHolder.append(value)
            await message.channel.send(value)
            arr.pop(number)

    if msg.startswith("!reset"):
        arr.clear()
        await message.channel.send("Questions cleared")


    if msg.startswith("!translate"):
        questionContent = msg.split("!translate ", 1) [1]
        translation = translate(questionContent)
        await message.channel.send(translation)

    if msg.startswith("!help"):
        await message.channel.send("!translate *word* -> translates word from english to chinese\n!new *question / word* -> adds a new question or word to the list\n!list -> lists all the questions / words in the list\n!q -> Outputs the question / word to test you")
        
client.run(os.getenv('TOKEN'))
