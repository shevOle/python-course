print(type(20) != int)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'\nAccount owner: {self.owner}.\nBalance: ${self.balance}\n'

    def deposit(self, sum):
        if (type(sum) != int and type(sum) != float) or sum < 0:
            return print('Deposit sum must be an integer greater than 0, nothing will be added.')
        
        self.balance += +sum
        print(f'${sum} was added. New balance: ${self.balance}')

    def withdraw(self, sum):
        if (type(sum) != int and type(sum) != float) or sum < 0:
            return print('Withdraw sum must be an integer greater than 0, nothing will be deducted.')
        
        if sum > self.balance:
            return print(f'Withdraw sum can not be greater, that balance. Current balance: ${self.balance}')
        
        self.balance -= +sum
        print(f'${sum} was withdrawn. New balance: ${self.balance}')

new_acc = Account('Diego')
print(new_acc)

new_acc.withdraw(1)
print()

new_acc.deposit('aaa')
print()

new_acc.deposit(-20)
print()

new_acc.deposit(20)
print()

new_acc.withdraw(-1)
print()

new_acc.withdraw('aaa')
print()

new_acc.withdraw(40)
print()

new_acc.withdraw(19)
print()

new_acc.deposit(20)
print()

print(new_acc)