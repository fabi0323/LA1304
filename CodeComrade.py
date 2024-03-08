import discord as dc
from discord.ext import commands


intents = dc.Intents.all()


bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def sida(ctx):
    if ctx.author == bot.user:
        return
    print("test")
    await ctx.send("sida")

    
bot.run("MTIxNTU1Nzg0NDI2MzIzOTY4MA.Gf1ibY.-g0kMh3LswifiT72rfWBqTXWnB3a1TMrCamOSU")
