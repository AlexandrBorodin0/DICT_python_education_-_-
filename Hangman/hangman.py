import random


print("HANGMAN")
lists = ["python", "java", "javascript", "php"]
win_word = random.choice(lists)
clue_spaces = "-" * (len(win_word) - 3)
clue_letters = "".join(list(win_word)[0:3])
user = input(f"Guess the word {clue_letters + clue_spaces}:> ")
if user == win_word:
    print("You survived!")
else:
    print("You lost!")
