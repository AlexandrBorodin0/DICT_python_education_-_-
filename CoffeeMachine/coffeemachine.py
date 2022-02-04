class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.run = True

    def action(self, action):
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()
        elif action == "exit":
            self.run = False
        else:
            raise NotImplementedError(action)

    def buy(self):
        drink = int(input(f"What do you want to buy? (1: espresso, "
                          f"2: latte, 3: cappuccino, 4: back to main menu):\n> "))
        if drink == 4:
            return
        elif drink == 1:
            if self.check(250, 0, 16, 1) == "None":
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.milk -= 0
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                self.check(250, 0, 16, 1)
        elif drink == 2:
            if self.check(350, 75, 20, 1) == "None":
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            else:
                self.check(350, 75, 20, 1)
        elif drink == 3:
            if self.check(200, 100, 12, 1) == "None":
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                self.check(200, 100, 12, 1)
        else:
            print("Invalid input")

    def check(self, water, milk, beans, cups):
        if self.water - water < 0:
            print("Sorry, not enough water")
        elif self.milk - milk < 0:
            print("Sorry, not enough milk")
        elif self.beans - beans < 0:
            print("Sorry, not enough coffee beans")
        elif self.cups - cups < 0:
            print("Sorry, not enough disposable cups")
        else:
            return "None"

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups do you want to add:"))

    def take(self):
        print(f"I'v gave you {self.money}")
        self.money = 0

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


def main():
    coffee = CoffeeMachine()
    while coffee.run:
        user = input("Write action (buy, fill, take, remaining, exit):\n> ")
        coffee.action(user)


if __name__ == '__main__':
    main()
