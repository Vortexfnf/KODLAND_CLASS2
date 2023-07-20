import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def random_emoji():
    emojis = ["😄", "🙂", ":skull:", "👍", "🤨", "🎮", "🗿", "🥶", "🐬", "✨", "🐀", "💯", "🐠"]
    return random.choice(emojis)

def flip_coin():
    coin = ["Heads", "Tails"]
    coin_flip = random.choice(coin)
    return coin_flip