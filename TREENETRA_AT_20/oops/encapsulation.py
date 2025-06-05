'''
Encapsulation = Data hiding + Controlled Access

To hide internal details of how an object works?

To Protect data from unauthorized acees and modification

To enforce validation logic before allowimng chages


Access modifiers in pythin (By convention)

Public              variable                       Acessiable from anywhere-- inside or outside of the class

Protected           _variable                      Suggest internal use only --- but still accessible from ouside

Private             __variable                      Name mangled; not directly accessoible from ouside of the class


what is being Encapsulated?

Data (attributes/variables)
Behavior(methods/functions)

'''

#Public

'''class Students:
    def __init__(self,name):
        self.name = name  # public vaariable

st = Students('Deepka')
print(st.name)'''

#protected

'''class Vehicle:
    def __init__(self):
        self._speed = 60


class Car(Vehicle):
    def display_speed(self):
        print("Speed:-",self._speed)

car = Car()
car.display_speed() # correct
print(car._speed) # its also correct but not permitted'''\


#private

# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance #public
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount(5000)
# print(account.get_balance())
# # print(account.__balance)
# # print(account._BankAccount__balance)

#Bank Project


# class BankAccount:
#
#     def __init__(self,balance):
#         self.__balance = balance  # private variable
#
#     def deposite(self,amount):
#         if amount>0:
#             self.__balance +=amount
#
#     def withdraw(self,amount):
#         if 0< amount <= self.__balance:
#             self.__balance-=amount
#         else:
#             print('Invalid withdrawl amount')
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount(5000)
#
# account.deposite(500)
# account.withdraw(200)
#
# print('Balance check',account.get_balance())
# print(account.__balance)


class Bank:
    def __init__(self,balance):
        self.balance = balance


class Emp1(Bank):
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self, amount):

        if amount>0:
            self.__balance +=amount

    def withdraw(self,amount):
        if 0< amount <= self.__balance:
            self.__balance-=amount
        else:
            print('Invalid withdrawl amount')

    def get_balance(self):
        return self.__balance


emp1 = Emp1(1000)
emp1.deposite(500)
print(emp1.get_balance())
emp1.__balance

class Emp2(Emp1):

    def display_emp1_salary(self):
        return Emp1.__balace

emp2 = Emp2
print(emp2.display_emp1_salary('j'))

# class Emp3(Bank):
#     def __init__(self,balance):
#         self.__balance = super().__init__(balance)

