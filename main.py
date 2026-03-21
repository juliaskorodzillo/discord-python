import discord
from discord.ext import commands
from model import get_class
import os,random
import requests
from PIL import Image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            await attachment.save(f'./{filename}')
            image = Image.open(filename)
            await ctx.send(get_class(image,"keras_model.h5", "labels.txt"))
    else:
        await ctx.send("Nie załączyłeś pliku!")

bot.run("bot token")
