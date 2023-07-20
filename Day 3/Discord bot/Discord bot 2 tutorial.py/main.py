import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot has logged in on discord as {client.user}')

@client.command()
async def ping(ctx):
    await ctx.author.send("Pong!")
@client.command()
async def hello(ctx):
    await ctx.send("Hello user!")

@client.command()
async def discordbotend(ctx):
    quit()

client.run("MTEyOTA5MjQ5NzIzMTA2OTI0NA.GCYX1N.VD-D_CKw4jHLSVnHuNAMoJ2EeB3nlRp5l2bVtg") 