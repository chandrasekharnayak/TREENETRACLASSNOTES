# def functiuon_name():
#     logic
#     return data(var)

# def even_or_odd(num):
#     if num%2==0:
#         return 'Even'
#     else:
#         return 'ODD'
#
#
# print(even_or_odd(10))
# print(even_or_odd(11))

#WAF add two number

# def addition(a,b):
#     add = a+b
#     return add
#
# print(addition(10,20))

#WAF in python check the string is pallindrom or not

'''def is_pallindrom(str):
    reverse_str = ''

    for i in str:
        reverse_str = i + reverse_str

    if str == reverse_str:
        return 'Pallindrom'
    else:
        return 'Not pallindrom'


print(is_pallindrom('qwerty'))'''

#WAF count the addition of a list


# def count_of_list(li):
#
#     sum = 0
#     for i in li:
#         sum = sum+i
#     return sum
#
# li = [10,23,45,43,23,67,89]
# print(count_of_list(li))


# WAP check the number is armstrong or not?

'''def is_armstrong(num):

    str_int = str(num)
    len_str_int = len(str_int)

    arm_add = 0
    for i in str_int:
        arm_add = arm_add +int(i)**len_str_int

    if num == arm_add:
        return 'armstrong'
    else:
        return 'not a armstromg'''


# print(is_armstrong(153))


#WAP check how many armstrong are prersent in 100 to 10000

'''def is_armstrong(num):

    str_int = str(num)
    len_str_int = len(str_int)

    arm_add = 0
    for i in str_int:
        arm_add = arm_add +int(i)**len_str_int

    return num == arm_add
'''

'''def armstrong_li(start,end):

    arm_li = []
    for i in range(start,end+1):
        if is_armstrong(i):
            arm_li.append(i)
    print(arm_li)
    print(len(arm_li))

print(armstrong_li(100,10000))'''




#types of arguments

'''
positional arg
keyword arg
default arg
variable length arg
'''

# positional arg
'''count the parameter and args must be same, 1st position of args, hit 1st parameter only  and others are same'''

'''def add(a,b):
    res = a+b
    return res


add(10,20,30)
'''

#keyword arg

'''def my_profile(name,age,salary,address,post):
    return f'Hi My Name is :{name}, and i am {age} years old, am staying in {address}, and currennt i will get {salary}, my post :- {post}'


print(my_profile(post='QA',name='chandra',salary=1,address='BBSR',age=28))'''

#default arguments

'''def wish(name='Uncle'):
    return f'Hi {name} good mornming'

print(wish())'''

#variable length of arguments :- nth variable
# *args
# **kwrags:- keywoords variable length args

# def add(*args):
#     return args,type(args)
#
# print(add(10,20,30,40,50))

'''def cal_add(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum


print(cal_add(10,20,30,40,70,90))'''

#kwrags

# def dict_op(**kwargs):
#     return kwargs,type(kwargs)


# print(dict_op(name='chandra',age=28,address='bbsr'))

#tyeps variables
#lambda funbction
#singlline function
#map, filter, reduce


# HW :-
#
# WAP to check number is prime or not?
# WAP to check string anonimus or not?
#
# silent
# listen


# class3
#types of variables?
#two types variables
    #global variable:- which variable declare outside of the function known as global variable, its work both outsidr and inside of the function.
    #local variable:- which variable declare only inside of the function, know as Local variables. it is not possiable use this vbariable outside of the fuhnction

# global keyowrd :- convert local variable into the global variable



#GV

'''x = 10
print(x)
def add(a,b):
    res = a+b+x
    return res

print(add(100,150))'''


#LV

'''def add():

    global a
    a= 10
    return a

print(add())

print(a)'''

#single functiomn or anonomyous function or lambda function

# anonomyous means no name , or function without a name, and it is a single line function or lambda function


# variable = lambda parameter:logic

# def function_name(parameter):
#     logic
#
# function_name()

'''
add = lambda a,b:a+b

print(add(10,20))
'''

# even = lambda num :num%2==0
# print(even(21))


# is_pallindrom = lambda num : str(num)==str(num)[::-1]
# print(is_pallindrom(134))

#wap lambda function return even number from a list.

'''li = [10,21,34,57.89,24]


var = lambda li : [i for i in li if i%2==0]
print(var(li))'''


#terrnery op and comprehension

# ternerray op is single line code for conditional statement

# if_print if condition else else_print

'''num = 10
var = 'even' if num%2==0 else 'odd'
print(var)'''

# comprehsion
# list comprehesion and dict
'''write the loop inside squre, loop generating the element and store in list, it is also a single line code'''

# var = [for ptint for loop use]

'''var = [i for i in range(1,11)]
print(var)'''

# var = [i for i in range(1,11) if i%2==0]
# print(var)

#filter, map, reduce

'''they are using a functional condition and based on functional conditonal , they need to operated the collection'''

#filter :- use the conditional collection,and filetr the collection.



#write filter program to filter element in a list
# synatx
# filter(functional condition,collection)


'''li = [10,24,56,89,97,99,81,33,66]
var = list(filter(lambda num:num%3==0,li))
print(var)'''


# li = [10,90.89,True,10,'yuo',78,'io']
#
# var = list(filter(lambda i: type(i)==str,li))
# print(var)

#map
# map(functional condition,collection)


# li = [10,20,30,40]
#
# var = list(map(lambda a:a*a,li))
# print(var)


# li = [10,'ui',80,'yu',60,'po']
# data = list(map(lambda x:x*x,list(filter(lambda a :type(a)==int,li))))
# print(data)

# data = list(map(lambda a:a.capitalize(),list(filter(lambda a:type(a)==str,li))))
# print(data)

# reduce()

import functools


# reduce(conditional_function,collection)

# li = [10,20,30,40]
#
# data = functools.reduce(lambda a,b:a+b,li)
# print(data)

li = [10,'ui',80,'yu',60,'po']
# [100,6400,3600]


# filter -- int
# map -- int ka squre
# reduce - squre ka sum

# import functools
#
# data = functools.reduce(lambda a,b:a+b,list(map(lambda x:x*x,list(filter(lambda a:type(a)==int,li)))))
# print(data)

#recusion
''' when a function call its self known as recusrion'''

'''def print_num(n):
    if n>5:
        return
    print(n+1)
    # print_num(n+1)

print(print_num(1))'''


# fib_series = [0,1]
#
# for i in range(10):
#     res = fib_series[-1]+fib_series[-2]
#     fib_series.append(res)
#
# print(fib_series)

#write fib series using python recursion?


# def fib_series(n):
#     if n<=0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return fib_series(n-1)+fib_series(n-2)
#
#
# for i in range(10):
#     print(fib_series(i),end = ' ')

# def generate_num(num):
#     print(num)
#     if num>0:
#         generate_num(num-1)
#
# generate_num(10)

'''def func(num):
    if num%5==0 and num%3==0:
        print(num)
    if num<100:
        func(num+1)

func(1)'''

#nested function:-

# def outer():
#     print('outfunction is exceute')
#     def inner():
#         print('inner function is execute')
#     inner()
#     print('inner function is completed')
#     print('outer function complete')

# outer()


#nested function with factorial

'''def compute_factorial_fib(n):
    def factorial(x):
        if x==0 or x==1:
            return 1
        else:
            return x*factorial(x-1)

    def fib_series(x):
        if x<=0:
            return 0
        elif x ==1:
            return 1
        else:
            return fib_series(x-1)+fib_series(x-2)

    for i in range(n):
        print(fib_series(i))

    return factorial(n)
print(compute_factorial_fib(10))'''



#decorater and generater
'''decorator is function it's modify the functionality of existing function,

how
decorator function takes paramerer name as a exitsing fuction name, and connect with the existing function 
help @ and provoide the decorator function name, and modify the funtionality help of inner function.

'''
#
# def decore(cal):
#     def mul(a,b):
#         res = a*b
#         return res
#     return mul
#
# @decore
# def cal(a,b):
#     res = a+b
#     return res
#
#
# print(cal(10,20))


# def decore(bank_deposite_book):
#     def bank_deposite_book_modified(withdraw,deposite,current_amount=100):
#         time = int(input("enter the days"))
#         if time>=180:
#             interset_amount = bank_deposite_book(withdraw,deposite)*(5/100)
#             final_amount = bank_deposite_book(withdraw,deposite)+interset_amount
#             return final_amount,bank_deposite_book(withdraw,deposite),interset_amount
#     return bank_deposite_book_modified
#
#
# @decore
# def bank_deposite_book(withdraw,deposite,current_amount=100):
#     after_withdraw = current_amount-withdraw
#     current_amount = current_amount-withdraw
#     # print(current_amount)
#     after_deposite = current_amount+deposite
#     current_amount = current_amount+deposite
#     # print(current_amount)
#     return current_amount
#
# # print(bank_deposite_book(80,0))
# print(bank_deposite_book(10,1000))



# WAP ,

'''li = ['Abhishek','Abhinash','Abhilash','Abhishek','Abhay','Abhinash','Abhilash','Abhilash']


def decore(count_element_list):
    def inner(li):
        return len(li),count_element_list(li)
    return inner

@decore
def count_element_list(li):
    count_element = {}

    for i in li:
        if i in count_element:
            count_element[i]+=1
        else:
            count_element[i]=1

    return count_element

print(count_element_list(li))'''

# 1.WAP decorator check the count the function calls
# 2.WAP program check the number is pallindrom or not and check number anagram or not?


#Generator
'''Generator is a function, it's generating the element one by one sequence wise. instead of return keyword
it's using yiled and also use next function'''

# def f1():
#     for i in range(1,11):
#         yield i
#
# var = f1()
# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))



# def f1():
#     for i in range(1,11):
#         return i
#
# print(f1())


# li = ['Vivek',28,780000,'Gopalpur','B.Tech']
#
#
# def f1(li):
#     for i in li:
#         yield i
#
#
# var = f1(li)
#
#
# for i in range(len(li)):
#     print(next(var))


# di = [
#     {'vivek':{'age':28,'salary':78000,'address':'gopalpur'}},
#     {'Sobhit':{'age':29,'salary':80000,'address':'ctc'}},
#     {'Richa':{'age':30,'salary':82000,'address':'bbsr'}},
#
# ]

'''di = [
    {'vivek':{'Math':78,'Chem':82,'Phy':85}},
    {'Sobhit':{'Math':78,'Chem':82,'Phy':85}},
    {'Richa':{'Math':78,'Chem':82,'Phy':85}},

]
def f1(li,name):
    for i in li:
        for key,value in i.items():
            if key==name:
                for key1,value1 in value.items():
                    yield key1,value1

var = f1(di,'Richa')


for i in range(3):
    print(next(var))'''



'''di = [
    {'vivek':{'Math':78,'Chem':82,'Phy':85}},
    {'Sobhit':{'Math':78,'Chem':82,'Phy':85}},
    {'Richa':{'Math':78,'Chem':82,'Phy':85}},

]'''


'''def f1():
    for i in range(1,11):
        yield i

var = f1()

print(next(var))'''


'''7th May'''

'''Types of variables
Lambda Functiomn
Ternery operator
comprehension
Filter'''

#Types of var
'''
global var
local var
'''
'''
a = 10
def f1():
    global b
    b = 20
    print('inside func:-',a)
    print('inside func:-',b)

print('outside func:-',a)

f1()
print('outside func:-',b)'''


#terrenery operator :- write conditional statement in a single so that it's know as terrenry operator, we will use terrenery op for the code optimization.

# var = if_printed if condition else else_printed

# num = 11
#
# var = 'even' if num%2==0 else 'odd'
# print(var)


#comprehesion
'''
list com
dict com
'''

# var = [var for var in coll]

# var = [i for i in range(1,11) if i%2==0]
# print(var)

# pallindorm_list = []
#
# for i in range(100,1001):
#     if str(i)==str(i)[::-1]:
#         pallindorm_list.append(i)
#
# print(pallindorm_list)

# pallidrom_list = [i for i in range(100,1001) if str(i)==str(i)[::-1]]
# print(pallidrom_list)


# di = {}
#
# for i in range(1,11):
#     di[i]=i*i
#
# print(di)

# di = {i:i*i for i in range(1,11)}
# print(di)

#lambda function

# var = lambda parameter:condition

# add = lambda a,b:a+b
# print(add(10,20))

#string palllindrom

# var = lambda str : str ==str[::-1]
# print(var('qwerty'))


li = [10,56,24,89,32,56,90,21]

# var = list(filter(lambda num : num%2==0,li))
# print(var)

# var = list(map(lambda num:num*num , li))
# print(var)

from functools import reduce

var = reduce(lambda a,b:a+b,li)
print(var)





