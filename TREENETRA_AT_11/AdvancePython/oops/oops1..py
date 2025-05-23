# class Students:
#     '''This class written for store the students information'''
#     pass
#
# # print(dir(Students))
# # print(Students.__dict__)
# # object_reference
#
# obj1 = Students
# obj2 = Students
#
# a = 900
# b = 900
#
# print(type(a))
#
# # print(id(a))
# # print(id(b))
#
# li = [10,20,30]
# li.append(70)
#
# li2 =[10,20,30]
# li2.append(80)




#create the constructor

# class Students:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def f1(self):
#         print(self.name)
#
#
# obj_ref = Students('Rohan',27)
# print(obj_ref.__dict__)
# obj_ref.f1()


# class ClassRoom:
#     def __init__(self,copy):
#         self.copy = copy
#
#     def bench_1(self,data_benche1):
#         self.data_benche1 = data_benche1
#
#     def bench_2(self,data_bench2):
#         self.data_bench2 = data_bench2
#
#
# obj_refrence = ClassRoom('Omm Therom')
# obj_refrence.bench_1('data1 of bench 1')
# obj_refrence.bench_2('data2 of bench 2')
# obj_refrence.bench_3='None'
# print(obj_refrence.__dict__)

'''Bank
account_number
account_balance

deposite--- balance

withdraw --- balance

# check the balance'''
#
# class BankOfPython:
#     def __init__(self,acc_num,acc_balance):
#         self.acc_num = acc_num
#         self.acc_balance = acc_balance
#
#     def deposite(self,depo_amount):
#         self.depo_amount = depo_amount
#         self.acc_balance = self.acc_balance+self.depo_amount
#         return self.acc_balance,self.depo_amount
#
#     def withdraw(self,withdraw_amount):
#         self.withdraw_amount = withdraw_amount
#         # del self.withdraw_amount
#         self.acc_balance = self.acc_balance- self.withdraw_amount
#         return self.acc_balance,self.withdraw_amount
#
#     def check_acc_balance(self):
#         return self.acc_num,self.acc_balance
#
#
# obj_bank = BankOfPython(10287356346,456)
# # print(obj_bank.__dict__)
#
# #
# # obj_bank.ifsc = 2345678
# print(obj_bank.deposite(200))
# print(obj_bank.withdraw(500))
# print(obj_bank.check_acc_balance())
# del obj_bank.withdraw_amount
# print(obj_bank.__dict__)

#class method and static variable

#stastic var == global var
'''inside a class and outside of the function when a variable is declared , know as static var.

1.insider instance method  by using self or classname.
2.inside constructor by using self or classname
3.inside a class method usring either cls var or class name
'''
# class A:
#
#     a = 10#static var
#
#     def __init__(self):
#         print(self.a)
#         print(A.a)
#
#     def f1(self):
#         print(A.a)
#         # print(self.a)
#
#
# obj = A()
# # obj.f1()


# class B:
#
#     a = 10
#
#     @classmethod
#     def f1(cls):
#         a = 60
#         b = 70
#         result = a+b+cls.a
#         print(result)
#
# obj = B()
# obj.f1()


#Same question static variable and class method


# class BankOfPython:
#
#     account_number = 1234567890
#     account_balance = 500
#
#     @classmethod
#     def deposite(cls,depo_amount):
#         cls.account_balance = cls.account_balance+depo_amount
#         print(f'depo amount:- {depo_amount}:--After deposite account balance is :- {cls.account_balance}')
#
#     @classmethod
#     def withdraw(cls,withdraw_amount):
#         if withdraw_amount<=cls.account_balance:
#             cls.account_balance=cls.account_balance-withdraw_amount
#             print(f'withdrar amount :-{withdraw_amount}---After withdraw account balance is :- {cls.account_balance}')
#         else:
#             print(f'Not Enough amount:- amount left is {cls.account_balance}')
#
#
# obj = BankOfPython()
# obj.deposite(700)
# obj.withdraw(1300)

#Local Variable and staticmethod

#
# class A:
#
#     @staticmethod
#     def add(a,b):
#         global sum1
#         sum1 = a+b
#         return sum1
#
#     @staticmethod
#     def prod(a,b):
#         mul = a*b*sum1
#         return mul
#
# obj = A()
# print(obj.add(10,20))
# print(obj.prod(1,2))


'''Query:-
I have bus bus travel from Pune to Mumbai
Bus Name :- Amravati
Seats avl = 100
price of seat = 100rs
cancelation fee = 25rs 
sunday ----- 7pm
booking start from Friday

Friday
Morning 41-- booked
eveng 17-- booked ---- 11-- cancelled

Saturday
Morning 25 seats booked --- 5 setas cancel
Evening -- 10 seats booked

Sundays 
Morninmg 15 seats booked and 3 seats -- cancel

Sunday evening -- bus left

1.How many seats booked when bus will dep.
2.How many seats left when bus will dep.
3.Total Collection amount (with each day)
4.How many seats cancelled by public
5.How mouch amount collect by cancelation fee

'''
#inhheritance

# class A:
#
#     def f1(self):
#         print('Function F1')
#     def f2(self):
#         print('Function F2')
#
#
# class B(A):
#
#     def f3(self):
#         print('Function F3')
#     def f4(self):
#         print('Function F4')
#
#
# obj_a = A()
# obj_b  = B()

# obj_a.f1()
# obj_a.f2()
# obj_a.f3()

# obj_b.f3()
# obj_b.f1()
# obj_b.f2()

'''
class A:

    def f1(self):
        print('Function1')

    def f2(self):
        print('Function2')

class B(A):

    def f3(self):
        print('Function3')

    def f4(self):
        print('Function4')

obj_a = A()
obj_b = B()

obj_a.f1()
obj_a.f2()
# obj_a.f3()

obj_b.f4()
obj_b.f1()'''

'''import math
class Math:

    def __init__(self,height,length):
        self.height = height
        self.length = length

    def rectrangle(self):
        return self.height*self.length

class Math2(Math):

    def __init__(self,height,length,radius):
        self.radius = radius
        super().__init__(height,length)

    def suqre(self):
        rectrangle_data = super().rectrangle()
        rec_squre = rectrangle_data**2
        return rec_squre

    def circle(self):
        return 2*math.pi*(self.radius)**2


obj_math2 = Math2(10,5,2)
print(obj_math2.suqre())'''
# print(obj_math2.circle())
# print(obj_math2.rectrangle())


#Multiple Inhheritance
'''
class Math:
    def addtition(self,a,b):
        self.a = a
        self.b = b
        add= self.a +self.b
        return add

class Math2:
    def substraction(self,a,b):
        self.a = a
        self.b = b
        sub = self.a - self.b
        return sub

class Math3(Math,Math2):
    def mul(self):
        add =super().addtition(10,20)
        sub = super().substraction(50,70)
        mul = add*sub
        return mul

obj_math3 = Math3()
print(obj_math3.mul())'''


#Polymerprisim

# method overrding is possiable

'''class A:

    def f1(self):
        print('Function 1')

class B(A):

    def f1(self):
        print('Function 1 from class B')

obj = B()
obj.f1()'''

'''class A:

    def f1(self):
        print('Function 1  from class A')

class B:

    def f1(self):
        print('Function 1 from class B')

class C(B,A):
    pass

obj = C()
obj.f1()'''

#single and multiple inhheritance and Polymerprisim

#Multilevel Inhheritance

'''GrandFather--- Property

Father -- (GF) ----FProerty

Son(Fa)--- GP---- FP

Son Of Son -- (son)--GP--FP--SP'''


'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print('Name:-',self.name)
        print('Age:-',self.age)

class Doctor(Person):
    def __init__(self,name,age,specilization):
        self.specilization=specilization
        super().__init__(name,age)

    def display_info(self):
        super().display_info()
        print('Specilization',self.specilization)

class Surgen(Doctor):
    def __init__(self,name,age,specilization,exp):
        super().__init__(name,age,specilization)
        self.exp = exp

    def display_info(self):
        super().display_info()
        print('Experience (Years):-',self.exp)


obj_surgeon = Surgen('Ashutosh',28,'Ortho',5)
obj_surgeon.display_info()'''


#class A -- f1 and f2

# want create class B and class B f1 method in f3 .

# class A:
#
#     def f1(self):
#         print('Function1')
#
#     def f2(self):
#         print('Function2')
#
# class B(A):
#     def f3(self):
#         return super().f1()
#
# obj = B()
# obj.f3()

# Hirechical Inhheritance

'''Fater ---- FP ----- 2sons 2 da
200CR
Father()

Son1(Father)

Son2(Father)

Da1(Father)

Da2(Father)'''



'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print('Name:-',self.name)
        print('Age:-',self.age)

class Nurse(Person):
    def __init__(self,name,age,dept):
        self.dept = dept
        super().__init__(name,age)

    def display_info(self):
        super().display_info()
        print('Department:-',self.dept)

class Receptionist(Person):
    def __init__(self,name,age,shift):
        self.shift = shift
        super().__init__(name, age)

    def display_info(self):
        super().display_info()
        print('Department:-', self.shift)

nurse_obj = Nurse('Abhijeet','26','Ortho')
# nurse_obj.display_info()
rept_obj = Receptionist('Abhijeet','26','2nd')
rept_obj.display_info()'''

'''Basic
Intro
Identifie
keyword
data type
Data Strcture
Operator
Flow Control

ADV
Function
Module
Packages
File Handeling
Exception 
Logging
Oops'''

Monday --- Dev -- morning - 8:15am --- offline-- django
                    Testing -- Evening --8pm -- online- selenium -- pytest and robot































