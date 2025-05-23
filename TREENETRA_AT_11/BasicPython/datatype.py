#int, float, complex ,bool

# -infinity ------- +infinity ----- complete

# a = 105478695483765457869706855768
# print(type(a))

# -infinity ------- +infinity ----- all decimal numbers

# a = 57868974.867
# print(type(a))


#complex( Real + imag)

# Real - may be it's a int, or a float --    -inf  to +inf --- all numbers(whole + decimal)
# imag :- if a number have no solution then the number is imag

'''c = 8+9j
print(type(c))
print(c.real)
print(c.imag)'''

'''a = 10+9j
b = 9+10j
print(a+b)'''

#bool --- True   False
'''print(10>11)'''


# bag = ['apple','orange','gra']
# print('orange' in bag)
# print('chiku' in bag)


'''int, float, complex, bool

str

list, tuple, set , frozenset, bytes, bytearray

dict, range ,None
'''

# String:-

# var = 'SRDTFYGJUHdtyfulgk3546789#%$^&*O('
# print(type(var))
#
# var1 = "SRDTFYGJUHdtyfulgk3546789#%$^&*O("
# print(type(var1))

# triple cot  - single Triple , double triple cot
''''''
""""""

'''what is doc string :- documentation string'''
# triple cot use for multiline comment


"""def passcode_retrival():
    '''this function is written atm card passcode retrival process intialization'''
    bswcjk
    kc bns
    bsc
    dcbj"""


#hsdvcjkwdcbklwecbvjkwebvwejbgvwbwjebcjwbv
'''klwc
sd not dsjc bytes
jksd bytes
jhsdfv'''

#string slicing
#
# s = 'Banglore'
# print(s[1:3:1])
# print(s[4:8])
# print(s[-7:-5])
# print(s[1:])

# Mathmetical imp.

#add

# we can add two string

# s = 'qwert'
# s2 = 'tyuiop'
# print(s+s2)

#mul

# s = 'Bang'
# print(s*3)
#strings methods

# name = 'chandra sekhar'
# dob = '17/03/1997'
#
# password = name[0:4]
# dob = dob [-4:]
# print(password+dob)


# name =  'Dhanchad Kore'
# dob = '19/07/1996'
# area = 'Bhubaneswar'
# plot_num =' #17, Girinag,'
# brach = 'Banglore'
#
# # OP :- hanchad07nesw17lor
# print(name[1:8]+dob[3:5]+area[-5:-2]+plot_num[1:3]+brach[-4:-1])

# string methods
# mutable   immutatable


# s = 'bhubaneswar'
# print(dir(s))
'''[ 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
  'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
  'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust',
  'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''

# var = s.capitalize()
# print(var)

#upper and lower and swapcase
# s1 = 'qwertGVJHwer'
# var = s1.upper()
# print(var)
#
# var2 = s1.lower()
# print(var2)
#
# var3 = s1.swapcase()
# print(var3)

#stratswith and endswith

# s = 'Delhi'
# print(s.startswith('d'))
# print(s.endswith('I'))

#find and index

# s = 'bhubaneswar'
# print(s.index('E'))
# print(s.find('Ba'))



#strip, split,join,format

st = '      Krishna     '
print(st.strip())

#format

'''a = 10
b = 5
result = a+b
print(f'the addition is:-{result}')

cap,upper,lower,swapcase,strtswith,endswith,strp,format,find, index

count,split,join'''

# s = 'wertyu'
# var = s.capitalize()
# print(s)

# a = int(input('data1:-'))
# b= int(input('data2:-'))
# result = a+b
#
# result = a+b
# print(f'format is resukt is:- {result}')

#capilize, lower,upper,startswith,endswith,swapcase,
#find,index, strip, format

#count

'''st = 'i love india, india is best'
print(st.count('z'))
print(len(st))
'''

# Data Strc

# List --- hetrogeneous

'''
1.list is data strc of python
2.list is enclode in squre bracket.
3. every element seprate with another element with help of comma
4.list is a hetrogeneous object type
5.list is accepting duplicate element
6.list is allow indexing 
7.list is mutable datatype
8.list is growable in anture
'''

'''li = [10,78.90,7+9j,True,'qwerty',[90,90],10,20,78.90,True,True]
print(type(li))
print(li)
print(len(li))'''

# mutable    immutable

#string split:-

"""name = 'Asish Rahul Hemu Rolex Gupta Kshitish Utkal'
var_li = name.split()
print(var_li)"""

#string join
"""names = ['Asish', 'Rahul', 'Hemu', 'Rolex', 'Gupta', 'Kshitish', 'Utkal']

st = " ".join(names)
print(st)"""

# li = [10,20,30,40]
# print(dir(li))

# python list indexing
'''li[0]=100
li[3]=400
print(li)'''


# 'append', 'clear', 'copy',count, 'extend', 'insert', 'pop', 'remove', 'reverse', 'sort'

#append :-
'''li = [10,20,30,40]
li.append('qwertry')
print(li)'''

#insert
'''li = [10,20,30,40]
li.insert(1,15)
print(li)'''

#extend

'''li1 = [10,20,30,40]
li2 = ['Qwerrty','Balckberry','Asha200']
li1.extend(li2)
print(li1)
print(li2)'''

#pop
'''li1 = [10,20,30,40]
li1.pop()
print(li1)'''

#remove
'''li1 = [10,20,30,40,10,203,40]
li1.remove(20)
li1.remove(10)
li1.remove(10)
print(li1)'''

#clear
'''li1 = [10,20,30,40,10,203,40]
li1.clear()
print(li1)'''

#copy
'''li1 = [10,20,30,40,10,203,40]
li2 = li1.copy()
print(li2)'''

#count
'''li1 = [10,20,30,10,20,30,10,20,40,40,90]
print(li1.count(90))'''

#reverse
'''li1 = [10,20,30,10,20,30,10,20,40,40,90]
li1.reverse()
print(li1)'''

#sort
'''li = [90,78,35,21,34,56,70,21,32,76,45,34,69]
li.sort()
# li.sort(reverse=True)
print(li)'''

#Tuple

'''
1.Tuple is data strc of python
2.Tuple is enclode in () bracket.
3. every element seprate with another element with help of comma
4.tuple is a hetrogeneous object type
5.tuple is accepting duplicate element
6.tuple is allow indexing 
7.tuple is immutable datatype
8.tuple is not growable in anture
'''

# tu = (10,89.89,9+9j,True,'qwertyu',[678,78],10,101,0)
# # print(type(tu))
# # print(tu[0])
# print(dir(tu))


#Set and Frozenset

'''
1.Set is data strc of python
2.Set is enclode in {} bracket.
3. every element seprate with another element with help of comma
4.Set is not a hetrogeneous object type
5.set  is not accepting duplicate element
6.set is not allow indexing 
7.set is mutable datatype
8.set is growable in anture

'''

'''se = {57,89,56,'5678',5+9j,True,89,89,89,45,45,57}
print(dir(se))
print(se)'''

 # 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',  'pop', 'remove',  'union', 'update'

 #add

'''se = {90,78,67,45,90,90}
se.add(100)
se.add(80)
print(se)'''

#clear
'''se = {90,78,67,45,90,90}
se.clear()
print(se)'''

#pop
'''se = {90,78,67,45,90,90}
se.pop()
print(se)'''

#remove
'''se = {90,78,67,45,90,90}
se.remove(67)
print(se)'''

#difference

'''se1 = {90,89,76,56,34,23}
se2 = {34,90,23,67,43,21}
print(se1.difference(se2))
'''

#intersection
'''se1 = {90,89,76,56,34,23}
se2 = {34,90,23,67,43,21}
print(se1.intersection(se2))'''

#union
'''se1 = {90,89,76,56,34,23}
se2 = {34,90,23,67,43,21}
print(se1.union(se2))'''


#frozenset

#Type Casting

# int
# float
# complex
# bool
# str
#
# list
# tuple
# set
# frozenset
# bytes
# bytearray
#
# dict
# range
# None

'''a = 10
b = dict(a)
print(b)
print(type(b))'''

'''lis = [10,20,30,40,10,20]

b = frozenset(lis)
print(b)
print(type(b))'''

#bytes and bytearray

'''lis = [10,20,30,40,10,20]

b = (bytearray(lis))
print(b)
print(type(b))'''

#dictionary

'''di = {'Name':'Jaga','Age':27,'Salary':81000,'location':'Marathahalli'}
print(type(di))
print(dir(di))'''

# 'clear', 'copy', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values

'''di = {'Name':'Jaga','Age':27,'Salary':81000,'location':'Marathahalli','Name':'Balia'}
print(di)'''


# di = {'Name':'Jaga','Age':27,'Salary':81000,'location':'Marathahalli'}
# print(di['salary'])
# di['Salary']=87000
# di['pincode']=751003
# print(di)

#clear
'''di.clear()
print(di)'''

#get
# print(di.get('location'))

#keys
# print(di.keys())

#values
# print(di.values())

#items()
# print(di.items())

#setdeafult
'''di.setdefault('pincode',751003)
print(di)'''

#uodate
'''di = {'Name':'Jaga','Age':27,'Salary':81000,'location':'Marathahalli'}
di2 = {'pincode':751003,'police_station':'mara','post':'HAL'}

di.update(di2)
print(di)'''


# pop
'''di = {'Name':'Jaga','Age':27,'Salary':81000,'location':'Marathahalli'}
di.pop('Age')
print(di)'''

#popitem
'''di = {'Name':'Jaga','Age':27,'Salary':81000,'location':'Marathahalli'}
di.popitem()
print(di)'''


#tuple,set,fzset,byte,bytearray,type casting,
# dictionary


# tu = (10,203,3,729)
# print(dir(tu))

'''di = {'Name':'Jaga','Age':27,'Salary':81000,'location':'Marathahalli','pincode':751003,'police_station':'mara','post':'HAL'}

li = ['Salary','pincode','post']

for i in li:
    di.pop(i)
print(di)'''

















