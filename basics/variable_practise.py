import sys


class Bank:
    bank_name = "Lloyds Bank"

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print(f"Your new balance is {self.balance}")

    def withdrawal(self, withdrawal_amount):
        if self.balance < withdrawal_amount:
            print("You don't have sufficient fund, try with lower amount")
        else:
            self.balance = self.balance - withdrawal_amount

    def check_balance(self):
        print(f"your current balance is {self.balance}")


customer_name = input("What is your name?")
customer1 = Bank(customer_name)

while True:
    choices = input("D-Deposit\nW-Withdrawal\n" +
                    "C-Check Balance\nE-Exit\n").lower()
    if choices == "d":
        deposit_amount = float(input("How much you want to deposit?"))
        customer1.deposit(deposit_amount)
    elif choices == "w":
        withdrawal_amount = float(input("How much you want to withdraw?"))
        customer1.withdrawal(withdrawal_amount)
    elif choices == "c":
        customer1.check_balance()
    elif choices == "e":
        print(f"Thank you for banking with {Bank.bank_name}")
        sys.exit()
