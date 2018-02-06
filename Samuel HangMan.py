import random

Word_bank = ["redbaby", "mcdonalds", "edison", "gaston", "addams", "CONTROL Z",
             "san fransisco 49ers", "do you know da wae", "atlanta falcons", "raiders are haters"]
length = len(Word_bank)
range(11)
range(len(Word_bank))

randomWords = random.choice(Word_bank)
Guesses_left = 10
letters_guessed = [' ']
user_input = ""
win = False
print("You have 10 guesses to win")

while Guesses_left > 0 and not win:  # while user_input != "quit":
    output = []
    for letter in randomWords:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    print(Guesses_left)

    if output == list(randomWords):
        print("You win")
        win = True
        continue

    user_input = input("Type in a letter: ")
    letters_guessed.append(user_input)
    print(letters_guessed)

    if user_input not in list(randomWords):
        print("Guess again")
        Guesses_left -= 1
