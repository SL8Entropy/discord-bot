import discord
import os
import random
from discord.client import Client
import wikipedia
#

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$roll'):
        rand = random.randint(1,20)
        converted_num = str(rand)
        await message.channel.send("you rolled a d20 and got "+converted_num)
    if ":D" in message.content:
        await message.channel.send(':D')
    if message.content.startswith("$say"):
        string = message.content.strip("$say")
        await message.channel.send(string)
    if message.content.startswith("$wiki"):
        working_message = await message.channel.send("working on it...")
        string1 = message.content.strip("$wiki")
        try:
            search = wikipedia.search(string1, results = 5)

            search1 = search[0]
            result = wikipedia.summary(search1, sentences = 2, auto_suggest=False)
            await working_message.delete()
            await message.channel.send(result)
        except wikipedia.exceptions.PageError:
            await working_message.delete()
            await message.channel.send("No results found")
        except IndexError:
            await working_message.delete()
            await message.channel.send("Invalid search term. Please try again.")
        except wikipedia.exceptions.DisambiguationError as e:
            await working_message.delete()
            await message.channel.send("No Results Found. you may be referring to one of these")    
            for i in range(5):
                await message.channel.send(e.options[i]) 
    if message.content.startswith("$help"):
        await message.channel.send("Commands: $hello, $roll, $say, $help,$breakingpointpingspamXD, $wiki")
    if message.content.startswith("$breakingpointpingspamXD"):
        for x in range(30):
            await message.channel.send("<@714770535346864148>")
    
client.run(os.getenv("TOKEN"))
