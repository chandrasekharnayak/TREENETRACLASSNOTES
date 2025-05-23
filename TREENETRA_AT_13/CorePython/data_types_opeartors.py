#keywords

'''import keyword
print(keyword.kwlist)

li =['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
 'with', 'yield']
print(len(li))
'''

# Data Type and Data Str.
'''14 Types of data

int:- integer
float :- float
complex :- complex
bool :- boolean
str :- string
list :- list
tuple :- tuple
set   :-set
frozenset :- fzset
bytes :- bytes
bytearray :- bytearray
range :- range
dict :- dictionary
None :- None'''



# a = 8+9j
# b = 2+3j
# print(a+b)
# print(type(a))

#bool
# True False

# li = [10,20,30]
# print(100 in li)

#print(10<20)

'''print(True+True)
print(True+False)
print(False+False)'''

#string:-
# var = 'data'

# def add():
#     '''this function is written for addition'''

# s = 'ankit111'
# print(dir(s))


'''a = 10
print(id(a))
print(id(10))

# print('line  63:-',a)
#
#
a = 20
print(id(a))
# print('line  67:-',a)'''


#String slicing
# st = 'bhubaneswar'
# print(st[0:4])
# print(st[::-1])

# s = 'raghav patel surya'
# print(s[0:12:3])

'''name = 'Rishab Patel'
dob = '20/06/1998'

password = name[0:4]+dob[-4:]
print(password)'''

# print('AB'+'YZ')
# print('AB'*'AB')

'''s = 'utkal'
# print(len(s))
print(type(s))'''
'''
capitalize
swapcase
endswith
startswith
lower,upper

find
index
count
replace



'isalnum', 'isalpha',isdigit,islower,isupper

strip,lstrip,rstrip
join
split
format'''

# s = 'I hAve'
# print(s.endswith('e'))

# print(s.lower())

# print(s.swapcase())
'''s =s.capitalize()
print(s)
'''
# print(s1)

'''s = 'qwerty'
print(s.index('z'))'''

#count

'''s = 'i love india, india is best'
print(len(s))
print(s.count('i'))'''
'''s= 'Li Lucy'
print(s.replace('Li Lucy','H'))'''

'''s = '123DFGH%^&'
print(s.isalnum())
'''

'''s = '         jggh         '
print(s.lstrip())'''

#split

'''name = 'Mahesh Ramesh Rohan Tushar'
print(name.split())
'''

#join

'''li = ['Mahesh', 'Ramesh', 'Rohan', 'Tushar']
var = '=='.join(li)
print(var)'''


#format
# var = 10
#
# print(f'variable value is {var}')

'''list,tuple
set,frozenset
bytes,bytearray
dict'''

# var = [10,20.89,8+9j,True,'Raghav',10,10,20,102,20,[98909,99],{90,89},{'A':1}]
# var_tup = (10,20.89,8+9j,True,'Raghav',10,10,20,102,20)
#
# print(type(var))
# print(dir(var_tup))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

'''l2 = [90,80]

li= [10,20,30]
li.append(l2)
print(li)
[10,20,30,[90,80]]'''

# insert
'''li = [10,20,30]
li.insert(1,15)
print(li)'''

#extend

'''l1 = [10,20,30]
l2 = [90,80,70]

l1.extend(l2)
print(l1)
print(l2)'''

#clear
'''li = [10,2,34]
li.clear()
print(li)'''

#pop

'''li = [10,20,30,40]
print(li.pop())
print(li)'''

#remove
'''li = [10,20,30,40]
li.remove(20)
print(li)'''

'''li = [10,20,30,10,10,20,30]
print(li.count(10))

print(li.index(10))'''


'''li = [10,67,65,32,34,78,90,43]
# li.reverse()
# print(li)


li.sort(reverse=True)
print(li)'''

'''li = [10,20,30]
var = li.copy()
print(var)'''

#set

# se = {10,20.89,8+9j,'rtyyy',(10,10,20),10,20,10,20}
# print(type(se))
# print(se)

# li = [10,20,30,40]
# li.insert(10,89)
# print(li)

#Type casting

'''int
float
complex
bool

str'''

# a = 10.9
# b = list(a)
# print(type(b))
# print(b)


'''range
None'''

'''list
tuple
set
frozenset
bytes
bytearray
dict'''

'''li = [10,20,30,45,121,256]

tu = bytes(li)
print(type(tu))
print((tu))'''


#dict

di = {'Name':'Krishna','Age':27,'Salary':10000000,'MN':'Krishna'}
# print(di['Name'])
# var['key_name']
# di['Name']='CS'
# print(di)

# print(dir(di))

# ['clear', 'copy', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# set = {10,20}
# di = {'Name':'Krishna','Age':27,'Salary':10000000,'MN':'Krishna'}

# set.clear()
# print(set)
# di.clear()
# print(di)

# var = di.copy()
# print(var)

# print(di.get('Age')
# print(di.items())
#
# di.setdefault('Pincode',890877)
# print(di)

# di.update({'A':'B','C':'D','E':'F'})
# print(di)

# di.pop('Salary')
# print(di)


# di = {'hhj':10,9:'hj'}
# print(di)


'''def f1():
    a = 10

print(f1())'''



                    # Operator
'''Arithmetic Op
Relationship op -- comparision
Logical
Assignment
Bitwise 
Special
identity op -- is
membership op -- in

'''
'''+,-,*,/
//- floor div
** :- exponent
%:- modulo'''
# print(10//3)

# print(2**3)
# print(10%6)

# rel
# >,>=,<,<=,==,!=


'''#logical(and,or,not)

and
T   T    T
T   F    F
F   T    F
F   F    F

or

T    T   T
F    T   T
T    F   T
F    F   F



not True
not False'''

#assigmenet
# a = 10
# a+=20
# print(a)


# a = 10
# b = 20
# print(a is b)

# li = [10,20,30,50]
# print(100 in li)

#How to take data from end user.

# var = eval(input('Enter your num:-'))
# print(type(var))














