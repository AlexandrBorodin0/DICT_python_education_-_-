water = 200
milk = 50
beans = 15

print("Write how many ml water the coffee machine has:")
user_water = int(input("> "))
print("Write how many ml milk the coffee machine has:")
user_milk = int(input("> "))
print("Write how many grams of coffee beans the coffee machine has:")
user_beans = int(input("> "))
print("Write how many cups of coffee you  will need:")
user_cups = int(input("> "))


def main():
    many_w = user_water // water
    many_m = user_milk // milk
    many_b = user_beans // beans
    if many_w * many_m * many_b == 0:
        cups = 0
    else:
        cups = min(many_w, many_m, many_b)

    difference_cups = cups - user_cups

    if user_cups == cups:
        print("Yes, I can make that amount of coffee")
    elif user_cups >= cups:
        print(f"No, I can make only {cups} cups of coffee")
    else:
        print(f"Yes, I can make that amount of coffee (and even {difference_cups} more than that)")


main()
