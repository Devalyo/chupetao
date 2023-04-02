import discord
from discord.ext.commands import Bot
from pytube import YouTube
from urlgen import *
import asyncio
import os


FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
bot = Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} tuc tuc tuc!')


queue = []
@bot.command()
async def play(ctx, *, url):
    voiceChannel = ctx.author.voice.channel
    if not ctx.voice_client:
        await voiceChannel.connect()

    video = YouTube(busca(url))
    if ctx.voice_client.is_playing():

        queue.append(busca(url))
        displayQueue.append(video.title)

    if not ctx.voice_client.is_playing():
        video = YouTube(busca(url))
        audio_stream = video.streams.filter(only_audio=True).first()
        file_path = f'audio/{video.title}'
        if not os.path.exists(file_path):
            audio_stream.download(output_path='audio', filename=video.title)
        await ctx.send(f"{itsNothing()} -> {video.title}")
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=file_path, options=FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

 
def play_next(ctx):
    print("playing next...")
    if len(queue) > 0:
        url = queue.pop(0)
        video = YouTube(url)
        audio_stream = video.streams.filter(only_audio=True).first()
        file_path = f'audio/{video.title}'
        if not os.path.exists(file_path):
            audio_stream.download(output_path='audio', filename=video.title)
        asyncio.run_coroutine_threadsafe(ctx.send(f"{itsNothing()} -> {video.title}"), bot.loop)
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=file_path, options=FFMPEG_OPTIONS), after=lambda e: play_next(ctx))


@bot.command()        
async def skip(ctx):
    if ctx.voice_client:
        ctx.voice_client.stop()

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send(f"{itsNothing()}???")       

#this is stupid
displayQueue = []
@bot.command()
async def fila(ctx):
    message = f"{itsNothing()}:\n ```\n"
    for i in range(len(displayQueue)):
        message += f"{i + 1} - {displayQueue[i]}\n"
    await ctx.send(message + '\n```')
          

@bot.event
async def on_message(message):
     if message.author == bot.user:
         await bot.process_commands(message)
         return
     text = str(message.content).lower()
     if 'chupetao' not in text:
         await bot.process_commands(message)
         return
        
     if 'video' in text:
        await message.channel.send(get_url())
     elif 'obrigado' or 'valeu' in text:
             await message.channel.send(itsNothing())

     await bot.process_commands(message)


bot.run('')