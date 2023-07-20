import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import random_emoji
from settings import settings

# The intents variable stores the bot's priviliges
intents = discord.Intents.default()
# Enabling the message-reading privelege
intents.message_content = True
# Creating a bot in the client variable and transferring it the priveleges
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot has logged in on discord as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send(quit())
    elif message.content.startswith('$gen_pass'):
        await message.channel.send(gen_pass(15))
    elif message.content.startswith('$randemoji'):
        await message.channel.send("And the emoji is!!!")
        await message.channel.send("🥁🥁🥁")
        await message.channel.send(random_emoji())
    elif message.content.startswith('$coin_flip'):
        await message.channel.send(flip_coin())

client.run(settings["TOKEN"])