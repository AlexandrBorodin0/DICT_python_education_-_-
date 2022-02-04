import random


def main():
    try:
        count = int(input("Enter the number of friends joining (including you):\n> "))
        message = "\nNo one is joining your party"
        assert count > 0, message

        friends_list = [input("Enter the name of every friends (including you), "
                              "each on a new line:\n> ") for _ in range(count)]

        total = int(input("Enter the total amount\n> "))

        lucky = input("Do you want yo use the 'Who is lucky?' feature? Write Yes/No:\n> ")
        message = "\nYou should enter Yes or No!"
        assert lucky in ["Yes", "No"], message

        if lucky == "Yes":
            amount = round((total / count - 1), 2)
            friends_dict = dict.fromkeys(friends_list, amount)
            lucky_dict = random.choice(friends_list)
            print(f"{lucky_dict} is the lucky one!\n")
            friends_dict[lucky_dict] = 0
        else:
            print("No one is going to be lucky")
            amount = round((total / count), 2)
            friends_dict = dict.fromkeys(friends_list, amount)
        print(friends_dict)
    except ValueError:
        print("You should enter numbers!")
    except AssertionError as error:
        print(error)


if __name__ == '__main__':
    main()
