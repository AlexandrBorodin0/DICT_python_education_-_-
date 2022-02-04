from math import ceil


principal = int(input("Enter the loan principal:\n> "))
print("What do you want to calculate?")


def monthly(months):
    payment = ceil(principal / months)
    print(f"It will take {payment} months to repay the loan")


def period(periods):
    period_payment = ceil(principal / periods)
    last_payment = principal - (periods - 1) * period_payment
    print(f"Your monthly payment = {period_payment}" if period_payment == last_payment
          else f"Your monthly payment = {period_payment} and the last payment = {last_payment}")


def main():
    user = input("type 'm' - for number of monthly payments,\n"
                 "type 'p' - for the monthly payment:\n> ")
    init(user)


def init(user):
    if user == "m":
        months = int(input("Enter the monthly payment:\n> "))
        monthly(months)
    elif user == "p":
        periods = int(input("Enter the number of months:\n> "))
        period(periods)
    else:
        print("You type incorrect word")
        main()


main()
