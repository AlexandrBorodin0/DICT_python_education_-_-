friends_list = []


def main():
    try:
        count = int(input("Enter the number of friends joining (including you):\n> "))
        if count > 0:
            while count != 0:
                name_friends = input("Enter the name of every friends (including you), each on a new line:\n> ")
                friends_list.append(name_friends)
                count -= 1
            dict_friends = dict.fromkeys(friends_list, 0)
            print(dict_friends)
        else:
            print("No one is joining for the party!")
    except ValueError:
        print("You should enter numbers!")


if __name__ == '__main__':
    main()
