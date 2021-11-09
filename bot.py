# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import choice
import time

bootTime = time.localtime()

logFile = open(f'logs/{time.strftime("%Y-%m-%d_%H.%M.%S", bootTime)}', 'w+')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MY_ID = int(os.getenv('MY_ID'))

# craigSimp = [
#     ':blush: hi Craig! :heart_eyes::kissing_closed_eyes:',
#     ':star_struck: OMG guys it\'s Craig!! :star_struck:',
#     ':sparkles::sparkling_heart::smiling_face_with_3_hearts: I LOVE YOU CRAIG!!!! :sparkles::sparkling_heart::smiling_face_with_3_hearts:'
# ]

bonkGifs = ['https://tenor.com/view/statewide-rp-mess-with-the-honk-you-get-the-bonk-baseballbat-untitled-goose-game-gif-17204101',
'https://tenor.com/view/mihoyo-genshin-genshin-impact-paimon-you-deserved-gif-23340767',
'https://tenor.com/view/chikku-neesan-girl-hit-wall-stfu-anime-girl-smack-gif-17078255',
'https://tenor.com/view/anime-bonk-gif-22497698',
'https://tenor.com/view/horny-bonk-gif-22415732',
'https://tenor.com/view/no-horny-gura-bonk-gif-22888944']


def log(ctx, args):
    currentTime = time.localtime()
    logMessage = f'{time.strftime("%Y-%m-%d_%H.%M.%S", currentTime)} | {ctx.channel} | {ctx.author} used {ctx.command}: {" ".join(args)}'
    logFile.write(f'\n{logMessage}')
    print(logMessage)

bot = commands.Bot(command_prefix='\\')

@bot.event
async def on_ready():
    currentTime = time.localtime()
    print(f'{bot.user} is connected!')
    logFile.write(f'{time.strftime("%Y-%m-%d_%H.%M.%S", currentTime)} | {bot.user} is connected!')

@bot.command()
async def pingme(ctx, *args):
    await ctx.send(f'hi {ctx.author.mention}!')
    log(ctx, args)

@bot.command()
async def stop(ctx, *args):
    if ctx.author.id == MY_ID:
        await ctx.send('`shutting down...`')
        time.sleep(1)
        await ctx.send('`goodnight`')
        log(ctx, args)
        exit(code=0)

@bot.command()
async def sp(ctx, *args):
    await ctx.message.delete()
    await ctx.send(f'||{" ".join(args)}||')
    log(ctx, args)

@bot.command()
async def bonk(ctx, mention, *args):
    if mention != ctx.message.mentions[-1].mention: return
    await ctx.message.delete()
    try: times = int(args[0]); args = args[1:]
    except ValueError: times = 1
    for n in range(0, times): await ctx.send(f'{mention} *bonk*')
    if args: await ctx.send(" ".join(args))
    else: await ctx.send(choice(bonkGifs)); args = ' '
    log(ctx, args=[mention, str(times), " ".join(args)])

@bot.command()
async def say(ctx, *args):
    if ctx.author.id == MY_ID:
        await ctx.message.delete()
        await ctx.send('{}'.format(' '.join(args)))
        log(ctx, args)

bot.run(TOKEN)
