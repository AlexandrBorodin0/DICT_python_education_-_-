print("HANGMAN")
win_word = "python"
user = input("Guess the word:> ")
if user == win_word:
    print("You survived!")
else:
    print("You lost!")
