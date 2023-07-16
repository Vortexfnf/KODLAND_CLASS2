import random

Charpos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passw = ""

Passlen = int(input("Enter a password length for your password (8-26): "))
while Passlen < 8 or Passlen > 26:
    Passlen = int(input("Invalid password length. Pick a number between 8 and 26 for your randomly generated password: "))

if Passlen >= 8 and Passlen <= 26:
    for i in range(Passlen):
        random_char = random.choice(Charpos)
        passw += random_char

print("Your generated password is: " + passw)