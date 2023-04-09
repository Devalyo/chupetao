import discord
from discord.ext.commands import Bot
from pytube import YouTube
from helpers import *
import asyncio
import os
import re


FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
bot = Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} tuc tuc tuc!')


queue = []
displayQueue = []

@bot.command()
async def play(ctx, *, url):
    voiceChannel = ctx.author.voice.channel
    if not ctx.voice_client:
        await voiceChannel.connect()
        if random.randrange(1, 100) <= 100:    
                video = YouTube(busca(url))
                if video.length > 1800:
                        mensagem = await ctx.send("Video muito longo. Seu filho da puta.")
                        await asyncio.sleep(8)
                        await mensagem.edit(content=tuc())
                        return
                queue.append(busca(url))
                try:
                    displayQueue.append(video.title)
                except:
                    asyncio.sleep(3)
                    displayQueue.append(video.title)
                ctx.voice_client.play(discord.FFmpegPCMAudio(source="audio/chupetas.mp4", options=FFMPEG_OPTIONS), after=lambda e: PlayNext(ctx))
                return

    
    if ctx.voice_client.is_playing():
        video = YouTube(busca(url))
        if video.length > 1800:
                mensagem = await ctx.send("Video muito longo. Seu filho da puta.")
                await asyncio.sleep(8)
                await mensagem.edit(content=tuc())
                return
        queue.append(busca(url))
        try:
             displayQueue.append(video.title)
        except:
            asyncio.sleep(3)
            displayQueue.append(video.title)
        await ctx.send(f"{tuc()} ✔✔✔ {video.title}")
        return

    if not ctx.voice_client.is_playing():
        video = YouTube(busca(url))
        try:
            title = re.sub('[\'^%#{\}=!$*?/()|\n\."]', '', video.title)
        except:
            asyncio.sleep(3)
            title = re.sub('[\'^%#{\}=!$*?/()|\n\."]', '', video.title)
            
        
        audio_stream = video.streams.filter(only_audio=True).first()
        file_path = f'audio/{title}.mp4'
        if not os.path.exists(file_path):
            if video.length > 1800:
                mensagem = await ctx.send("Video muito longo. Seu filho da puta.")
                await asyncio.sleep(8)
                await mensagem.edit(content=tuc())
                return
            audio_stream.download(output_path='audio', filename=f"{title}.mp4")
        await ctx.send(f"{tuc()} 🎶▶ {video.title}")
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=file_path, options=FFMPEG_OPTIONS), after=lambda e: PlayNext(ctx))
         


def PlayNext(ctx):

    print("playing next...")
    if random.randrange(1,100) <= 20:
        ctx.voice_client.play(discord.FFmpegPCMAudio(source="audio/chupetas.mp4", options=FFMPEG_OPTIONS), after=lambda e: PlayNext(ctx))
        return
    if len(queue) > 0: 
        url = queue.pop(0)
        displayQueue.pop(0)
        video = YouTube(url)
        try:
            title = re.sub('[\'^%#{\}=!$*?/()\n|\."]', '', video.title)
        except:
            asyncio.sleep(3)
            title = re.sub('[\'^%#{\}=!$*?/()\n|\."]', '', video.title)
   
        audio_stream = video.streams.filter(only_audio=True).first()
        file_path = f'audio/{title}.mp4'

        if not os.path.exists(file_path):
                audio_stream.download(output_path='audio', filename=f"{title}.mp4")
        
        asyncio.run_coroutine_threadsafe(ctx.send(f"{tuc()} 🎶▶ {video.title}"), bot.loop)
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=file_path, options=FFMPEG_OPTIONS), after=lambda e: PlayNext(ctx))


@bot.command()        
async def skip(ctx):
    if ctx.voice_client:
        ctx.voice_client.stop()


@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send(f"{tuc()}???")       


@bot.command()
async def remove(ctx, index):
    numero = int(index)
    if numero > 0 and numero <= len(queue):
        await ctx.send(f"{tuc()} ❌❌❌ {displayQueue[numero - 1]}")
        del queue [numero - 1]
        del displayQueue [numero - 1]


@bot.command()
async def fila(ctx):

    if len(displayQueue) < 1:
        await ctx.send(f"{tuc()} 💨")
        return

    message = f"{tuc()}: ```\n"
    for i in range(len(displayQueue)):
        message += f"{i + 1} - {displayQueue[i]}\n"
    await ctx.send(message + '\n```')
          
nameList = ["chupetas", "chupetão", "chupetao", "chupetasso", "chupetola"]
@bot.event
async def on_message(message):
     if message.author == bot.user:
         await bot.process_commands(message)
         return
     
     text = str(message.content).lower()
     if any(word in text for word in nameList):
         if 'video' in text:
            await message.channel.send(get_url())
         mensagem = tuc(beast=True)
         sent_message = await message.channel.send(mensagem)
         if len(mensagem) > 63:
             await asyncio.sleep(8)
             await sent_message.edit(content=tuc())
     else:
         await bot.process_commands(message)
         return
     

def chups(ctx):
    ctx.voice_client.play(discord.FFmpegPCMAudio(source="audio/chupetas.mp3", options=FFMPEG_OPTIONS))


bot.run('')