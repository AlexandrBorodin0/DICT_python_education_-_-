import random


print("HANGMAN")
lists = ["python", "java", "javascript", "php"]
word = random.choice(lists)
win_word = list(word)
clue = list("-" * len(win_word))
null = []
print(''.join(clue))
for i in range(8):
    user_letter = input("Input a letter: ")
    if user_letter in null:
        print("No improvements")
    elif user_letter in win_word:
        if win_word.count(user_letter) >= 2:
            index = win_word.index(user_letter)
            clue[index] = user_letter
            win_word[index] = "-"
        index = win_word.index(user_letter)
        clue[index] = user_letter
    else:
        print("That letter doesn't appear in the word")
    print(''.join(clue))
    null.append(user_letter)
if (''.join(clue)) == word:
    print("You survived!")
else:
    print("You lost!")
