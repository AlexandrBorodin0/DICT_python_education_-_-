import random


print("HANGMAN\n")
lists = ["python", "java", "javascript", "php"]
word = random.choice(lists)
win_word = list(word)
clue = list("-" * len(win_word))
null = []
english_letters = list("qwertyuiopasdfghjklzxcvbnm")
print(''.join(clue))
attempts = 0
while attempts < 9:
    user_letter = input("Input a letter: ")
    if user_letter in null:
        print("You've already guessed this letter")
    elif user_letter in win_word:
        if win_word.count(user_letter) >= 2:
            index = win_word.index(user_letter)
            clue[index] = user_letter
            win_word[index] = "-"
        index = win_word.index(user_letter)
        clue[index] = user_letter
        attempts += 1
    elif len(user_letter) >= 2:
        print("You should input a single letter")
    elif user_letter not in english_letters:
        print("Please enter a lowercase English letter")
    elif user_letter not in win_word:
        print("That letter doesn't appear in the word")
        attempts += 1

    print("\n", ''.join(clue))
    null.append(user_letter)

if (''.join(clue)) == word:
    print("You survived!")
else:
    print("You lost!")
