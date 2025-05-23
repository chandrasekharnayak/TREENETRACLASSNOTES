'''
There are two types of functions
Inbuilt function  -= print(),id(),dir().help(),input(),eval(),len()
User Define Function

'''

'''def function_name(parameter:- if required):
    logic/statement
    return values'''


'''def wish():
    return 'Hi all good morning'


print(wish())
print(wish())
print(wish())
print(wish())'''

#what is parameter

'''def add(a,b):
    result = a+b
    return result

print(add(10,20))'''

# Types of parameters or arguments

'''
Positional Arguments
Keyword Arguments
Default Arguments
Variable Length of arguments

'''

#positional Arguments


'''def function(a,b): ----- parameter

function(values,values)---- arguments
'''

'''def add_numbers(a,b,c):
    results = a+b+c
    return results

print(add_numbers(10,20,30))'''

#keyword arguments

'''def name(state1,state2,state3,state4):
    print(f'Hi State names are {state1},{state2},{state3},{state4}')

name('Odisha',state4='Jharkhand',state2='Bihar',state3='Chatishgarh')
'''

#Default Argguemnst

'''def wish(name='Guest'):
    return f'Hi {name} good morning'

print(wish('Ramesh'))
print(wish('Suresh'))
print(wish())'''


'''def shoping_mall(total_price=100):
    return f'Hi today total price is :-{total_price}'

print(shoping_mall(678))
print(shoping_mall(1670))
print(shoping_mall())'''


#Write a python function check the number is pallindrom or not , not using str() and using str()
#write a python function check the number is even or odd.
#Write a python function and iterate a for loop using list data type.

#with help of str
'''def func1(num):
    if str(num)==str(num)[::-1]:
        return 'Pallindrom'
    else:
        return 'Not a Pallindrom'

print(func1(121))
print(func1(1291))
'''
#without string

'''def is_pallindrom(num):

    reversed_number = 0
    original_num = num

    while num>0:
        digit = num%10
        reversed_number = reversed_number*10+digit
        num//=10

    if original_num == reversed_number:
        return 'Pallindrom'
    else:
        return 'Not a Pallindrom'

print(is_pallindrom(121))
'''


'''def func1(li):
    for i in li:
        print(i)

func1([10,20,30,40])'''

#Variable length of arguments

'''*args
**kwargs'''

'''def func1(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

print(func1(10,20,30,40,50,607,67,89,675,45,32,12,12,1,2,12))'''


#create additional calcultor , first he is asking how many number you want, then provide
# the each number from customer
#or end user  then add those number.


'''def func2(**kwargs):

    for k,v in kwargs.items():
        print(k,v)

func2(name='Swadin',age=26,salary=890000)'''


'''def add_numbers(*args):
    # If no arguments provided, ask the user for numbers
    if not args:
        # Ask the user how many numbers they want to add
        num_numbers = int(input("How many numbers do you want to add? "))

        # Initialize an empty list to store the numbers
        numbers = []

        # Loop through each number and ask the user for input
        for i in range(num_numbers):
            number = float(input(f"Enter number {i + 1}: "))
            numbers.append(number)

        # Sum the numbers
        total = sum(numbers)
    else:
        # If arguments provided, sum them directly
        total = sum(args)

    # Print the result
    print("The sum of the numbers is:", total)


# Call the function to add numbers
add_numbers()'''

'''collcetion_for_argument = []

num = int(input('How many data number you want:-'))

for i in range(num):
    element = int(input('Enter your element in the func argument:-'))
    collcetion_for_argument.append(element)

def func1(*args):
    sum = 0
    for i in args:
        sum = sum+i
    print(sum)

func1(*collcetion_for_argument)'''


#Global variable and Local Variable

'''a = 10 # global var
# print(a)
def func1():

    global b
    a = 20 # local var
    # print(a)
    print(a)

func1()'''

# print(b)


#Anonymous Function or Lambda Function

'''A function who had no name, and its a single line code. Anonymous function use lambda keyword for declare it.'''

'''var = lambda parameter:logic/statement
var(parameter)'''

#add function in lambda

'''var = lambda a,b:a+b
print(var(10,20))
print(type(var))
'''

#even

'''var = lambda a:a%2==0
print(var(11))'''

#take a string a parameter check pallindrom or not in lambda function

'''is_pallindrom = lambda s : s == s[::-1]
print(is_pallindrom('race'))'''


#filter , map, reduce

'''age = [23,67,56,43,89,56,34,31,27,45,48,37,91,23,70]

# filter(functionality,collection_name)

var = list(filter(lambda i:i>=35 and i<=50,age))
print(var)'''


#map

# map(functionality,collection_name)
'''ten_years_back_age = [23,67,56,43,89,56,34,31,27,45,48,37,91,23,70]

var = list(map(lambda i:i**2,ten_years_back_age))
print(var)'''



#first filter age betweeen 35 to 50 and increase 10 in each element
'''age = [23,67,56,43,89,56,34,31,27,45,48,37,91,23,70]

var = list(map(lambda i:i+10,list(filter(lambda j:j>=35 and j<=50,age))))

print(var)'''

#reduce

# reduce(functionality,collection_name)

# from functools import reduce
#
# marks = [89,76,89,91,67,90]
#
# var = reduce(lambda a,b:a+b,marks)
# print(var)


#Nested Function

'''def outer():
    print('Outer function is execute:-')
    def inner():
        print('inner function is execute:-')
    inner()
    print('inner function was completed')
    print('outer function was completed')

outer()'''


'''def is_even(num):
    if num%2==0:
        def factorial(num):
            result = 1
            for i in range(2,num+1):
                result *=i
            return result
        return factorial(num)

print(is_even(12))'''


#data hiding
# Nested function can hide internal details and expose only the necessary


'''def counter():
    count = 0
    def increment():
        nonlocal count
        count +=1
        return count
    return increment

my_counter = counter()
print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())'''

#decorator

'''def decore(calculator):
    def substraction(a,b):
        sub = a-b
        return sub,calculator(a,b)
    return substraction


@decore
def calculator(a,b):
    add = a+b
    return add

print(calculator(10,20))'''

# create decorator with nth arguments and main functionlity is addition call new functionlity is substraction create decore.


'''def decore(calculator):
    def substraction(*args):
        sub = args[0]
        for i in args[1:]:
            sub = sub -i
        return sub,calculator(*args)
    return substraction


@decore
def calculator(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

print(calculator(10,20,30,40,50))'''


#write decorate check number is_pallindrom(without str) and is_armstrong.

#tomorrow decorator chaining
#generator


'''def decore3(calcultor):
    def division(a,b):
        div = a/b
        return div,calcultor(a,b)
    return division

def decore2(calcultor):
    def multiplication(a,b):
        mul = a*b
        return mul,calcultor(a,b)
    return multiplication

def decore1(calcultor):
    def substraction(a,b):
        sub = a-b
        return sub,calcultor(a, b)
    return substraction

@decore3
@decore2
@decore1
def calcultor(a,b):
    add = a+b
    return add

print(calcultor(10,20))'''


'''def calculator(a,b):
    add = a+b
    sub = a-b
    div = a/b
    mul = a*b
    return add,sub, div, mul

print(calculator(10,20))'''

#Generator

'''Generator is function , who is generate the sequence of number with hjelp of yield keyword , istead of return generator use yield for
returning the object, and use next()'''

'''def func1():
    for i in range(1,6):
        yield i

obj1 = func1()
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))'''



'''def decore(is_armstrong):
    def is_pallindrom(num):
        temp = num
        rev = 0
        while num>0:
            digit = num%10
            rev = rev*10+digit
            num = num//10

        if temp == rev:
            print('Pallindrom'),is_armstrong(num)
        else:
            print('Not Pallindrom'),is_armstrong(num)
    return is_pallindrom



@decore
def is_armstrong(num):
    num_digits = len(str(num))

    sum = 0

    temp_num = num

    while temp_num>0:
        digit = temp_num%10
        sum = sum+(digit**num_digits)
        temp_num = temp_num//10

    if num == sum:
        print('Armstrong')
    else:
        print('Not a Armstrong')



is_armstrong(121)'''


#Topics

'''what is function
user deefine function
parameter
type of arguments
global var and locals var
global and nonlocal keyword
lambda 
filter,map,reduce
nested function
decorator
generator'''

#module and package
#File Handleing
#Exception Handeling
#Regular exp
#oops