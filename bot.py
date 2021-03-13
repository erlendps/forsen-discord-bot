# bot.py

import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="=")

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now tracking throwing.')

@bot.event
async def on_message(message):
    if (message.author == bot.user):
        return
    
    forsen_quotes = ["fucking unlucky", "forsene", "zulul", "no, "*10+"no, yes", "guys, relax", "bread boat OMEGALUL",
                    "hey molly", "The god gamer is back"]

    if "forsen" in message.content.lower():
        return_message = random.choice(forsen_quotes)
        await message.channel.send(return_message)

@bot.command(name="forsen")
async def is_forsen_live():
    return


bot.run(TOKEN)


