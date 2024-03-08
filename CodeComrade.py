import discord as dc
from discord.ext import commands


intents = dc.Intents.default()
intents.messages = True  # Enable message intents

client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("MTIxNTU1Nzg0NDI2MzIzOTY4MA.Gf1ibY.-g0kMh3LswifiT72rfWBqTXWnB3a1TMrCamOSU")



async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "neger":
        await message.channel.send == "sida"
    
