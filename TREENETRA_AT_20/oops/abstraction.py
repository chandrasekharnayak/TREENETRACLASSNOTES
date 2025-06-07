'''its a core part of oops, that hides the internal implimentation details and only expose the essential features of an object'''

'''abstract class and abstract method using abc module'''

'''why do we need abstraction


1.Hides complexity
2.Improves security
3.Enhance maintainbility'''

'''Use abstraction

1.Use the abc module
2.Import ABC and abstractmethod
3.Create an abstract class(inherits from ABC)
4.Define one or more abstract methods(@abstractmethod)
5.A subclass(child-class) must implement all abstract methods

'''

'''
Savings Accounts
Current Accounts

    create_account(),get_balance(), calculate_interst()
'''

from abc import ABC,abstractmethod

class BankAccount(ABC):

    def __init__(self,account_number,balance = 0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def calculate_intrest(self):
        pass

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):

    def create_account(self):
        print(f'saving Account {self.account_number} created with balance :- {self.balance}')

    def calculate_intrest(self):
        interest = self.balance*0.04
        print(f'Intrest on saving account {self.account_number}:- {interest} rs')
        return interest


class CurrentAccount(BankAccount):

    def create_account(self):
        print(f"Current account {self.account_number}  created with balance :- {self.balance}")

    def calculate_intrest(self):
        # print("No interest  for current account")
        interest = self.balance * 0.05
        print(f'Intrest on current account {self.account_number}:- {interest} rs')
        return 0


savings = SavingsAccount('SA123',1000)
savings.create_account()
savings.calculate_intrest()
print('Balance of savings account :- ',savings.get_balance())

print()

current = CurrentAccount('CA123',10000)
current.create_account()
current.calculate_intrest()
print('Balance of savings account :- ',current.get_balance())





















