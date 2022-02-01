import random


print("HANGMAN")
lists = ["python", "java", "javascript", "php"]
win_word = random.choice(lists)
user = input("Guess the word:> ")
if user == win_word:
    print("You survived!")
else:
    print("You lost!")
