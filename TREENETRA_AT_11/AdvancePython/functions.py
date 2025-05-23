'''syntax:-

def function_name(parameter):
    logic/statement
    return value

function_name()
function_name()'''

# def add_func():
#     a= int(input('Enter 1st num:-'))
#     b = int(input('Enter 2nd num:-'))
#     sum = a+b
#     return sum

# #what is parameter
#
# def add(num1,num2):
#     sum = num1+num2
#     return sum
# print(add(20,89))


# write function check the number is even or odd?

# def even_odd(num):
#     if num%2==0:
#         return 'Even'
#     else:
#         return 'Odd'
#
# print(even_odd(34))

#write function take list as a parameter , iterate the list check the how many pallindrom number is their.

# def list_pallindrom(li):
#     for i in li:
#         if str(i)==str(i)[::-1]:
#             print('Pallindrom',i)
#
#         else:
#             print('Not a Pallindrom',i)
# list_pallindrom([121,67,890,989,675])

#type of arguments

'''def func(parameter):#formal arguements
    logic
    
var = func(arguemnts) # actual argument
func()'''


# def addition():
#     a = int(input('Enter your number:-'))
#     b = int(input('Enter your number'))
#     result = a+b
#     return result
#
# print(addition())

#
# def addition(a,b):
#     result = a+b
#     return result
# print(addition('qwe','fgh'))


#type arguments

'''1.Positional Arguments
2.Keyword arguments
3.Default Arguments
4.Variable length of argument'''

# def substract(a,b):
#     result = a-b
#     return result
# print(substract(20,10))

# congrates for your marriege


#keyword arguments
# def marriege_wish(date,bride_name,groom_name,wish):
#     return f'hi,{bride_name} and {groom_name} ,{wish} on {date}'
#
# print(marriege_wish('09-09-2024',wish = 'congrates for your marriege',groom_name='Akhil',bride_name='Ritu'))


#Default Arguments

# def wish(name='Guest Uncle'):
#     return f'hi {name} welcome'
#
# print(wish('Pradeep Uncle'))
# print(wish('Mishra Uncle'))
# print(wish())



#Write a function take 3 parameter of int value and check who is the biggest number?
# write a function , function check the string in alphanumeric or not?
# Write a function conver int to string and add him in a another siting
#write function take a diction and itetrate and return the values only
# write function iterate a list ?


#Variable length of arguments
# *args and **kwargs
# *args :- nth of number of arguments


# def add(*args):
#     sum = 0
#     for i in args:
#         sum = sum+i
#     print(sum)
#
# add(10,20,67,78,54,809,67,45,90,75,345,9,79,654,99)


# def diction_data(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# diction_data(Name='Vishal',Address='Chatishgad',Dept='Dev',Salary=640000)

#Types of variable in Function

#global
#local

#global variable exam
'''c = 90
print(c)
def add(a,b):
    # inside of the fuction
    result = a+b+c
    return result
print(add(80,70))
print(c)'''



#local variable

'''
def add(a,b):
    global c
    c = 90
    result = a+b+c
    return result
print(add(10,20))

print(c)'''


#What is anonemous function
'''
it is nameless function
it is a single line code
lambda is the representer
'''

# syntax:-

'''var = lambda parameter:statements
var(parameter)'''

"""add = lambda a,b:a+b
print(add(10,20))

even = lambda a:a%2==0
print(even(11))

str_pallindrom = lambda str: str==str[::-1]
print(str_pallindrom('madam'))"""

# terenarry operator--single line cod eof conditional statement
# syntax:  ifresult if condition else elseresult
'''if 10>20:
    print(True)
else:
    print(False)'''

# var = True if 100>20 else False
# print(var)

#write a lambda function , check between the two number which is the biggest value help terennary operator

# number=lambda x,y:max(x,y)
# res=number(50,20)
# print(res)

# number = lambda a,b: a if a>b else b
# print(number(50,30))

# def largest_number(a,b,c):
#     if (a>b) and (a>c):
#         print('Biggest is:-',a)
#     elif (b>c):
#         print('Biggest is:-',b)
#     else:
#         print('Biggest is:-',c)
#
# largest_number(90,91,56)

#filter, map, reduce

#filter :- filter is a python inbuild method,who based on the fucntional condition filterized a collection

'''syntax
filter(function,collection)
'''
'''li = [10,21,43,34,67,78,99,98,69]

var = list(filter(lambda a:a%2==0,li))
print(var)'''


#map :- based on the functional condition, it will chnage the value of each element.


'''li = [10,23,45,43,29,90,231,453,267]

var = list(map(lambda a:a**2,li))
print(var)'''


#reduce
'''from functools import reduce

li =[10,23,45,43,29,90,231,453,267]

var = reduce(lambda a,b:a+b,li)
print(var)'''


# Nested Function
'''def outside_functions():
    print('outside function execute')
    def inner_function():
        print('inner function executed')
        print('inner function completed')
    inner_function()
    print('ouside function completed')

outside_functions()'''


#write a program check the list of element even or not, if evene write another function return squre of numbers

'''li = [10,11,12,13,14,15,16,27,18,19,20]
def even_element(li):
    for i in li:
        if i%2==0:
            def squre(i):
                print(i**2)
            squre(i)

# even_element({'Name':20})
even_element(li)'''

#decorater


# def decore(cal):
#     def mul(a,b):
#         m = a*b
#         return m,cal(a,b)
#     return mul
# @decore
# def cal(a,b):
#     sum = a+b
#     return sum
#
# print(cal(10,20))


#write a nested function, check the number is prime or not, if prime write a another function for cube.
#write decorate main function a factorial of 1,1000 and check in decorater how many armstrong is number is 1 to 1000.


'''def prime__number(n):
    count=0

    for i in range(1,n+1): 
        if n%i == 0:
            count+=1

    def prime(count):
        if count==2:
            print("is prime ")

            def cube(n):
                print((n*n*n))
            cube(n)
        else:
            print("is not a prime")
    prime(count)

prime__number(5)'''

#factorial

'''def fact(n):
    if n ==0:
        return False
    else:
        result = 1
        for i in range(1,n+1):
            result = result*i
        return result

for i in range(1,101):
    print(i,fact(i))'''


# Decorator chaining

'''def decore3(calculator):
    def division(a,b):
        div = a/b
        return div,calculator(a,b)
    return division

def decore2(calculator):
    def multiplication(a,b):
        mul = a*b
        return mul,calculator(a,b)
    return multiplication

def decore1(calculator):
    def substraction(a,b):
        sub = a-b
        return sub,calculator(a,b)
    return substraction

@decore3
@decore2
@decore1
def calculator(a,b):
    add = a+b
    return add

print(calculator(10,20))'''

#Generator

# def func():
#     for i in range(1,6):
#         yield i
#
# obj = func()
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
li = ['user-01','user-021','user-03','user-046','user-051','user-067','user-017','user-0134']
def func1(li):
    for i in li:
        yield i

obj = func1(li)

for i in range(1,5):
    print(next(obj))


















