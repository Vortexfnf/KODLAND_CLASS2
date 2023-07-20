import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import random_emoji

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot has logged in on discord as {client.user}')

@client.command()
async def Genpass(ctx, passwlenght = 8):
    await ctx.author.send("Your password is: " + gen_pass(passwlenght))

@client.command()
async def Hello(ctx):
    await ctx.send("Hello user!")

@client.command()
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    quit()

@client.command()
async def randemoji(ctx, emoji_count = 1):
    await ctx.send(random_emoji(emoji_count))

@client.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@client.command()
async def hehe(ctx, count_hehe = 5):
    await ctx.send("hehe" * count_hehe)

client.run("MTEyOTA5MjQ5NzIzMTA2OTI0NA.GQwncc.6X-PWV4FR5Z4FzmBdahsxw52xUmAVkHA1eT_6M")