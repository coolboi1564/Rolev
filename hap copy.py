import discord
from discord import user
from discord.ext import commands, tasks
from googlesearch import search as sarch
from googletrans import Translator, constants
from pprint import pprint
import random
import time
import youtube_dl as ydl
import os
import discord.utils
from discord.utils import get 

client = commands.Bot(command_prefix="!")

translator = Translator()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("It's none of ur business"))
    print("Bot is online!")

@client.command()
async def play(ctx, *, question):
    query = question    

    for i in sarch(query, tld="com" or "co.in", num=1, stop=1, pause=1):    
        print(i)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send('Wait for the music playing right now to stop or use the !stop to stop the music')
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    video_link = i                
ydl_opts = {'format': 'bestaudio'}
with ydl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(download=False)
    URL = info['formats'][0]['url']
voice = get(client.voice_clients, guild=ctx.guild, video_link)
voice.play(discord.FFmpegPCMAudio(URL))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot already left")  

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('Audio is already paused')

@client.command(aliases=['continue'])
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('The bot is already playing')

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    
client.run('your token')
    
