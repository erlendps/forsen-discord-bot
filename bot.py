# bot.py

import twitch

import os
import random
import time
from mutagen.mp3 import MP3

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.voice_client import VoiceClient

import youtube_dl

players = {}

live = ["live1.mp3", "live2.mp3", "live3.mp3", "live4.mp3", "live5.mp3", "live6.mp3", "forsenbajs.mp3"]
not_live = ["not_live1.mp3", "not_live2.mp3", "not_live3.mp3", "not_live4.mp3"]

forsen_quotes = ["fucking unlucky", "forsene", "zulul", "no, "*10+"no, yes", "guys, relax", "bread boat OMEGALUL",
                    "hey molly", "The god gamer is back", "📜 ✍ Sadge 𝓜𝔂 𝓭𝓮𝓪𝓻𝓮𝓼𝓽 𝓫𝓻𝓸𝓽𝓱𝓮𝓻, 𝓽𝓸𝓭𝓪𝔂 𝓶𝓪𝓻𝓴𝓼 𝓽𝓱𝓮 8𝓽𝓱 𝔂𝓮𝓪𝓻 𝔀𝓮 𝓱𝓪𝓿𝓮 𝓱𝓪𝓭 𝔀𝓲𝓽𝓱𝓸𝓾𝓽 𝓿𝓪𝓻𝓲𝓮𝓽𝔂. 𝓦𝓮 𝓶𝓪𝔂 𝓷𝓸𝓽 𝓫𝓮 𝓪𝓫𝓵𝓮 𝓽𝓸 𝓮𝓷𝓭𝓾𝓻𝓮. 𝓟𝓵𝓮𝓪𝓼𝓮 𝓹𝓻𝓪𝔂 𝓯𝓸𝓻 𝓸𝓾𝓻 𝓼𝓪𝓵𝓿𝓪𝓽𝓲𝓸𝓷. .",
                    "forsenCD YOU MAY SAY THAT IM A DREAMER forsenCD BUT IM NOT THE ONLY ONE forsenCD I HOPE SOMEDAY YOU'LL JOIN US forsenCD AND THE WORLD WILL BE AS ONE forsenCD",
                    """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⡛⠛⠛⠛⠻⢿⣿⣿⣿⣿
⡹⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⠋⠄⠄⣀⣴⣶⣦⣀⣿⣿⠿⢟
⣿⣷⣬⣛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣯⠄⠄⣼⣿⣟⠙⢻⣿⠈⣴⣾⣿
⣿⣿⣿⣿⣿⣷⣶⣯⠍⣫⡭⠉⠻⢿⣿⣧⢻⣮⠄⠄⣿⣿⣿⠿⢚⣱⣰⣾⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠅⡀⠟⣱⣿⠿⠸⣿⣿⣧⡄⣤⡜⠛⣿⣿⣤⣀⣾⢘⣿⣿⣿
⣿⣿⣿⣿⣿⢯⠖⣶⡇⣾⢏⣥⣶⣶⣶⣶⣶⣥⡉⢳⣆⠈⠛⠿⠟⢃⣸⣿⣿⣿
⣿⣿⡿⢟⠶⣣⣾⣿⢇⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣇⣙⣛⣛⣃⡺⠿⣿⣿⣿⣿
⣿⣿⠓⢁⣾⣿⡟⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡹⣿⣿
⣿⡏⣸⣿⡿⢏⣈⠿⢿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢻⣿
⣿⢃⣿⢛⣤⣾⣿⣿⣦⣍⡛⠟⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣧⠘⣿
⡟⡿⢣⣾⣿⣿⣿⣿⣿⡿⢃⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⠄⣿
⢀⣴⣿⣿⣿⣿⣿⠿⢏⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢤⣶⠄⣿""",
"You 'Bajs' are fucking pathetic. I've been watching your 'god gamer' for 3 hours now and not only has he failed to complete a single run, but he hasn't even cured my depression once.",
"📜 ✍ ️ Okayge 𝓑𝓻𝓸𝓽𝓱𝓮𝓻 𝓘 𝓻𝓮𝓬𝓮𝓲𝓿𝓮𝓭 𝔂𝓸𝓾𝓻 𝓶𝓮𝓼𝓼𝓪𝓰𝓮 𝔀𝓮𝓵𝓵. 𝓘𝓽 𝓮𝔁𝓬𝓲𝓽𝓮𝓼 𝓶𝓮 𝓽𝓸 𝓲𝓷𝓯𝓸𝓻𝓶 𝔂𝓸𝓾 𝓪𝓫𝓸𝓾𝓽 𝓪 𝓬𝓸𝓬𝓴 𝓻𝓮𝓼𝓮𝓻𝓿𝓮, 𝓯𝓻𝓮𝓽 𝓷𝓸𝓽, 𝓬𝓸𝓬𝓴 𝔀𝓲𝓵𝓵 𝓫𝓮 𝓼𝓮𝓷𝓽 𝔂𝓸𝓾𝓻 𝔀𝓪𝔂 𝓼𝓸𝓸𝓷.",
"FeelsOkayMan 🍷 Such exquisite entertainment certainly would not be complete without some full blown ass-blasting gachimuchi, wouldn't you agree, Mr Fors?",
"Hello everyone, I don’t know if this is the place to say this but since bunch of females have been coming out saying people have sexually assaulted them I as a male need to get this off my chest. I met forsen one year ago at the gym lockerroom when he was doing two streams with workout in between. He said why I was wearing a jabroni outfit and I said “fuck you”, he responded back with “no fuck you leatherman” and things got heated up.",
"""⣿⣿⣿⣿⢹⣿⡂⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢸⣿⡒⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣸⣿⣂⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣸⣿⠂⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢸⢿⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢸⣿⠄⣼⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠙⠋⠙⠿⣯⡿⠽⠿⢿⣿⣿⣿
⣿⣿⣿⡟⣼⣭⠍⠫⠸⠟⢛⣉⣥⣤⣶⠾⠛⠩⠄⠒⠄⡀⠄⠄⢀⣁⣀⠙⠿⣿
⣿⠿⠟⢋⣓⣭⣥⣶⣶⣿⣿⣿⣿⣿⣿⠅⣠⣤⣶⣶⣶⣶⣄⢠⣶⣶⣶⣦⣤⠙
⢁⣴⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡟⢿⡟⢈⠻⢿⣿⣿⣿⠿⠟⠸⢿⣿⣿⣿⡿⠇
⣾⡟⢠⢊⣥⣶⠶⢦⣬⣭⣉⡛⠷⣤⣙⡂⠉⠒⠒⠒⠒⣂⣠⡈⠠⠄⠄⠄⢀⠄
⠘⣷⣿⡘⠿⠿⠿⢷⣶⣭⣍⣛⡳⠶⣤⣍⣙⡛⠛⠿⠿⣿⣿⣿⣦⠶⠿⠿⠛⢠
⣅⡈⢙⠿⣿⣿⣿⣶⣶⣬⣍⣛⠛⠿⢶⣦⣭⣭⣙⣛⠶⠶⠶⢶⡶⠶⠾⢟⢁⣾
⣿⣿⣶⣬⣀⡈⠙⢛⠻⠿⠿⣿⣿⣷⣶⣶⣤⣭⣭⣛⠛⠻⠿⠶⠶⠖⢂⣼⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣷⣤⣤⣤⣂⣐⣂⣒⣠⣄⠤⣴⣶⣷⣶⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿""",
"The doubters have been wrong 100% of the time",
"forsenbajs",
"pray for allah seeds"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MEMBER_ID = os.getenv('BOT_MEMBER_ID')

bot = commands.Bot(command_prefix="=")

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now tracking throwing.')


@bot.command(brief="dont use this")
async def join(ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    
    in_channel = False

    for member in channel.members:
        if member.id == int(MEMBER_ID):
            in_channel = True

    if voice == None:
        vc = await channel.connect()
        return vc
    elif in_channel == False:
        await ctx.send("cant you see im elsewhere??")
    else:
        return voice

@bot.command(brief="Disconnets the bot")
async def dc(ctx):
    await ctx.voice_client.disconnect()


@bot.command(name="forsen", brief="Tells you wether forsen is live or not")
async def is_streamer_live(ctx, *args):
    a = 0
    is_live = twitch.is_live("forsen")

    try:
        voice_client = await join(ctx)
        if voice_client is not None:
            a = 1
        
    except Exception as e:
        print(e)
        await ctx.send("you are not in a voice channel retard")

    if is_live:
        if a == 0:
            await ctx.send("forsen is live pogchamp")
        else:
            audio = random.choice(live)
            audio_length = MP3("voice_feedback/" + audio).info.length
            audio_source = discord.FFmpegPCMAudio("voice_feedback/" + audio)
            voice_client.play(audio_source)
            time.sleep(audio_length)
            await voice_client.disconnect()
            
    else:
        if a == 0:
            await ctx.send("forsen is not live, fucking unlucky")
        else:
            audio = random.choice(not_live)
            audio_length = MP3("voice_feedback/" + audio).info.length
            audio_source = discord.FFmpegPCMAudio("voice_feedback/" + audio)
            voice_client.play(audio_source)
            time.sleep(audio_length)
            await voice_client.disconnect()


@bot.command(name="forsenquote", brief="Returns a forsen copypasta or quote")
async def quote(ctx):
    if (ctx.author == bot.user):
        return

    return_message = random.choice(forsen_quotes)
    await ctx.channel.send(return_message)



@bot.command(name="forsenbajs", brief="plays forsenbajs")
async def bajs(ctx):
    b = 0
    try:
        voice_client = await join(ctx)
        if voice_client is not None:
            b = 1
        
    except Exception as e:
        print(e)
        await ctx.send("you are not in a voice channel retard")
    
    if b == 1:
        audio_source = discord.FFmpegPCMAudio("voice_feedback/forsenbajs.mp3")
        voice_client.play(audio_source)
        

bot.run(TOKEN)
