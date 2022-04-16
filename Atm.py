class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    
    def checkBalance(self):
        print("Your balance is $50,000")

    def cashWithdrawal(self, amount):
        if(amount <= 50000):
            new_amount = 50000 - amount
            print("You have withdrawn: " + str(amount) + " Your remaining balance is: " + str(new_amount))
        else:
            print("You cannot withdrawal this much. Please withdrawal a smaller amount of cash.")

def main():
    name = input("Hello there! What is your name? ")
    print("Hello, " + name + "!")
    cardNumber = input("Please enter your card number: ")
    # use 1234 for the pin!!
    pin = input("Enter your pin (4-digits): ")
    if(pin == "1234"):    
        new_user = Atm(cardNumber, pin)

        print("Please make a selection from the menu below.")
        print("1. Savings Balance")
        print("2. Cash Withdrawal")
        selection = int(input("Enter the activity number: "))

        if(selection == 1):
            new_user.checkBalance()

        elif(selection == 2):
            print("Your total savings balance is $50,000")
            amount = int(input("Enter the amount of money you would like to withdrawal: "))
            new_user.cashWithdrawal(amount)

        else:
            print("Please enter a valid number")

    else:
        print("The pin you entered is incorrect. Please enter the correct pin.")

main()