def welcome():
    print("Hello! My name is Hagrit.")
    print("I was created in 2021.")
    print("Please, remind me your name.")
    name = input("> ")
    print(f"What a great name you have, {name}!")


def init():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3,5 and 7.")
    age_1 = int(input("> "))
    age_2 = int(input("> "))
    age_3 = int(input("> "))
    age = (age_1 * 70 + age_2 * 21 + age_3 * 15) % 105
    print(f"Your age is {age}; that's good time to start programming!")


def main():
    print("Now I will prove to you that I can count to any number you want")
    number = int(input("> "))
    for i in range(number + 1):
        print(f"{i}!")
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    test = 0
    while test != 2:
        user = int(input("> "))
        if user == 2:
            print("Completed, have a nice day!")
            print("Congratulations, have a nice day!")
            test = 2
        else:
            print("Please, try again.")


welcome()
init()
main()
