import discord
from discord.ext import commands
#  initializes a new bot object from the discord.py library  &&    let all Intents  use 
bot=commands.Bot(command_prefix='_',intents=discord.Intents.all())
bot.remove_command('help')

@bot.event # send when bot turns on
async def on_ready():
    print('logged in as'+bot.user.name+'!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

# commands
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello ! :)')

@bot.command(name='chiz')
async def ping(ctx):
    await ctx.send(f'miz! -> || {round(bot.latency *1000)} ms ||')

@bot.command(name='help')
async def help(ctx):
bot.run('MTEwMjI2NTI5NTIwMjE3MzAzOA.Go-aIS.IKWCrMCMamZZyj6XwQepq2w8w_7R-sNTqe1rYM')