# bot.py

import twitch

import os
import random
import time

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.voice_client import VoiceClient

live = ["live1.mp3", "live2.mp3", "live3.mp3", "live4.mp3", "live5.mp3", "live6.mp3"]
not_live = ["not_live1.mp3", "not_live2.mp3", "not_live.mp3", "not_live.mp3"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="=")

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now tracking throwing.')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def dc(ctx):
    await ctx.voice_client.disconnect()


@bot.command(name="forsen")
async def is_streamer_live(ctx, *args):
    a = 0
    is_live = twitch.is_live("forsen")
    guild = ctx.guild
    vc: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=ctx.guild)


    try:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
        
        a = 1
    except Exception as e:
        print(e)
        await ctx.send("you are not in a voice channel retard")
    

    if is_live:
        if a == 0:
            await ctx.send("forsen is live pogchamp")
        else:
            audio = random.choice(live)
            audio_source = discord.FFmpegPCMAudio("voice_feedback/" + audio)
            voice_client.play(audio_source)
            
    else:
        if a == 0:
            await ctx.send("forsen is not live, fucking unlucky")
        else:
            audio = random.choice(not_live)
            audio_source = discord.FFmpegPCMAudio("voice_feedback/" + audio)
            voice_client.play(audio_source)


@bot.command(name="forsenquote")
async def quote(ctx):
    if (ctx.author == bot.user):
        return

    
    forsen_quotes = ["fucking unlucky", "forsene", "zulul", "no, "*10+"no, yes", "guys, relax", "bread boat OMEGALUL",
                    "hey molly", "The god gamer is back"]

    return_message = random.choice(forsen_quotes)
    await ctx.channel.send(return_message)

bot.run(TOKEN)
