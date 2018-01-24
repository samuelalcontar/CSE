import random
"""
This is a guide of how to make hangman
1. Make a word bank - 10 items
2. select a random item to guess
3. take in a letter and add list if letters guessed
4. Hide and reveal letter
5. Create a win and lose condition
"""

Word_bank = ["redbaby", "mcdonalds", "edison", "gaston", "addams", "antidisestablishmentarianism " ,
             "san fransisco 49ers", "do you know da wae", "atlanta falcons", "raiders are haters" ]
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

length = len(Word_bank)
range(11)
range(len(Word_bank))

randomWords = random.choice(Word_bank)

user_input = input("Type in a letter: ")


user_input = ()
listOne = user_input
print(listOne)
print(listOne)
letters_guessed = [user_input]
print(letters_guessed)



