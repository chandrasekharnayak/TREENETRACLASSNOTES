#oops:- object oriented programming scripts.
# how to write a class and syntax of the class

'''
class class_name:
    statement
    def
    def
    def

3 types of function and 3 types of variable are present.
'''
from tkinter.font import names

from django.contrib.auth import aget_user

'''class Studnets:
    """this class is present by explain about the students information."""
    def std_info(self):
        pass
    def std_display(self):
        pass

object_reference = Studnets
print(dir(object_reference))'''

#constructor
'''
it is a special function in a class.
__init__
here have by default parameter name is self.
when class will execute in that time,aumaticlly constructor will exceute. and we will pass arg of cons.

#what is self.
self is by default parameter in cons and instance method.
it will vary from object to onject.
'''


'''class Std:

    def __init__(self,name,batch):
        self.name = name
        self.batch = batch


    def student_info(self):
        print(f'The name of the studnet is {self.name}')
        print(f'Batch is {self.batch}')

obj = Std('Ajit','AT#14')
obj.student_info()'''
# print(obj.__dict__)


# write generic class to display your academic roles.

'''class Name:
    def __init__(self,name,age,address):
        
    def 10
        
    def 12
        
    def graducation
    
    def pos
'''
#oops concept methods and variables
'''methods
there are 3 types of methods avl.
1.instance method
2.Class method
3.Static Method

3 types of variabel.
1.instance variable 
2.static variable
3.loacl variable

'''

# 1.instance method:- after declare the class, then we will create a generic method, that method automaticlly take self parameter, and which methid have the instance variable, that method consider as a instance method.
# 1.instance variable  :- who vary from object to objcet like self.

''''class Student:

    def __init__(self,school_name):
        self.school_name = school_name

    def class_info(self,class_data,class_name):
        self.class_data = class_data
        self.class_name = class_name
        print(f'{self.class_name} and about the class data :- {self.class_data} the school is {self.school_name}')

    def total_studnets(self,amount):
        self.amount = amount
        print(f'Total students :- {self.amount} and school name :- {self.school_name} and class 8th studnets {self.class_data} ')




obj = Student("DAV")
obj.class_info(60,'standard-8th')
obj.total_studnets(600)'''



'''BUS program:-
There is a bus name 'Galaxy'
Root :- Jaiput to Delhi
Bus have 100 seats
per seats :- 100rs
cancelation charge - 20rs


Monday morning :- 25 seats booked
Monday eveng :- 20 seats booked, 5 cancelled

tuesday morning :- 35 seats booked , 12 canclled
Tuesday eveng :- 37 seats booked, 2 canclled

1.Total booking tickets
2.Total cancel tickets
3.How much amount should be return
4.Left seats
5.Currently how many passenger travel.
6.total income.

25 ---  75
25*100 = 2500

ME
25+20 = 45
5 can = 
45-5 = 40
20*5  = 100
100*5 = 500
500-100 = 400
2500-400 = 2100


'''


'''class BusProgram:

    def __init__(self,bus_name,arv_location,depature_location,total_seats,per_seat_price,cancellation_charge):
        self.bus_name = bus_name
        self.arv_location= arv_location
        self.depature_location=depature_location
        self.total_seats=total_seats
        self.per_seat_price = per_seat_price
        self.cancellation_charge = cancellation_charge


    def monday_morning(self,book_seats,monday_morng_cancel_seats):
        self.monday_morng_cancel_seats = monday_morng_cancel_seats
        self.total_seats = self.total_seats-book_seats
        self.total_seats = self.total_seats+self.monday_morng_cancel_seats
        total_book_on_monday_morning = book_seats-monday_morng_cancel_seats
        total_price_of_book = total_book_on_monday_morning * 100 + monday_morng_cancel_seats * 20
        print(f'Monday morning total seats avl :- {self.total_seats}')
        print(f'Monday morning total booked seats :- {total_book_on_monday_morning}')
        print(f'Total amount :- {total_price_of_book}')
        return total_price_of_book

    def monday_eveng(self,book_seats,monday_eveng_cancel_seats):
        self.monday_eveng_cancel_seats = monday_eveng_cancel_seats
        self.total_seats = self.total_seats-book_seats
        self.total_seats = self.total_seats+monday_eveng_cancel_seats
        total_book_on_monday_eveng = book_seats-monday_eveng_cancel_seats
        total_price_of_book = total_book_on_monday_eveng * 100 + monday_eveng_cancel_seats * 20
        print(f'Monday eveng total seats avl :- {self.total_seats}')
        print(f'Monday eveng total booked seats :- {total_book_on_monday_eveng}')
        print(f'Total amount :- {total_price_of_book}')
        return total_price_of_book

    def tuesday_morning(self,book_seats,tuesday_morng_cancel_seats):
        self.tuesday_morng_cancel_seats = tuesday_morng_cancel_seats
        self.total_seats = self.total_seats-book_seats
        self.total_seats = self.total_seats+tuesday_morng_cancel_seats
        total_book_on_tuesday_morning = book_seats-tuesday_morng_cancel_seats
        total_price_of_book = total_book_on_tuesday_morning * 100 + tuesday_morng_cancel_seats * 20
        print(f'Tuesday morning total seats avl :- {self.total_seats}')
        print(f'Tuesday morning total booked seats :- {total_book_on_tuesday_morning}')
        print(f'Total amount :- {total_price_of_book}')
        return total_price_of_book

    def tuesday_eveng(self,book_seats,tuesday_eveng_cancel_seats):
        self.tuesday_eveng_cancel_seats = tuesday_eveng_cancel_seats
        self.total_seats = self.total_seats-book_seats
        self.total_seats = self.total_seats+tuesday_eveng_cancel_seats
        total_book_on_tuesday_eveng = book_seats-tuesday_eveng_cancel_seats
        total_price_of_book = total_book_on_tuesday_eveng * 100 + tuesday_eveng_cancel_seats * 20
        print(f'Tuesday eveng total seats avl :- {self.total_seats}')
        print(f'Tuesday eveng total booked seats :- {total_book_on_tuesday_eveng}')
        print(f'Total amount :- {total_price_of_book}')
        return total_price_of_book

    def total_count_bus(self):
        total_booking_seats = 100 -self.total_seats
        print(f'Total booking tickets:- {total_booking_seats}')
        total_cancel_seats = self.monday_morng_cancel_seats+self.monday_eveng_cancel_seats+self.tuesday_morng_cancel_seats+self.tuesday_eveng_cancel_seats
        print(f'Total cancellation seats {total_cancel_seats}')
        print(f'how much amount should be return:- {total_cancel_seats*80}')
        print(f'setas left :-{self.total_seats}')





obj = BusProgram('Galaxy','jaipur','Delhi',100,100,20)
monday_morning=obj.monday_morning(25,0)
print('------------------------------------------------------------------')
monday_eveng= obj.monday_eveng(20,5)

tuesday_morning= obj.tuesday_morning(35,12)
print('------------------------------------------------------------------')
tuesday_eveng = obj.tuesday_eveng(37,2)

print('------------------------------------------------------------------')
obj.total_count_bus()

print('------------------------------------------------------------------')
print(f'Total amount:-{monday_eveng+monday_morning+tuesday_eveng+tuesday_morning}')
'''

#static variable and class method

'''which variable written inside the class and but outside method, those variable know as static variable.
it is access by class Name , Obj Reference and class method cls variable
static variable is acceable by all methods'''

'''
class method :-

class method mainly use for access the static variable in a low memory efficiency.
class method by default use cls variable , instead of self parameter. in the parameter section.
with help of the cls variable it access the static variable inside the class method.
@classmethdo use decorator to create the class method
'''


'''class A:

    var = 10 #static variable.

    def f1(self):
        print(A.var)

    @classmethod
    def methods(cls):
        print(cls.var)



obj = A
obj.methods()'''

#satic method and local variable


'''
local variable 

inside the method or function , which variable is metioned known as local variable
local variable only accesable by the same method only

static method :-

it is a normal method, here we can pass any self and cls variable.
it will work like a generic method only.
@staticmethod
'''

'''class A:

    def f1(self):
        global a
        a = 10 #local
        print(a)

    def f2(self):
        print(a)

obj = A
obj.f1('None')
obj.f2('None')'''


class A:

    @staticmethod
    def add(a,b):
        res = a+b
        return res


obj = A
print(A.add(10,20))


















