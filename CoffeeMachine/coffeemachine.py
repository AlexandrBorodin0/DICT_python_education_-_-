water = 400
milk = 540
beans = 120
cups = 9
money = 550


def espresso():
    water_espresso = water - 250
    milk_espresso = milk
    beans_espresso = beans - 16
    cups_espresso = cups - 1
    money_espresso = money + 4
    init(water_espresso, milk_espresso, beans_espresso, cups_espresso, money_espresso)


def latte():
    water_latte = water - 350
    milk_latte = milk - 75
    beans_latte = beans - 20
    cups_latte = cups - 1
    money_latte = money + 7
    init(water_latte, milk_latte, beans_latte, cups_latte, money_latte)


def cappuccino():
    water_cappuccino = water - 200
    milk_cappuccino = milk - 100
    beans_cappuccino = beans - 12
    cups_cappuccino = cups - 1
    money_cappuccino = money + 6
    init(water_cappuccino, milk_cappuccino, beans_cappuccino, cups_cappuccino, money_cappuccino)


def fill():
    wat = (input("Write how many ml of water you want to add:")) + water
    mil = (input("Write how many ml of milk you want to add:")) + milk
    bean = (input("Write how many grams of coffee beans you want to add:")) + beans
    cup = (input("Write how disposable coffee cups you want to add:")) + cups
    init(wat, mil, bean, cup, money)


def take():
    print(f"I gave you {money}")
    money_take = 0
    init(water, milk, beans, cups, money_take)


def init(w, m, b, c, mon):
    print(f"The coffee machine has:\n{w} of water")
    print(f"{m} of milk\n{b} of coffee beans")
    print(f"{c} of disposable cups\n{mon} of money")


def main():
    user = input("Write action (buy, fill, take):\n> ")
    if user == "buy":
        buy = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
        if buy == 1:
            espresso()
        elif buy == 2:
            latte()
        elif buy == 3:
            cappuccino()
        else:
            print("Invalid input")
    elif user == "fill":
        fill()
    elif user == "take":
        take()
    else:
        print("Invalid input")


main()
