 #-User input
Word = input("Enter a word! this program will detect if it's a palindome or not.")

 #-Convert into lowercase
Word = Word.lower().replace(" ", "")

 #-Reverse the word
reversed_word = Word[::-1]

 #-Checking
if Word == reversed_word:
    print("This word is a palindrome!")
else:
    print("This word is not a palindrome!")