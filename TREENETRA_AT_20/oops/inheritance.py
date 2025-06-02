#inheritance
'''
what is inheritance?
A child class inheritance to the parent class, and child is capabale use all the behaviour of parent


use case of inheritance?

we will use inheritnace for the code optimization, and avoid unessary writing the codes and avooid the duplicates function and functionalities
'''

# class A: #parent class
#
#     a = 10
#
#     def f1(self):
#         pass
#
#
#
# class B(A):# child class
#
#     b = 10
#
#     def f2(self):
#         pass
#
# obB = B
# obB.

#types of inheritance?
'''
1.Single inheritance:- one parent class , called in one child class.
2.Multiple inheritance
3.Multilevel inheritance
4.Hyreichical inheritance
'''

'''class School:

    def __init__(self,school_name):
        self.school_name = school_name

    def class_8(self,sec_a,sec_b,sec_c):
        self.sec_a =sec_a
        self.sec_b = sec_b
        self.sec_c = sec_c
        return self.sec_a+self.sec_b+self.sec_c

    def get_info(self):
        print(f'school name {self.school_name}, total student of class 8 :-{self.sec_a+self.sec_b+self.sec_c}')



class Std9(School):
    def __init__(self,new_admission,school_name):
        self.new_admission=new_admission
        super().__init__(school_name)

    def class_9(self):
        class_8_students_count = super().class_8(35,42,37)
        self.total_students_of_class_9 = self.new_admission+class_8_students_count
        return self.total_students_of_class_9

    def get_info(self):
        print(f'school name {self.school_name}, total student of class 9 :-{self.total_students_of_class_9}')
        print(f'class 8 students count :-  {super().class_8(35,42,37)}')





# scl = School('Sri aurobindo')
# scl.class_8(35,42,37)
# scl.get_info()

std9 = Std9(14,'Sri aurobindo')
std9.class_9()
std9.get_info()'''




#super() :- parent class all beheviour use to child class with method, variable and constrctor


#Multiple inheritance :- one child class have multiple parent class.


'''class A:#parent1
    def f1(self):
        print('class A f1')


class B:#parent2
    def f1(self):
        print('class B f1')


class C:#parent3
    def f1(self):
        print('class c f1')

class D(B,A,C):#Child

    def f2(self):
        print('class D f1')

objd = D
objd.f1('bh')'''

#MRO :- Method resolution order use in multiple inheeritance


#Bank application

'''
3 parent class (BankAccount, customerinfo, KYC verification)
BankAccount :- Handel account creation
customerinfo :- stores customer detils
Kyc :- Handel KYC check

1. child ( Final account)

Final account :- combimnes everything- intilizes account,...

super() for chaining 

MRO


'''
#
# class BankAccount:
#     def __init__(self):
#         super().__init__()
#         self.account_type ='Saving'
#         self.account_numvber = 1000000
#         self.apply_date = '20-08-2024'
#
#
#     def account_details(self):
#         print('Bank account detials')
#         print(f'Account Type :- {self.account_type}, Account number :- {self.account_numvber}, Apply date :- {self.apply_date}')
#
#
#
# class CustomerInfo:
#     def __init__(self):
#         super().__init__()
#         self.name = 'satyajit'
#         self.balance = 10000
#
#     def customer_details(self):
#         print(f'Customer details :- {self.name}, Balance :- {self.balance}')
#
#
# class KYCVerification:
#     def __init__(self):
#         super().__init__()
#         self.kyc_status = 'verified'
#
#     def kyc_detils(self):
#         print(f'kyc status :- {self.kyc_status}')
#
#
# class AccountActivation(BankAccount,CustomerInfo,KYCVerification):
#     def __init__(self,):
#         super().__init__()
#         self.branch = 'Bbsr'
#
#     def full_details(self):
#         print('\n Final count :- fetching all details')
#         print(f'Account Type :- {self.account_type}')
#         print(f'Account number {self.account_numvber} and apply date :-{self.apply_date}')
#         print(f'Customer information :- {self.name}')
#         print(f'Current balance:- {self.balance}')
#         print(f'Kyc status :- {self.kyc_status}')
#         print(f'Barnch :- {self.branch}')
#
#
#
# ob = AccountActivation()
# ob.full_details()


#multilevel inheritance

# class Grandpa:
#     15ac -- area
#
#
# class GrandMother:
#     20ac-- area
#
# class Father(Grandpa,GrandMother)
#     10ac -- area
#
# class Uncle(Grandpa,GrandMother)
#
#
# class son(Father):
#     8ac --- area
#
#
# class Grandson(son):
#     10ac -- area


'''class Animal:
    def sound(self):
        print('Animal  make a differnt sounds')


class Dog(Animal):
    def brak(self):
        print('Dogs branks')


class Puppy(Dog):
    def weep(self):
        print('Puppy weep')


p = Puppy()


p.sound()
p.weep()
p.brak()'''

#Telecom CRM
'''
we are bulding a crm system for a telecom company

There are Customerm PostPaidCustomer, and PremiumPostPaidCustomer  classes

customer :- Base class with basic customer details

PostPaidCustomer :- inherits fronm customer, adss postpaid- specfic deatils like billing

PremiumPostPaidCustomer:- inherits fronm PostPaidCustomer,adds premoium benifits

'''



class Customer:

    def __init__(self,name,mobile):
        self.name = name
        self.mobile = mobile

    def display_details(self):
        print(f"Customer Name :- {self.name}")
        print(f"customer mobile number :- {self.mobile}")



class PostPaidCustomer(Customer):
    def __init__(self,name,mobile,plan,balance):
        super().__init__(name,mobile)
        self.plan = plan
        self.balance = balance

    def check_balance(self):
        print(f"Current Balance :- {self.balance}")
        print(f"Plan :- {self.plan}")



class PremiumPostPidCustomer(PostPaidCustomer):
    def __init__(self,name,mobile,plan,balance,loyality_points):
        super().__init__(name,mobile,plan,balance)
        self.loyality_points = loyality_points

    def premium_benifits(self):
        print(f'Loyalty Points :- {self.loyality_points}')
        print('Access to premium  loung and priority customer support')


class PrePaidCustomer(Customer):
    def __init__(self,name,mobile,balance,charges):
        super().__init__(name,mobile)
        self.balance= balance
        self.charges = charges

    def balance_deducation(self,use_per_min):
        charges_deduction = use_per_min*self.charges
        self.balance = self.balance-charges_deduction
        print(f'after use {use_per_min}mints balance check:- {self.balance}')



class BroadBandUser(Customer):
    def __init__(self,name,mobile,broadband_id,total_data):
        super().__init__(name,mobile)
        self.broadband_id= broadband_id
        self.total_data = total_data


    def wifi_user(self,data_usage):
        current_data = self.total_data-data_usage
        print(f'current data avl for customer {self.name} and avl data is {current_data}')

# customer1 = PremiumPostPidCustomer("Biswajit","1234567890","Platinum plan",500,1200)
# customer1.display_details()
# customer1.check_balance()
# customer1.premium_benifits()


# customer2 = PrePaidCustomer('Gyana','0987654321',500,1)
# customer2.display_details()
# customer2.balance_deducation(60)

customer3 = BroadBandUser('Isik','12345566644','airtel_133442',500)
customer3.wifi_user(200)


# Ploymerprisim
# Encapsulation
# Abstraction
# Multiprocess and multithereading

SDET
SDEDF

Dev-- AI

Testing-- en


















