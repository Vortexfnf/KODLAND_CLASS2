import datetime
import os
import discord
import asyncio
import random
from discord.ext import commands
from bot_logic import *
intents = discord.Intents.default()
intents.message_content = True

# CLIENT
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Create an instance of the Guessing_Game class
game_instance = Guessing_Game()

@client.event
async def on_ready():
    print(f'Bot has logged in on discord as {client.user}')


@client.command()
async def Genpass(ctx, passwlenght = 8):
    await ctx.author.send("Your password is: " + gen_pass(passwlenght))

@client.command()
async def Hello(ctx):
    await ctx.send("Hello")

@client.command()
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    await client.close()

@client.command()
async def randemoji(ctx, emoji_count = 1):
    await ctx.send(random_emoji(emoji_count))

@client.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@client.command()
async def hehe(ctx, count_hehe = 5):
    await ctx.send("hehe" * count_hehe)

@client.command()
async def guess(ctx, player_guess=0):
    answer, response = game_instance.guess(player_guess)
    if response == "You got it right!":
        await ctx.send("You got it right!")
    elif response == "You got it wrong :(":
        await ctx.send(f"You got it wrong :( The correct answer was {answer}.")

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(title="User Info", color=member.color)

    # Check if member has an avatar and set the thumbnail accordingly
    if member.avatar:
        embed.set_thumbnail(url=member.avatar.url)
    else:
        embed.set_thumbnail(url=None)  # Set an empty thumbnail

    embed.add_field(name="Username", value=member.name, inline=True)
    embed.add_field(name="Nickname", value=member.nick, inline=True)
    embed.add_field(name="User ID", value=member.id, inline=False)
    embed.add_field(name="Status", value=str(member.status).title(), inline=True)

    # Convert joined_at and created_at dates to the desired format
    joined_at = member.joined_at.strftime('%d/%B/%Y')
    created_at = member.created_at.strftime('%d/%B/%Y')

    embed.add_field(name="Joined Server", value=joined_at, inline=False)
    embed.add_field(name="Joined Discord", value=created_at, inline=False)

    await ctx.send(embed=embed)


@client.command()
async def meme(ctx):
    meme_files = [
        'Memes/meme1.jpg',
        'Memes/meme2.jpg',
        'Memes/meme3.jpg'
    ]

    # Randomly select a meme file from the list
    selected_meme_file = random.choice(meme_files)

    # Open the selected meme file in binary read mode
    with open(selected_meme_file, "rb") as f:
        # Save the converted archive in this variable:
        meme = discord.File(f)

    # Send the image:
    await ctx.send(file=meme)

@client.command()
async def editme(ctx):
    msg = await ctx.send("10")  # Defines the message
    await asyncio.sleep(3.0)
    await msg.edit(content="40")

@client.event
async def on_message_edit(before, after):
    msg = f'**{before.author}** has edited their message from\n"{before.content}" to "{after.content}"'
    await before.channel.send(msg)

# Run the bot
client.run("MTEyOTA5MjQ5NzIzMTA2OTI0NA.G_kSHW.T-jjRLVaYJjRpirsDtNqqJTYLFq2q1s8WBj3s0")
