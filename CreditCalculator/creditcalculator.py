from math import ceil, log, pow


def number_monthly():
    principal = float(input("Enter the loan principal:\n> "))
    monthly = float(input("Enter the monthly payment:\n> "))
    loan_interest = float(input("Enter the loan interest:\n> ")) / 1200
    summa = (monthly / (monthly - (loan_interest * principal)))
    number_ = ceil(log(summa, (1 + loan_interest)))
    year, month = divmod(number_, 12)
    if number_ % 12 != 0:
        print(f"It will take {year} years and {month} months to repay this loan!")
    elif number_ % 12 == 0:
        print(f"It will take {year} years to repay this loan!")
    else:
        print(f"It will take {month} months to repay this loan!")


def loan():
    a = float(input("Enter the annuity payment:\n> "))
    n = float(input("Enter the number of periods:\n> "))
    loan_interest = float(input("Enter the loan interest:\n> ")) / 1200
    summa = a / ((loan_interest * pow((1 + loan_interest), n)) / (pow((1 + loan_interest), n) - 1))
    print(f"Your loan principal = {round(summa)}!")


def annuity():
    principal = int(input("Enter the loan principal:\n> "))
    periods = int(input("Enter the number of periods:\n> "))
    loan_interest = int(input("Enter the loan interest:\n> ")) / 1200
    summa = principal * ((loan_interest * pow((1 + loan_interest), periods)) / (pow((1 + loan_interest), periods) - 1))
    print(f"Your monthly payment = {ceil(summa)}!")


def main():
    print("What do you want to calculate?")
    user = input("type 'n' for number of monthly payments,\n"
                 "type 'a' for annuity monthly payment amount,\n"
                 "type 'p' for the loan principal:\n> ")
    init(user)


def init(user):
    if user == "n":
        number_monthly()
    elif user == "p":
        loan()
    elif user == "a":
        annuity()
    else:
        print("You type incorrect word")
        main()


main()
