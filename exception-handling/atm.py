def deposit(money):
    # prompt for a deposit and validate input
    try:
        amount = float(input("Enter an amount to deposit: "))

        if amount <= 0:
            raise Exception("Amount can't be negative")

        # add the deposit amount to the money balance
        return money + amount
    except Exception as e:
        print("That's an invalid amount", str(e))
        return money # unmodified money


def withdraw(money):
    # prompt for a withdraw and validate input
    try:
        amount = float(input("Enter an amount to withdraw: "))

        if amount <= 0 or amount > money:
            raise Exception("Amount can't be negative or greater than available money")
        
        # subtract the withdraw amount from the money balance
        return money - amount
    except Exception as e:
        print("That's an invalid amount", str(e))
        return money # unmodified money

def check_balance(money):
    print("Your balance is $", money)


def main():
    money = 1000

    while(True):
        option = input("Select an Option: \n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n\nSelect: ")

        if option == "1":
            money = deposit(money)

        elif option == "2":
            money = withdraw(money)

        elif option == "3":
            check_balance(money)

        elif option == "4":
            print("Thank you for using our ATM")
            break

        else:
            print("Invalid Choice")

        print()


main()