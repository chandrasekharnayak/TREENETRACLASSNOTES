'''def function_name():
    statemenet/logic/expression
    return data

function_name()
'''
from numpy.f2py.crackfortran import parameterpattern

'''
def addddd():
    a = int(input('Enter a num:-'))
    b = int(input('Enter a num2:-'))
    result = a+b
    return result

print(add())
'''
# What is a parameter?

'''def add(x,y):
    res = x+y
    return res

print(add(10,20))'''

'''def even_odd(num):
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'

print(even_odd(11))'''

'''def is_pallindrom(var):
    if  var == var[::-1]:
        return 'Pallindrom'
    else:
        return 'Not a Pallindrom'

print(is_pallindrom('wqdwq'))'''

# what is parameter and arguments?

'''def func1()---- parameters ------ formal arguemnts(its a one kind of variable)



fucn1()---arguments ---- actual arguments(data send -- variaable)'''

# types of arguemnts?

# positional
# keyword
# default
# variable length


#WAP a function for mathemetical op, (+,-,*,/)
#WAP a function check its even or not.
# WAP a function find a biggest number in a list.


'''def math(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add,sub,mul,div

print(math(10,20))
'''

'''def largest_num(li):
    max = 0
    for i in li:
        if i>max:
            max = i
    return max

li = [10,23,21,45,32,67,89,32,43,27]

print(largest_num(li))'''

'''li = [31,23,21,45,32,67,89,32,43,27]

n = len(li)

for i in range(n):
    for j in range(0,n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]

print(li)'''

# positional
# keyword
# default
# variable length

'''def cal(a,b,c,d):
    sub = (a-b)+(c-d)
    return sub

print(cal(10,20,30,40))'''


'''def add(b,f,c,e,d,a):
    print(a,b,c,d,e,f)

print(add(a=10,b=20,c=30,d=40,e=50,f=60))'''

# default arguments

'''def wish(name='sir'):
    return f'hi good morning {name}'

print(wish('pattnaik sir'))
print(wish('sahoo sir'))
print(wish())'''

#variable length of arguemnts - nth arguemnts

'''*args  - tuple
**kwargs- dict'''


'''def add_cal(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

print(add_cal(10,20,30,40,89,78,567,98))
'''

'''def nth_dict(**kwargs):
    print(kwargs)

print(nth_dict(name='A',age=21,salary=56000))
'''

#types of variables
# > global variables
# > local variables

'''var = 10 #global variable
print(var)

def f1():
    print(var)

f1()

def f2():
    print(var)

f1()
'''

'''def f1():
    global var
    var = 10 #local variable
    return var


print(f1())
print(var)'''

#anonomeous function:- a function have no name :- lambda function
'''
syntax:-
var = lambda parameter:logic
'''

# def func_name(parameter):
#     logic
#     logic based on pass parameter


#write a program add function help of lambda function

# var = lambda a,b:a+b
# print(var(10,20))

#pallindrom or not in lambda

'''var = lambda st:st == st[::-1]
print(var('mam'))'''

'''var = lambda a:a%2==0
print(var(11))'''

#addition operation  -- single line code
'''1. ternnary operator
2. List Comprehension
3. Dictionary Comprehension'''

# ternnary operator :- it is a single statement of if condition
'''
var = if_return  if condition else else_return
'''

'''st = 'mat'
var = 'Pallindrom' if st == st[::-1] else 'not a pallindrom'

print(var)'''

#list comprehension:- list com it is a single line code, in squre bracket we are iterate and get
# the result

# var = [i for i in range(1,50) if i%5==0]
# print(var)

li =['aw',90,'yu',67,65,'ui']

# op =['aw','yu','ui']
# new_li= []
# for i in li:
#     if type(i)==str:
#         new_li.append(i)
# print(new_li)

# new_li = [i for i in li if type(i)==str]
# print(new_li)

# [0,1,1,2,3,5,8,13]
# li = [0,1,1,2,3,5]
#
# for i in range(10):
#     var = li[-1]+li[-2]
#     li.append(var)
# print(li)


'''fib_series  = [0,1]
[fib_series.append(fib_series[-1]+fib_series[-2]) for i in range(10)]
print(fib_series)'''

#
'''['A','B','C'',D'.......'Z']
ord()
chr()'''

#filter, map, reduce(imp)
# filter(functional_condition,collection)

'''li = [12,56,43,23,67,89,34,21]
var = list(filter(lambda i:i%2==0,li))
print(var)'''

'''tu = ('yu',90,8+9j,'qw',98)
var = list(filter(lambda i:type(i)==str,tu))
print(var)
'''

'''li = [12,56,43,23,67,89,34,21]

def filter_even(li):
    even_li =[]
    for i in li:
        if i%2==0:
            even_li.append(i)
    return even_li

print(filter_even(li))
'''

# map :- map(function,collection)

'''li = [10,20,30,40,50,60]

var = list(map(lambda i:i+5,li))
print(var)'''

'''n =len(li)

for i in range(n):
    li[i] = li[i]+5
print(li)'''

'''li = ['qwerty','jbji','bjh','yugy']

var = list(map(lambda i:i.capitalize(),li))
print(var)'''

'''li = [116,899,676,455,321,449,318]'''

# '''add 5 in each element
# check the num is pallindrom'''

'''var = list(filter(lambda j:str(j)==str(j)[::-1],list(map(lambda i:i+5,li))))
print(var)'''

# reduce
from functools import reduce

# reduce(function,collection)

'''salary = [89,78,56,21,34,43,21,56,78,54]
var = reduce(lambda a,b:a+b,salary)
print(var)
'''

# nested function
'''a function under a function is know as nested fucntion, and first function is know as outer function and second
function know as inner function, every time inner function is depends upon the outer function'''


'''def outer_function():
    print('outer function execution')
    def inner_function():
        print('inner function execution')
    inner_function()
    print('inner function end')
    print('outer function end')

outer_function()
'''

# write a nested function check the number is pallindrom or not if the number is pallindrom the check the
# number even or not?

'''def is_pallindrom(num):
    if str(num)==str(num)[::-1]:
        def is_even(num):
            if num%2==0:
                return 'Even and Pallindrom'
            else:
                return 'Pallindrom but not even'
        return is_even(num)
    else:
        return 'not a pallindrom'


print(is_pallindrom(121))'''

# write a nested function , take a list of int,float,string, if string avialble then reverse a inner function

'''def fetch_string(li):
    string = []
    for i in li:
        if type(i)==str:
            def reverse_str(i):
                string.append(i[::-1])
            reverse_str(i)
    return string


li = [12,'rahul',98.9,9+9j,'ketan','rajib']'''

# print(fetch_string(li))


#decorater
# decorater is a function, take the argument a exiting function,
# modify the functionality of the existing function and return the extensible functionality

'''def decore(cal):
    def sub(a,b):
        res = a-b
        return res,cal(a,b)
    return sub


@decore
def cal(a,b):
    add = a+b
    return add

print(cal(10,20))'''

'''def decore(fibo):
    def inner(obj):
        data = fibo(obj)
        li = [i for i in data if i%2==0]
        data.append(li)
        print(data[0:-1])
        print(data[-1])
    return inner
@decore
def fibo(num):
    li = [0,1]
    for i in range(num-2):
        var = li[-1]+li[-2]
        li.append(var)
    return li

fib = fibo(10)
print(fib)'''

# what is decorator chining?

'''def decore3(cal):
    def div(a,b):
        res = a/b
        return res,cal(a,b)
    return div

def decore2(cal):
    def mul(a,b):
        res = a*b
        return res,cal(a,b)
    return mul


def decore1(cal):
    def sub(a,b):
        res = a-b
        return res,cal(a,b)
    return sub

@decore3
@decore1
@decore2
def cal(a,b):
    add= a+b
    return add

data = cal(10,20)

def
for i in data:
    if type(i)==tuple:
        for j in i:
            print(j)
    else:
        print(i)
'''

# what is recursion ? and how the recursive function work?

'''def fact(num):
    f = 1
    for i in range(1,num+1):
        f = i*f
    return f

print(fact(5))'''


'''def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))'''


# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(10))



'''li= [9,6,'676',3,5,'75',2,'878',1]

def sum(num):
    if len(num)<=1:
        return 1

    else:
        var = num[0] if isinstance(num[0],int) else 1
        return var*sum(num[1:])'''

# print(sum(li))

#generator:- function

# next()
# def f1():
#     for i in range(10):
#         yield i
# obj = f1()
#
# for i in range(10):
#     print(next(obj))

'''function:- 
parameter
type of arguments
types variable
lambda fucntion
terenarry op.
list com
nested fucntion
decorater
recursive fun
generator'''

module and Packages
exception handeling
File Handeling
Regular Expression
Opps




