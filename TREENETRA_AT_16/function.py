# function?
# function is a wrapper code, based the requirement we call that logic based on function name.

'''
inbuilt function :- print(),id(),type(),dir(),eval(),datatyep function -- ()
user define function
'''
from idlelib.run import manage_socket
from lib2to3.pytree import convert

from pandas.io.formats.format import return_docstring
from sqlalchemy.orm.util import eval_name_only

'''def function_name():
    logic--- statements
    return data

function_name()'''


'''def wish(name,msg):
    return f'hi {name}  {msg}'

print(wish('akshya','good eveng'))
print(wish('lokesh','good morning'))
# print(wish('jitu'))'''

'''def addition(a,b):
    res = a+b
    return res


print(addition(10,20))
print(addition(100,2000))'''

'''def is_even(num):
    if num%2==0:
        return 'Even'
    else:
        return 'odd'

print(is_even(20))'''



'''def rev_st(st):
    new_st = ''
    for i in st:
        new_st=i+new_st
    return new_st

print(rev_st('lokesh'))
print(rev_st('rupali'))'''

'''def highest_word_length(st):
    split_st = st.split()

    num = 0
    for i in split_st:
        if len(i)>num:
            num = len(i)

    for i in split_st:
        if len(i)==num:
            return i,num

st = ' i love india it is a best country'

print(highest_word_length(st))'''


# def func(para1,para2,par3):
#     logic
#
# func(argu1,argu2,argu3)
#types of arguments?
'''
1.positional
2.Keyword
3.Default
4.Variable length of arguments
'''

'''def add(a,b,c):
    res = a+b
    return res
print(add(10,20,30))
'''

'''def add(a,e,c,b,d):
    print('a',a)
    print('b', b)
    print('c', c)
    print('d', d)
    print('e', e)


add(a=10,b=20,c=30,e=50)'''


#default arguments

'''def add(a,b=0):
    res= a+b
    return res
print(add(10,20))'''

#variable length
# *args  **kwargs


'''def add(*args):
    res = 0

    for i in args:
        user_input = input('Enter your symbol')
        if user_input =='+':
            res = res + i
        elif user_input == '-':
            res = res - i
        elif user_input == '*':
            res = res * i
        elif user_input == '/':
            res = res / i
        print(res)
    print(res)
add(10,20,30,40,50,60)'''

'''first_num = int(input('Enter your number:-'))
symbol = input('Enter your symbol:-')
sec = int(input('Enter your number:-'))'''

'''res = 0
while True:
    symbol = input('Enter your symbol:-')
    num = int(input('Enter your number:-'))

    if symbol == '+':
        res = res+num
    elif symbol=='-':
        res = res-num
    elif symbol=='*':
        res = res*num
    elif symbol=='/':
        res = res/num
    print(res)'''

#types of variable in function
#what is lambda or anomomyous function
#terenary op
#list comprehension
#dict comprehension

'''
1.global variable:
outside of function when we declare a variable and that variable access by outside of the function and inside the function known as global variable.


2.local variable
a variable declare inside of the function, it will access in inside of the function only, not in other function and outiside of the function.
'''

'''a = 10#global

def f1():
    print(a)

f1()
print(a)

def f2():
    print(a)
f2()'''


'''def f1():
    global a
    a = 10
    print(a)

f1()

def f2():
    print(a)

f2()
'''

#what is lambda or anomyous func.
'''a function have a no name, that function know as lambda ,
 lambda function advantage
 it is a single line code.
 less time taken
 memory efficient.
 
 syntax:-
 
 var = lambda parameter:logic
 print(var(arg))
 '''
'''add = lambda a,b:a+b
print(add(10,20))'''

'''evn = lambda n:n%2==0
print(evn(11))
'''

# terenary operator
'''write a single line code for the conditional statement.

if_result if condition else else_result

'''

'''num = 11

var ='even' if num%2==0 else 'odd'
print(var)
'''
# if num%2==0:
#     print('even')
# else:
#     print('odd')


'''var = lambda num:'pallindrom' if str(num)==str(num)[::-1] else 'not pallindrom'
print(var(122))'''

'''var = lambda a,b,c: 'a is biggest number' if a>b and a>c else 'b is biigest number' if b>c else 'c is biggest number'
print(var(5,3,9))'''

'''even = lambda : [i for i in range(1,21) if i%2==0]
print(even())'''

#list comprehension
'''it is a single code to generate a multiple elements help of for loop and store in a list'''

#store 1 to 10 in a list

# li = [i for i in range(1,11) if i%2==0]
# print(li)


'''li = [i for i in range(1,1001) if str(i)==str(i)[::-1] and len(str(i))>2]
print(li)'''


# what is dictionary comprehesion?
'''it is a single code to generate a multiple elements help of for loop and store in a dict'''

'''di = {i:i**3 for i in range(1,11)}
print(di)'''

# for i in range(1,11):
#     di[i]=i**3
#
# print(di)


# tomorrow
#special function :- filter, map and reduce
#leap year, prime numebr, armstring number, while number reversing
#nested function

#filter
'''filterlize the element from collection based on condition

var = filter(functional_condition,collection)
'''

'''li = [12,90,'qwerty',78.89,'yuo']
'''
# string_li = []
#
# for i in li:
#     if type(i)==str:
#         string_li.append(i)
# print(string_li)

'''var = list(filter(lambda a : type(a)==str,li))
print(var)'''


'''li = [12,89,56,55,20,15,90,23,45,12]

var = list(filter(lambda a:a%3==0 and a%5==0,li))
print(var)'''

# what is armstrong?

# def is_armstrong(num):
#     len_num = len(str(num))
#
#     sum = 0
#     for i in str(num):
#         value = int(i)**len_num
#         sum = sum+value
#
#     return sum == num

'''is_armstrong = list(filter(lambda num: num if sum(int(i) **len(str(num)) for i in str(num)) == num else None, range(100,10001)))
print(is_armstrong)
'''
# num = 153
#
# if is_armstrong(num)== num:
#     print('is arm')
# else:
#     print('not arms')


'''for i in range(100,10001):
    if is_armstrong(i):
        print(i)'''

# map
'''map(functional_condition,collection)\

what ever element are present in a collection based on the requirement , it will modify the each element.

'''
'''
li = [10,20,30,40,50,60]


var = list(map(lambda a: a+100,li))
print(var)'''


'''li = ['Ajit Kumar','Abhay Kumar','Chandan Pradhan','Biswas Bharadwaj','Sekhar Achary','Dharshan Mishra']

var = list(filter(lambda a : type(a)==tuple,list(map(lambda a:tuple(a.split()) if 'Kumar' in tuple(a.split()) else None,li))))
print(var)'''

'''new_li = []

for i in li:
    new_li.append(tuple(i.split()))'''

'''new_li = []

for i in li:
    if 'Kumar' in tuple(i.split()):
        new_li.append(tuple(i.split()))
print(new_li)
'''



'''1.[('F','L'),('F','L'),('F','L')]
[('Ajit','Kumar'),('Abhay','Kumar')]'''

'''
#reduce

syntax:-

reduce(condition,collection)


'''

'''li = [10,20,30,40]
from functools import reduce

var = reduce(lambda a,b:a+b,li)
print(var)'''


'''what is function and how to write it.
what is parameter, and how define the parameter
Types arguments
types of variables
lambda function
map , filter and reduce
programs.

#leap year, prime numberr, armstrong number, while number reversing
'''
'''file handeling
oops
expection handeling
Regular expression '''

'''Falsk and Test in api and json'''
'''Basic HTML and CSS'''
'''Selenium and Pytest'''
'''Django'''
'''Project'''
'''Docker, Jenkins'''
'''From tomorrow SQL and Unix'''


'''Nested function:-

In function, write a another function known as nested function.

'''

'''def outer_function():
    print('Outer Function is execute')
    def inner_function():
        print('Inner Function is execute')
    inner_function()
    print('Inner function completed')
    print('Outer function completed')

outer_function()'''


'''def panel_zone(LL,RL):
    def acc():
        pass
    acc()
    def break1():
        pass
    break1()
    def clutch():
        pass
    clutch()
'''

'''def calculator(*args):

    def addition():
        res = sum(args)
        return res

    return addition()

    def sub

print(calculator())'''


#decorator :-

'''def decore1(cal):
    def mul(a,b):
        res = a*b
        return res,cal(a,b)
    return mul


@decore1
def cal(a,b):
    add = a+b
    return add

print(cal(10,20))'''



'''def is_prime(num):

   if num<=1:
       return False

   for i in range(2,num+1):
       if num%i==0:
           if i ==num:
               continue
           else:
               return False

   return True'''

# for i in range(1,101):
#     if is_prime(i):
#         print(i)


'''def is_prime(num):

   if num<=1:
       return False

   for i in range(2,int(num**0.5)+1):
       if num%i==0:
           return False

   return True

print(is_prime(99))'''


'''
1.decorator chaining
2.Generator
3.Iterator
4.Closer
'''


#decorator chaining:- when in a single function , we will execute a nth number of decorator , called decorator chaining\

'''def decore_mul(cal):
    def mul(a,b):
        res = a*b
        return res,cal(a,b)
    return mul


def decore_sub(cal):
    def sub(a,b):
        res = a-b
        return res,cal(a,b)
    return sub

@decore_mul
@decore_sub
def cal(a,b):
    res = a+b
    return res

print(cal(10,20))'''



'''st = 'i love india'

WAP count the each occurance of string
Decore them and split the string into a list ['i','love','india']'''


'''def decore_split(count_occurance):
    def split(st):
        res = st.split()
        return res,count_occurance(st)
    return split

@decore_split
def count_occurance(st):
    count_element = {}

    for i in st:
        if i in count_element:
            count_element[i]+=1
        else:
            count_element[i]=1
    return count_element

st = 'i love india'
print(count_occurance(st))'''


#generator:- generator is a function , it will return values sequence wise, instead of return it will use yield keyword. and generating the obj help of next function.

'''def f1():
    for i in range(1,10):
        yield i

var =f1()
print(next(var))
print(next(var))
print(next(var))
print(next(var))'''



'''def f1():
    li = [10,20,30,40,50]
    for i in li:
        res = i**2
        yield res

var = f1()
for i in var:
    print(i)'''


'''li_str = ['Abhiman','Abhilash','Abhilipsa','Abhiram']

def f1(li_str):
    for i in li_str:
        if 'Abhi' in i:
            yield i.replace('Abhi','****')

var = f1(li_str)

for i in var:
    print(i)'''

def f1():
    a = 10

print(f1())
