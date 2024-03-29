class Account():
    owner = ""
    balance = 0

    def __init__(self, owner, balance):
        self.owner = owner 
        self.balance = balance

    def __str__(self):
        return f"Owner of an account is: {self.owner}\nAccount balance is: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return "The deposit has been made"

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            return "Withdraw accepted"
        else:
            return "Withdraw can not be accepted"


acc1 = Account("Maxim", 5000)

print(acc1)
print(acc1.deposit(100))
print(acc1.withdraw(50))
print(acc1.balance)