import discord as dc
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = dc.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)



async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "neger":
        message.channel.send == "sida"
    
