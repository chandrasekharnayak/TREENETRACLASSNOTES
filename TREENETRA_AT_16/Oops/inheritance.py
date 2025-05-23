'''
class A--- object
    function1--- login function-- 10 lines code
    function2
    function3

Class B(A)
    function1--- login functionality -- 10lines


obj --- all kind of functionality use.

class A --inh---> Class B
ParentCls 1,2      ChildClas 3,4 -----(1,2,3,4)


parent --- cycle, car

child (parent)-- bike

cycel,car, bike

inhheritance is a concept where, parent call from the child one. and parent all methods are used by child side, but parent is
unable to child methods.

in python there are 4 types of

single inhheritance:- single parent class called in single child class.
multiple innheritance
multilevel inhheritance
hyrechical inhheritance


'''

'''class A:

    def f1(self):
        print('Class A fucntion 1')

    def f2(self):
        print('Class A function 2')

    def f3(self):
        print('Class A function 3')


class B(A):

    def f3(self):
        print('Class B function3')


obj_b = B
print(obj_b.f1('None'))
print(obj_b.f2('None'))
print(obj_b.f3('None'))

obj_a = A
print(obj_a.f3('None'))
'''

#multiple ohheritance
''' single child class but its inhherite many parent class'''


'''class A:
    def f1(self):
        print('Class A and function 1')
        
    def f5(self):
        print('Class A and function 5')

class B:
    def f2(self):
        print('Class B and function 2')
        
    def f5(self):
        print('Class B and function 5')

class C:
    def f3(self):
        print('Class C and function 3')
        


class D(C,B,A):
    def f4(self):
        print('Class D and function 4')
        


obj_d = D

obj_d.f1('None')
obj_d.f2('None')
obj_d.f3('None')
obj_d.f4('None')

obj_d.f5('None')'''

# MRO:- method resolution order

'''
multiple inhheritance stands from MRO, which class inhherite first those class method use first.

'''

#multilevel inhheritance

'''
singel parent class inhherite from multiple child class.

'''

'''class A:
    def f1(self):
        print('Class A and function 1')


class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

obj_b = B
obj_b.f1('None')

obj_c = C
obj_c.f1('None')

obj_d = D
obj_d.f1('None')'''


#hyrechical inhheritance

'''
parent class called from child, and this child is the parent class of another child class
last child its access all the method of parent and grand parent class
its look like family hyrechy
'''

'''class A:#GF
    def f1(self):
        print('Class A function f1')


class B(A):#f
    def f2(self):
        print('Class B function f2')
    

class C(B):#son
    def f3(self):
        print('Class C function f3')

obj_c = C
obj_c.f3('None')
obj_c.f2('None')
obj_c.f1('None')
'''


#polymerprisim

# methdo use in class in many form
#method overloading ''' in a class both the method name is same and access via the same class, but it is not support in python
#method overiding :- ''' two class same method, parent and child relationship between two class


#overloading

'''class A:
    def f1(self):
        print('Class A1 fuction 1')
        
    def f1(self):
        print('Class A2 function f1')
        
obj_a = A
obj_a.f1('None')'''

#method overriding

'''class A:
    def f1(self):
        print('Class A fuction 1')


class B(A):
    def f1(self):
        print('Class B fuction 1')
        A.f1('None')

obj_b = B
obj_b.f1('none')'''



















