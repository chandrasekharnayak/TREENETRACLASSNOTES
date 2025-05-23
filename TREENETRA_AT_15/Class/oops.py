# class Studnet:
#     '''this class is writen for studnets data'''
#     def methods1(self):#instnace methods
#         return 'Hi'
#
# #call the class
# #create the obj for call the class
# #obj means its a variable, where we can call the class
#
# obj = Studnet()
# print(obj.__doc__)
# print(obj.methods1())

'''
there are 3 types of variables and methods
variables
---------
instance variabe
static var
local var

methods
---------
instance methods
class mathods
static methods

'''
from django.db.models.base import method_set_order
from pandas.core.indexes.extension import inherit_names
from pandas.plotting import hist_frame

"""class Studnets:

    def __init__(self,name,age,salary):#constructor
        '''self is instnace variable , instnace var who chnage the data from obj to obj'''
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):#instnace methdos
        print(f'My name is {self.name}, age is {self.age}, my slaary is {self.salary}')

obj = Studnets('Ashutosh',21,450000)
# print(obj.__dict__)
obj.display()
# obj.display()

obj2 = Studnets('DJ','28',9876545678)
obj2.display()"""

'''create class name studnet_mark
subject math, science, history
create method fetch total mark and percentage of rahul, atul, sipun'''


'''instnace method and instance variable

instance varuable:- who vary from object to object know as instnace variable.
    1.inside a constructor with help of self.
    2.inside a instance  method with help of self.
    3.with help object reference create instance variable
'''

'''class Students:
    def __init__(self,math,science,history):
        self.math = math
        self.science = science
        self.history = history

    def total_mark_and_percetange(self):
        total = self.history+self.math+self.science
        pec = (total/300)*(100)
        return f'{total} out 300 marks , percentage is {pec}%'

obj_rahul= Students(78,83,91)
obj_rahul.geography = 83
obj_rahul.chem = 90
del obj_rahul.chem # dec
print(obj_rahul.__dict__)
print(obj_rahul.total_mark_and_percetange())'''


'''bus  --- 60 seats 
 per ticket booking was 300 
 cancelation fee :- 30rs. -- 270 return 

sunday  morning --- 15 tickets book
sunday evening --- 3 tickets canceled

monday monring --- 35 tickets booked and 7 tickets cancel 

Tueasday --- 8 seats booked -- and 3 cancelled--

count how many seats are booked, how many seats are vacate,
total booking amount 

'''

'''class Bus:

    def __init__(self,seta_avl=60,ticket_price=300,cancelation= 30):
        self.seta_avl = seta_avl
        self.ticket_price = ticket_price
        self.cancelation = cancelation
        self.booked_seats = 0
        self.vacate_seats = 0
        self.total_earnings = 0

    def book_tickets(self,count):
        if count <= self.seta_avl:
            self.seta_avl = self.seta_avl-count
            self.booked_seats= self.booked_seats+count
            self.total_earnings += count*self.ticket_price
            print(f'{count} tickets  booked, {self.seta_avl} seats avilable now')
        else:
            print(f'Not Enough seats avl to book')

    def cancel_tickets(self,count):
        if count <= self.booked_seats:
            self.seta_avl += count
            self.vacate_seats += count
            self.booked_seats -= count
            self.total_earnings-= count*(self.ticket_price-self.cancelation)
            print(f'{count} tickets canceld, {self.seta_avl} seats avl now')
        else:
            print(f'cannot cancel {count} ticket as only {self.booked_seats} are booked')

    def summary(self):
        print('------summary-------')
        print(f'Total seats booked :{self.booked_seats}')
        print(f'Total seats vacate :{self.vacate_seats}')
        print(f'Total earning :{self.total_earnings} rs')

bus = Bus()

#sunday
bus.book_tickets(15)
bus.cancel_tickets(3)

#monday
bus.book_tickets(35)
bus.cancel_tickets(7)



#summary
bus.summary()'''


'''class Bus:
    def _init_(self,seats,book_price,tcket_booked,cancel):
        self.seats=seats
        self.book_price=book_price
        self.ticket_booked=tcket_booked
        self.cancel=cancel

    def calc(self):
        total_seats_booked=self.seats-self.cancel
        total_price=self.book_price*total_seats_booked
        total_vacate=self.seats-total_seats_booked
        print(f"total price:{total_price} total seats vacate:{total_vacate} total seats booked:{total_seats_booked}")

sunday=Bus(60,300,15,3)
sunday.calc()
monday=Bus(60,300,35,7)
monday.calc()
tuesday=Bus(60,300,8,3)
tuesday.calc()'''

#ihheritance
'''
single -- super() ---
multiple
multilevel 
hyrechical
'''

'''class A:

    def f1(self):
        print('class A f1')
    def f2(self):
        print('class A f2 ')


class B(A):
    def f3(self):
        print('class B f3')

    def f4(self):
        print('class B f4')

obj_b = B()

obj_b.f3()
obj_b.f4()
obj_b.f1()
obj_b.f2()'''


#polymerprism

'''@classmethod
@staticmethod
staic var
local var

regular exp --'''

'''class A:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        res = self.a+self.b
        return res

class B(A):

    def __init__(self,c,a,b):
        self.c =c
        super().__init__(a,b)

    def mul(self):
        res = super().add()*self.c
        return res,super().add()



obj_b = B(10,20,30)
print(obj_b.mul())'''



#multiple :-

# in a single class, we will inhherite multiple clases using MRO(Method Resolution Order) principle.

'''class A:

    def method1(self):
        print('Class A method1')

class B:

    def method1(self):
        print('Class B method1')


class C:

    def method1(self):
        print('Class C method1')

class D(C,A,B):

    def method1(self):
        print('Class D method1')
        super().method1()

obj_d = D()
obj_d.method1()'''

# Multilevel inherit


'''class Grandfather:

    def gf_properties(self):
        return 'gf properyies'


class father(Grandfather):

    def father_properties(self):
        return 'father properyies'


class me(father):

    def my_properties(self):
        return 'my properyies'


# obj_g = Grandfather()
# print(obj_g.gf_properties())
# print(obj_g.father_properties())

# obj_father = father()
# print(obj_father.gf_properties())
# print(obj_father.father_properties())

obj_me = me()
print(obj_me.gf_properties())
print(obj_me.father_properties())
print(obj_me.my_properties())'''



'''class Father:
    def father_proerties(self):
        return 'father properties'

class ElderSon(Father):

    def method1(self):
        return super().father_proerties()

class YongerSon(Father):
    def method1(self):
        return super().father_proerties()

class Doughter(Father):
    def method1(self):
        return super().father_proerties()

object_elder = ElderSon()
print(object_elder.method1())

object_younger = YongerSon()
print(object_younger.method1())'''


#polymerprism :- methods have many forms

'''
method overloading
method overiding'''


'''class A:

    def f1(self):
        return 'f1 method first'

    def f1(self):
        return 'f1 method second'

obj_a = A()
print(obj_a.f1())
'''


'''class A:
    def f1(self):
        return 'f1 method class A'

class B(A):
    def f1(self):
        return 'f1 method class B',super().f1()


object_b = B()
print(object_b.f1())'''

#classmethod and static variables

'''class Counter:#10MB

    count = 0 # static variable --- global var#1kb

    def __init__(self):
        Counter.count+=1

    @classmethod
    def get_count(cls):
        print(f'Number of instnace :-{cls.count}')

obj= Counter()
obj.get_count()
obj.get_count()'''

#static method

'''class Math:

    @staticmethod
    def add(a,b):
        res = a+b
        return res

    @staticmethod
    def sub(a, b):
        res = a - b
        return res

    @staticmethod
    def mul(a, b):
        res = a * b
        return res

obj = Math()
print(obj.add(10,20))
'''

# Abstration
'''A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.'''

from abc import ABC,abstractmethod

class MathOperation(ABC):
    '''Abstract base class for mathemetical operation'''

    @abstractmethod
    def calculator(self,a,b):
        pass

    def trigno(self):
        pass

    def algerbra(self):
        pass

    def hyprothenisi(self):
        pass

class Addition(MathOperation):
    def calculator(self,a,b):
        return a+b

class Substration(MathOperation):
    def calculator(self,a,b):
        return a-b

class Multiplication(MathOperation):
    def calculator(self,a,b):
        return a*b

class Division(MathOperation):
    def calculator(self,a,b):
        return a/b


operations = [
    Addition(),
    Substration(),
    Multiplication(),
    Division()
]

a,b = 10,20

for i in operations:
    print(i.calculator(a,b))






















# deep copy vs shallow copy

import copy
'''copy.copy() # shallow

copy.deepcopy()#deep'''

# old_var = [[1,2],[3,4],[5,6]]

#shllow
'''new_var = copy.copy(old_var)
new_var[0][0]=100
print(new_var)
print(old_var)
print(id(old_var))
print((id(new_var)))'''

'''new_var = copy.deepcopy(old_var)
new_var[0][0]=100
print(new_var)
print(old_var)
print(id(old_var))
print((id(new_var)))'''


# a = 'kjuhuj'
# b = 'kjuhuj'
# print(id(a))
# print(id(b))













