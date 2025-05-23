'''
Datatype:- 6 types
In python there are 14 types of data is avl.

int
float
complex
boolean
string
None
-----------------
list
tuple
set
frozenset
bytes
bytearray
dictionary
range


those data types are in python inbuilt function and as well as python class.

'''

'''var = 10.89
print(type(var))'''

#complex
# Real num (int and float)+ imaginary num = complex num
#
# -1 , -4, -9 ---- comlexity num --- i , j , k---- j

'''var = 8+9j
var1 = 2+3j

print(type(var))
print(var/var1)'''

#boolean :- conditonal check
# True  False
# print(10<12)
'''print(True+True)
print(True+False)
print(False+False)'''

'''a = 3
a= a-3
print(a)
print(type(a))


b = None
print(type(b))'''
'''3 mangoe 
1-- bhai  --- 2
1-- behen --- 1
1-- mummy --- 0

kuch v mango nehi hai -- nothing'''

'''def f1():
    a = 10

print(f1())
'''

# string:- charcters:- string is a collection of substrings. and its
# st = "drgfhjDRJGFHKJ345678#$%^&* jbhgf  "
# print(type(st))

#triple cot :- doc string (documentation of string) and multiline comment.

# def bank_statement():
#     '''this function fetch bank statement of each cutomer based Account num and ifsc code'''
#


#variables and garbage collection
# string slicg
#string methods


#variables and garbage collection

'''object--- location ---- physical point.
|
|
exitance 


data ---- location --- physical point


data ---- variable --- store --- variable --physical point
'''
# how to check the location in python ?
'''a = 20
print(id(10))
print(id(a))'''

'''variable behaves a datatype only, those data are store in that time.'''

'''a = 10 #its provide 10 -- location-- auto delete --- garbage collection process

a = 20 #its provide 20 -- 

print(a)'''

#where we store our garbage data, this point is known a garbage collector.


# string
'''st = ''
print(type(st))'''

# what is string slicing?-- peace

st = 'Bhubaneswar'
#bhu--- index-- position-- exctract

# Syntax

'''
[] --- operator of slicing
variable[start:end+1:steps]
'''
# print(st[0:3:1])



'''
python is zero based index. means its start from 0
+ve(left to right) , -ve(right to left)

'''


''' 
-10  -9    -8   -7  -6  -5   -4  -3  -2   -1
B    H     U    B    N   E   S   W   A    R
0    1     2    3    4    5  6   7   8    9

'''


# st = 'Bhubneswar'
'''var = st[3:7]
print(var)'''
# B    H     U    B    N
#BUN

'''var = st[0:5:2]
print(var)'''

# var = st[-7:-4]
# print(var)

'''var = st[-4:]
print(var)'''

# 1.want to revsere the string? #rawsenbuhB
# 2.raws

'''st = 'Bhubneswar'
var = st[::-1]
print(var)
'''
# start --- end position
#
# end +1--- start
#
# step   -  -1

'''st = 'Bhubneswar'#raws #enb
# var = st[:-5:-1]
# print(var)
var = st[-5:-8:-1]
print(var)'''

# string -- mathnetical( +, *)

'''addition :- string add with a another string only
mul :- string mul with a int only'''

'''print('a'+'b')
print('a'*3)
'''

# unique number genrate

# first char+ dob yyyy
# server ec2 --- email first char+gen otp
# sbin0010917

'''first = 'Rahul'
last = 'Sachdev'
dob = '20/9/1997'
vechile = 'OD-14-K-0108'
house = 'Cheand-MIG-00123'
'''
# create a uniqe pass
'''
first name first two char
last name last two char
dob -- yyyy
vechile :- RTO -- 14
house - MIG

Raev199714MIG

'''


import math
print(math.factorial(5))









