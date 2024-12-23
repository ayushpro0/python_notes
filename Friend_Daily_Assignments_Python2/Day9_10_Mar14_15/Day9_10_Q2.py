"""2.	Create BankAccount class
Specify initial amount in Bank account as 50000
Write functionality for 	showBalance()
			Deposit(amount)
			WithDrawl(amount)
Error to be handled if Withdraw amount is greater that available balance.
Appropriate Exception handling expected.
"""


class BankAccount:
    def __init__(self):
        self.amount = 50000

    def showBalance(self):
        print("Amount:", self.amount)

    def Deposit(self, amount):
        self.amount = self.amount + amount

    def WithDrawl(self, amt):
        self.amount = self.amount - amt


account1 = BankAccount()

account1.showBalance()

val = 60000
try:
    if val < account1.amount:
        account1.WithDrawl(val)
        account1.showBalance()

    else:
        raise Exception("amount is lesser than withdrawl value!!!")

except Exception as e:
    print(e)
