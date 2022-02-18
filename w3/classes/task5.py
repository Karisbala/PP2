class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def show(self):
        return self.owner, self.balance
        
    def deposit(self, d):
        self.balance += d
        
    def withdraw(self, w):
        if w > self.balance:
            return False
        else:
            self.balance = self.balance - w

person = Account('Abzal', 1000)

print(person.show())

#deposit test
person.deposit(300)
print(person.show())

#withdrawl test
person.withdraw(200)
print(person.show())

#overdraw test
person.withdraw(2000)
print(person.show())