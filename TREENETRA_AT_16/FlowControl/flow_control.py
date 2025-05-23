#conditional statement(if,elif,else)

# if:- if is a keyword, and statement, if condition True the statement will execute or not to be.

'''
syntax

if condition(True or False:
    statements
    .
    .
    .

jbjdv

'''
from crypt import methods
from curses.ascii import controlnames

from django.contrib.admindocs.utils import replace_named_groups
from numpy.lib.recfunctions import structured_to_unstructured
from numpy.ma.core import append
from pandas.core.ops.mask_ops import raise_for_nan
from reportlab.lib.PyFontify import keywordsList
from sqlalchemy.dialects.mysql import insert

'''name = input('Enter a name:-')

if name=='Rahul':
    print('Good morning rahul')'''

'''
take user input help of input function
check the number is even or not
if its is even , print number is even
'''

'''num = int(input('Enter a number:-'))

if num%2==0:
    print('even')'''

# else:if the condition is failed , then else will execute.

'''
its not a mandatory statement, based on requirement , we will write.
'''

'''num = int(input('Enter a number:-'))

if num%2==0:
    print('even')
else:
    print('odd')'''

'''
a take string input from user.
check the string is pallindrom or not

mam
madam
'''

'''st = input('Enetr a string:-')

if st ==st[::-1]:
    print('its a pallindrom')
else:
    print('its not a pallindrom')'''


'''
check the the list 67 is avl or not.
if avl then print it

'''

'''li = [19,23,67,45,32,10]

if 89 in li:
    print(67)
else:
    print('not present')'''

'''
i have two number and its take from user, wants check which one is the biggest num

'''
'''a = int(input('Enter ur 1st number:-'))
b = int(input('Enter ur 2nd number:-'))

if a>b:
    print(a,'is the biggest num')
else:
    print(b,'is the biggest num')'''

# elif:- elif actually used for multicondition statement

'''synatx

if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
.
.
.
else:
    else_statement

'''

'''city = input('Enter ur city:-')

if city=='jaipur':
    print('city of joy')
elif city =='bhubaneswar':
    print('temple city')
elif city == 'banglore':
    print('silicon city')
elif city == 'mumbai':
    print('filmy city')
else:
    print('we dont other city idea')'''

# i have three number and its take from user, wants check which one is the biggest num

'''a=int(input("enter 1st no-"))
b=int(input("enter 2nd no-"))
c=int(input("enter 3rd no-"))

if a>b  and a>c:
    print(a,'is the biggest number')
elif b>c:
    print(b, 'is the biggest number')
else:
    print(c, 'is the biggest number')'''

#iterative statement
'''
for :- collectional iteration(ds and str)
while :- conditional iteration( based on logic)


for :- for is a loop, its iterate over though the collection like str, list, tuple dict...

syntax

for var in collection_name:
    statement
'''

'''box --- apple, ban, gra, che 
apple
ban
gra
che
'''

'''li = [45,78,23,21,89,54]

for var in li:
    print(var)'''



'''li = [67,54,24,21,89,86,33,20]

even_li = []
odd_li = []

for var in li:
    if var%2==0:
        even_li.append(var)
    else:
        odd_li.append(var)

print(even_li)
print(odd_li)'''

'''li = [12,6.78,'qwerty',6+9j,'vbnm',90,'78']

str_li = []

for var in li:
    if type(var)==str:
        str_li.append(var)

print(str_li)'''


'''li = [10,20,30,40,50]

sum = 0
mul = 1
for var in li:
    sum = sum+var
    mul = mul*var
print(sum)
print(mul)'''

'''data strcture means collection , list, tuple, set,fzsey, bytes,bytearray,range,dict
string --- collections of substring'''

# syntax
'''
for var in collection_name:
    statement

'''

'''li = [10,20,30,40]

for var in li:
    print(var)
'''

#range iteration
# range:- range is a datatype in python, it's  genegrate sequence of numbers

# range(start,end+1,steps)

'''for i in range(2,10,2):
    print(i)'''

'''for i in range(100,106):
    print(i)'''

# star programming

# *
# *
# *
# *
# *

# for i in range(5):
#     print('*')


# * * * * *

'''for i in range(5):
    print('*',end='')'''

# *
# **
# ***
# ****
# *****

'''for i in range(1,6):
    print('*'*i)'''


# *****
# ****
# ***
# **
# *

'''for i in range(1,6):
    print('*'*(6-i))'''

# *****
# ***
# *

# for i in range(1,6,2):
#     print('*'*(6-i))

# *****
# ***
# *
# ***
# *****

'''for i in range(1,6,2):
    print('*'*(6-i))
for i in range(3,6,2):
    print('*'*i)'''


#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# nested loop:- loop inside a another loop know as nested loop.

# for i in range(5):#i = 0, 1 ,2, 3, 4
#     for j in range(5):#0,1,2,3,4
#         print(i,j)

# out exec --- inside inner --- inner exec


# for i in range(3):
#     for j in range(2):
#         print('TREENETRA')

#i = 0   j = 0,1   --- 2
# i = 1  j = 0,1 --- 2
#i = 2  j = 0 ,1 --- 2


'''for i in range(2,6,2):
    for j in range(3):
        print('TREENETRA')'''

# i = 2 , j = 0,1,2
# i = 4 , j = 0,1,2
# 6 times


'''li = [67,56,21,89,43,12,44,32,18,62]
# [12, 18, 21, 32, 43, 44, 56, 62, 67, 89]

n = len(li)

for i in range(n):
    for j in range(n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]

print(li)'''

#how to use for loop in a dictionary
'''di = {'Name':'A','Age':27,'Address':'Odisha'}

for k,v in di.items():
    print(k,v)'''


'''li = [
    {'Name':'A','Age':27,'Address':'Odisha','Salary':60000,'Language':['Python','SQL']},
    {'Name':'B','Age':25,'Address':'AP','Salary':78000,'Language':['Python','Java']},
    {'Name':'C','Age':23,'Address':'AP','Salary':33000,'Language':['Java','Golonag']},
    {'Name':'D','Age':31,'Address':'WB','Salary':41000,'Language':['SQL','Plsql']},
    {'Name':'E','Age':21,'Address':'WB','Salary':42000,'Language':['.Net','Python']},
    {'Name':'F','Age':22,'Address':'Odisha','Salary':82000,'Language':['Python','Java']},
    {'Name':'G','Age':29,'Address':'Odisha','Salary':91000,'Language':['Python','SQL']}
]

for i in li:
    if i['Address']=='Odisha' and 'SQL' in i['Language']:
        i['Language'][i['Language'].index('SQL')]='PLSQL'
print(li)'''

# fetch address is odisha and sql in language
'''for i in li:
    if i['Address'] == 'Odisha' and 'SQL' in i['Language']:
        for j in range(len((i['Language']))):
            if i['Language'][j]== 'SQL':
                i['Language'][j]= 'PSQL'

print(li)'''


#fetch the name those age are greater than 25.

'''for i in li:
    if i['Age']>25:
        print(i['Name'])'''

'''for i in li:
    if i['Salary']>50000:
        print(i['Name'],i['Age'])'''

'''sum = 0
for i in li:
    if i['Salary'] < 50000:
        sum = sum +i['Salary']
print(sum)'''



#conditional iteration:-
#while loop.:- when the condition is satisfy or full-fill based on that , it will itrate the loop.

'''
while True:
    statements
'''

'''while True:
    print(1)'''

# print 1 to 10.


'''num = 1

while num<=10:
    print(num)
    num = num+1'''

'''num = 25
sum = 0#77

while num<=35:
    sum = sum+num
    print(num)
    num = num+1
print(sum)'''

#reverse a number

# 1234 --- 4321

# 4 , 3 , 2 , 1

'''num = 1234
reversed_num = 0

while num>0:
    digit = num%10
    reversed_num = reversed_num*10+digit
    num =num//10

print(reversed_num)'''

# Transfer statement(break, continue, pass)
#break :- based on the condition it will stop the iteration, once it's stop the iteration, loop is terminate.

'''for i in range(10):
    if i==7:
        break
    print(i)'''


#continue :- skip the iteration. based on the condition it will skip the iteration and move to next one.

'''for i in range(1,11):
    if i%2==0:
        continue
    print(i)
'''


#pass:- pass the statement , if programer have nothing.

# for i in range(1,10):
#     pass

#
# while True:
#     pass

'''def f1():
    pass'''


# core python
'''
keywords
identifiers
data type and data structured
data strctute methods
operator
input and output
flow control
    conditional st.(if,elif,else)
    iterative st.(for,while)
    transfer st.(break,continue, pass)'''

# Advance python

'''functions
modules and packages
file handeling
opps
exception handeling
regular expression.'''











