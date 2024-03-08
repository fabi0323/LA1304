import discord as dc
from discord.ext import commands
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


intents = dc.Intents.all()
preferred_channel_id = None

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)



bot = commands.Bot(command_prefix='.', intents=intents)

def is_preferred_channel(ctx):
    return ctx.message.channel.id == preferred_channel_id

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='prefChannel')
async def channelSettings(ctx):
    
    global preferred_channel_id

    # Set the preferred channel to the channel where the command was invoked
    preferred_channel_id = ctx.message.channel.id

    await ctx.send(f"Preferred channel set to {ctx.message.channel.mention}")



@bot.command(name='inf')
async def get_information(ctx, language, topic):
    

    input_text = f"{language}: {topic}"

    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    attention_mask = [1] * len(input_ids[0])

    model.config.pad_token_id = model.config.eos_token_id

    output = model.generate(input_ids, attention_mask=torch.tensor([attention_mask]), max_length=150, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    await ctx.send(response)


    

    
bot.run("MTIxNTU1Nzg0NDI2MzIzOTY4MA.Gf1ibY.-g0kMh3LswifiT72rfWBqTXWnB3a1TMrCamOSU")
