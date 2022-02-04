friends_list = []


def total(count):
    try:
        total_ = int(input("Enter the total amount\n> "))
        amount = round((total_ / count), 2)
        return amount
    except ValueError:
        print("You should enter numbers!")


def main():
    try:
        count = int(input("Enter the number of friends joining (including you):\n> "))
        if count > 0:
            while count != 0:
                name_friends = input("Enter the name of every friends (including you), each on a new line:\n> ")
                friends_list.append(name_friends)
                count -= 1
            amount = total(len(friends_list))
            dict_friends = dict.fromkeys(friends_list, amount)
            print(dict_friends)
        else:
            print("No one is joining for the party!")
    except ValueError:
        print("You should enter numbers!")


if __name__ == '__main__':
    main()
