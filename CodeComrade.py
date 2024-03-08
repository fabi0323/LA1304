import discord as dc
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = dc.Intents.default()
intents.messages = True  # Enable message intents

client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)



async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "neger":
        message.channel.send == "sida"
    
