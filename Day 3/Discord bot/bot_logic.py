import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def random_emoji(ammount):
    emojissent = ""
    emojis = ["😄", "🙂", ":skull:", "👍", "🤨", "🎮", "🗿", "🥶", "🐬", "✨", "🐀", "💯", "🐠"]

    for i in range(ammount):
        emojissent += (random.choice(emojis))
        
    return emojissent

def flip_coin():
    coin = ["Heads", "Tails"]
    coin_flip = random.choice(coin)
    return coin_flip

class Guessing_Game:
    def __init__(self):
        self.response = ""

    def guess(self, p_gss):
        answer = random.randint(1, 10)
        if p_gss == answer:
            self.response = "You got it right!"
        else:
            self.response = "You got it wrong :("

        return str(answer), self.response