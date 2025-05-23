"""def function_name(requried_paramete
jbj
    '''doc_string'''
    logic
    return value

function_name()"""

# what is a parameter?


# def addition(a,b):
#     add = a+b
#     return add
#
# # print(addition(10))
# print(addition(60,80))

# para vs arg

# actaul arg--arg
# formal arg-- parameter

#
# def function(formal arg):
#
#
# function(actual arg)

'''def even_odd(num):
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'

print(even_odd(10))
print(even_odd(99))'''

#Write a function check the number is armstrong or not?
#write function check in list all how many int is their?

#Types of arguments
# 4 types
#Postional Arguments
#Keyword Arguments
#Default Arguments
#variable length of Arguments

'''def sub(a,b):
    s = a-b
    return s

print(sub(30))'''

'''def wish(name,gift,wish,age):
    return f'Hi {name} {wish}, it"s from my end:-{gift}, now you are :- {age}'

print(wish('Reshab',wish='HBD',age=25,gift='VR-AIRTEL'))'''


#deafult arg

'''def wish(name='Uncle'):
    return f'Hi welcome to my sister mrg:{name}'

print(wish('Panda'))
print(wish('Patil Uncle'))
print(wish())'''

#Variable length of arguments
# args  == *args
# kwargs  == **kwargs


# def add(*args):
#     sum = 0
#     for i in args:
#         sum = sum+i
#     return sum
#
# print(add(10,20,30,89,78,76,56))


'''def add(*args):

    result = 0
    for i in args:
        arth = eval(input('Enter your op:-'))
        result = result, arth,i
    return result

print(add(10,20,30))'''

# **Keyword arguments

# def dict(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# dict(name='Reshab',address='Banglore')

#types of variables in py function
# global
# local
#
# a= 10#global
# print('outside:-',a)
# def f1():
#     global b
#     b = 20#local
#     print('inside f1:-',b)
#     print('inside f1:-',a)
#
#
# def f2():
#     print(b)
#     print('inside f2:-', a)
#
#
# f1()
# f2()
# print(b)

#Anonymyous function---lambda

# def function_name(parameter):
#     statement---logic
#
# function_name(arguments)



# def cal(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     return add,sub,mul
#
# print(cal(10,20))


# var = lambda paremeter:logic/statement

# var = lambda a,b:a+b
# print(var(10,20))

# pall = lambda a:str(a)==str(a)[::-1]
# print(pall(122))

#terenaary op-- single line conditional st.
#list comp

# num= int(input('Enter a number:-'))

# if var%2==0:
#     True
# else:
#     False
#
# var = if_result if condition else else_result

# var = 'even' if 10%2==0 else 'Odd'
# print(var)

# var = 'Pallindrom' if str(num)==str(num)[::-1] else 'Not a Pall'
# print(var)

# list comprenhension
# even_li = []
#
# for i in range(1,21):
#     if i%2==0:
#         even_li.append(i)
# print(even_li)

# even_li= [i for i in range(1,21) if i%2==0]
# print(even_li)

# pall = [i for i in range(100,501) if str(i)==str(i)[::-1]]
#
# # for i in range(100,501):
# #     if str(i)==str(i)[::-1]:
# #         pall.append(i)
# print(pall)


# li = [10,20,[78,90],(45,91)]

# li_new = [10,20,78,90,45,91]

# new_li = [i for sublist in li  for i in (sublist if isinstance(sublist,(list,tuple)) else [sublist])]
# print(new_li)

# new_li = [i for sublist in li for i in (sublist if isinstance(sublist,(list,tuple)) else [sublist])]
# print(new_li)

#filter,map,reduce

# filter :--- filter(function_name,collection)

# li = [10,23,45,32,67,89,76,65,221,41]
#
#
# var = list(filter(lambda n:n%2==0,li))
# print(var)

# map---map(function_name,collection)

'''li = [10,23,46,89,78]

var = list(map(lambda n:n+5,li))
print(var)'''

#reduce

# from functools import reduce
# li = [10,23,46,89,78]
#
# var = reduce(lambda a,b:a+b,li)
# print(var)

#decorator

# def decore1(cal):
#     def mul(a,b):
#         result = a*b
#         return result,cal(a,b)
#     return mul
#
# def decore(cal):
#     def sub(a,b):
#         result = a-b
#         return result,cal(a,b)
#     return sub
# @decore
# @decore1
# def cal(a,b):
#     add = a+b
#     return add
#
# print(cal(10,20))

'''def decore(string_length_count):
    def reverse_string(st):
        rev = ''
        for i in st:
            rev = i+rev
        return rev,string_length_count(st)

    return reverse_string


@decore
def string_length_count(st):
    var = len(st)
    return var

print(string_length_count('qwerty'))'''






# def decore(vi):
#     def count_occurance(s):
#         char_count = {}
#         for i in s:
#             if i in char_count:
#                 char_count[i]+=1
#             else:
#                 char_count[i]=1
#         data = [k for k in char_count if char_count[k]>1]
#         return data,vi(s)
#     return count_occurance
#
#
# @decore
# def is_prime(s):
#     if s == s[::-1]:
#         return f'{s} is pallindrom'
#
# print(is_prime('madam'))


#write function check the number is prime or not, and write decorater check the number is even or not

# def
#
#
#
#
#
# def is_prime(num):
#     if num<=1:
#         return False
#     if num ==2:
#         return True
#     if num%2==0:
#         return False
#     for i in range(3,int(num**0.5)+1,2):
#         if num%i==0:
#             return False
#     return True
#
# print(is_prime(102))

#generator

def f1():
    for i in range(1,6):
        yield i

my_obj = f1()

for i in range(5):
    print(next(my_obj))


