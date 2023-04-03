import discord
from discord.ext.commands import Bot
from pytube import YouTube
from urlgen import *
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

    video = YouTube(busca(url))
    if ctx.voice_client.is_playing():

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
        title = re.sub('[\'^%#{\}=!$*?/()\n\."]', '', video.title)
        audio_stream = video.streams.filter(only_audio=True).first()
        file_path = f'audio/{title}.mp4'
        if not os.path.exists(file_path):
            audio_stream.download(output_path='audio', filename=f"{title}.mp4")
        await ctx.send(f"{tuc()} 🎶▶ {video.title}")
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=file_path, options=FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

 
def play_next(ctx):

    print("playing next...")
    if len(queue) > 0:
        url = queue.pop(0)
        displayQueue.pop(0)

        video = YouTube(url)
        title = re.sub('[\'^%#{\}=!$*?/()\n\."]', '', video.title)
        audio_stream = video.streams.filter(only_audio=True).first()
        file_path = f'audio/{title}.mp4'

        if not os.path.exists(file_path):
            audio_stream.download(output_path='audio', filename=f"{title}.mp4")
        asyncio.run_coroutine_threadsafe(ctx.send(f"{tuc()} 🎶▶ {video.title}"), bot.loop)
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

    message = f"{tuc()}: ```\n"
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
     else:
         mensagem = tuc(beast=True)
         sent_message = await message.channel.send(mensagem)
         if len(mensagem) > 20:
             await asyncio.sleep(3)
             await sent_message.edit(content=tuc())
         

     await bot.process_commands(message)

beast = False
def tuc(beast=False):
    if  random.randrange(0,100) > 96 and beast:
        noTucs = ["A verdade sempre está com a minoria, e a minoria é sempre mais forte do que a maioria, porque a minoria geralmente é formada por quem realmente tem opinião, enquanto a força da maioria é ilusória, formada pelas gangues que não têm opinião; e que, portanto, no próximo instante (quando é evidente que a minoria é a mais forte) assume sua opinião… Enquanto isso, a verdade novamente se reverte para uma nova minoria.", "Existir significa 'escolher', mas isso não representa a riqueza, mas a miséria do homem. Sua liberdade de escolha não é sua grandeza, mas seu drama permanente. De fato, ele sempre se depara com a alternativa de uma 'possibilidade de sim' e uma 'possibilidade de não', sem possuir qualquer critério seguro. E tateando no escuro numa posição instável de indecisão permanente.", "Não existe pátria para quem desespera e, quanto a mim, sei que o mar me precede e me segue, e minha loucura está sempre pronta. Aqueles que se amam e são separados podem viver sua dor, mas isso não é desespero: eles sabem que o amor existe. Eis porque sofro, de olhos secos, este exílio. Espero ainda. Um dia chega, enfim...", "Há um incêndio no interior de um teatro. O palhaço sobe ao palco para avisar o público. Eles pensam que é uma piada e aplaudem. O palhaço repete e é aplaudido com mais entusiasmo. É como eu penso que o mundo chegará ao seu fim: sendo aplaudido por testemunhas que acreditam que tudo não passa de uma piada", "De repente, estou só no mundo. Vejo tudo isto do alto de um telhado espiritual. Estou só no mundo. Ver é estar distante. Ver claro é parar. Analisar é ser estrangeiro. Toda a gente passa sem roçar por mim. Tenho só ar à minha volta. Sinto-me tão isolado que sinto a distância entre mim e o meu fato.", "De repente, estou só no mundo. Vejo tudo isto do alto de um telhado espiritual. Estou só no mundo. Ver é estar distante. Ver claro é parar. Analisar é ser estrangeiro. Toda a gente passa sem roçar por mim. Tenho só ar à minha volta. Sinto-me tão isolado que sinto a distância entre mim e o meu fato. "]
        beast = True
        return random.choice(noTucs)
    tucs = ('tuc ' * (random.randint(1,20)))
    return tucs


bot.run('')