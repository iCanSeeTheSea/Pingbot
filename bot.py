# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import choice
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MY_ID = os.getenv('MY_ID')

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


bot = commands.Bot(command_prefix='\\')

@bot.event
async def on_ready():
    print(f'{bot.user} is connected!')

@bot.command()
async def pingme(ctx):
    await ctx.send(f'hi {ctx.author.mention}!')

@bot.command()
async def stop(ctx):
    if ctx.author.id == [MY_ID]:
        exit()

@bot.command()
async def bonk(ctx, mention, *args):
    await ctx.message.delete()
    try: times = int(args[0])
    except ValueError: times = 1
    for n in range(0, times): await ctx.send(f'{mention} *bonk*')
    if args: await ctx.send('{}'.format(' '.join(args)))
    else: await ctx.send(choice(bonkGifs))

@bot.command()
async def say(ctx, *args):
    await ctx.message.delete()
    await ctx.send('{}'.format(' '.join(args)))

bot.run(TOKEN)