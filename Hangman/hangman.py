import random


print("HANGMAN")
lists = ["python", "java", "javascript", "php"]
win_word = list(random.choice(lists))
clue = list("-" * len(win_word))
print(''.join(clue))
for i in range(8):
    user_letter = input("Input a letter: ")
    if user_letter in win_word:
        if win_word.count(user_letter) >= 2:
            index = win_word.index(user_letter)
            clue[index] = user_letter
            win_word[index] = "-"
        index = win_word.index(user_letter)
        clue[index] = user_letter
    print(''.join(clue))
if win_word == clue:
    pass
else:
    print("That letter doesn't appear in the word")

print("\nThanks or playing!")
print("We'll se how well you did in next stage")
