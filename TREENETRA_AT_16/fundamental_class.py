
# a = 20
#
# a = 'qwerty'
# print(id(a))
#
# print(id(10))

# a = 3.90
#
# print(type(a))
# b =
# print(b
#
#       low ------> higherbits

# a = 10.86
# print(type(a))

# c = 10+7j
# print(type(c))

'''a = 10<20
print(a)
print(type(a))'''
from email.quoprimime import body_length

from PIL.BdfFontFile import bdf_spacing

'''st = "RERTEghfg7564&^%^&%$^/}{}"
print(type(st))
'''

# Multiline String :-
'''hvherivhri
ljvoerjvo]
kvhreihvi
iehviewrhv
ievhier
iegvie'''

'''a = 'treenetra'
print(dir(a))

slicing'''

# var = Real +img

'''var = 10+7i
print(type(var))'''

var = 'kncdksncli67756JBHJ7656757^&%&^%^&'

var1 = "gvhjvhjHVGHKV576567>:>"

# string scling, and methods

'''
kgjygfyhhh
jhfuygfuiy
jhfuyy
fyufyu
'''

# what is slicing?
st = 'Banglore' # indexing or position

'''
+VE - positive indexing(left to right -- 0)
-VE - negetive indexing(right to left -- -1)
Pytho is a zero based index
'''
'''
-8  -7  -6  -5  -4  -3  -2   -1
B   A   N   G   L   O   R    E
0   1   2   3   4    5   6   7'''

'''
syntax
variable[start:end+1:step] 

'''

'''name = 'chandra sekhar'
first_4_char = name[-10:-7]
print(first_4_char)'''

# application :- wants to create a unique alphanumeri/passowrd

'''name = 'ABCDEFGH'
dob = '17/04/1998'

password = name[0:4]+dob[-4:]
print(password)'''

# string (mathmetical opeartion)(+,*)
# string add with a another string
# print('A12'+'B12')

#string multuple with a int only
# print('A'*30)


'''name = 'abc'
surename = 'patil'
dob = '17/3/1989'
city = 'Indore'''

'''name first char 3 time
surename last 3 char
dob month only
city :- complete string

password = aaatil3Indore'''

'''var = name[0]*3+surename[-3:]+dob[3]+city
print(var)'''

'''a = 'ram'
reverse the string with help of string slicing'''

# what is a methods?

'''a = 'abcd'
print(type(a))
print(dir(a))'''

''', ('capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 
   'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
   'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
   'rsplit', 'rstrip', 'split', 'splitlines', 
   'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill)'''



#capitalize
# st = 'qwerty'
'''var = st.capitalize()
print(var)'''

#upper
'''
st = 'QhgHGYUbhbh'
var = st.upper()
print(var)'''

#lower
'''st = 'QhgHGYUbhbh'
var = st.lower()
print(var)'''

'''# swapcase
st = 'QhgHGYUbhbh'
var = st.swapcase()
print(var)'''

#startswith
'''st = 'hi all'
print(st.startswith('h'))'''

#endswith
'''st = 'hi all'
print(st.endswith('y'))'''

'''st = ' hj   '
print(st.isspace())'''

'''st = 'i love india'
var = len(st)
print(var)
'''

#count
'''st = 'i love india'
print(st.count('e'))
'''

#strip,rstrip,lstrip
'''
st = '          jhjkhui          '
var = st.strip()
print(var)
'''

#replace

'''st = 'ji jack'
var = st.replace('ji','hi')
print(var)'''

#split

'''st = 'abhay abhiman abhilash abhilipsa abhishek'
var = st.split()
print(var)'''

#splitlines

# st = '''jhjg
# jkgj
# jkbjh
# jkkjh
# '''
#
# var = st.splitlines()
# print(var)


#join:-
'''collection = ['A','B','C','D']
# 'ABCD'

var = ''.join(collection)
print(var)'''

#format :- fstring

'''a = 10
b = 20
res = a+b

print(f'{a} addition with {b} and the result is {res}')'''

'''var = data --- but variable only store a single in a single time.

var = data1,data2,data3 ---- this not possiable

collections --- box -- those store nth number of elementsal data--
when we can declare a collection infornt variable , variable consider this a single data'''


# what is data structutre?  ---- collection
# where we will staore multiple elemenet in a single box.
# var = data---

'''list
tuple
set
frozenset
bytes
bytearray
dictionary

None
range

list_of_students = 'sritam','Antaryami','debasish'''

'''what is list?

list is a datatype and a data strcture in python, it store multiple element inside him. list is a collections

behaviour:-

it is enclosed in [], and [] represent him as a list.
list is a hetrogenous object type.(all kind of data should be allowed)
here indexing is possiable (positioning)
duplicate element allowed in list
it is manipulation  in nature(mutability)
'''

# var1 = [1,7.8,6+9j,True,'uiop',[89,90],(67,89),1,1,1,1,1,1,1,1]
# var1= [1,2,3,4]
# # print(type(var))
# # print(var[-3])
# print(var1)
# print(type(var1))

'''var[0]=100
print(var)'''

'''import numpy as np

var =np.array([1,2,3,4])
print(var)
print(type(var))'''

'''what is tuple ?

behaviour:-

it is enclosed in (), and ()represent him as a tuple.
list is a hetrogenous object type.(all kind of data should be allowed)
here indexing is possiable (positioning)
duplicate element allowed in tuple
manupulation is not possibale(immutable'''

# tu = (1,7.8,6+9j,True,'uiop',[89,90],(67,89),1,1,1,1,1,1,1,1)
# print(type(tu))


# list methods


# print(dir(li))

# append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort

#append :- insert a single data in  a list last position

'''
li = [1,2,3,4]
li.append((90,91))
print(li)
'''
#insert:- insie a single data, in given position

'''li = [1,2,3,4]
li.insert(2,'qwerty')
print(li)'''

#extend :- merge two list.

'''li1 = [10,20,30,40]
li2 = [11,21,31,41]

li1.extend(li2)
print(li1)
print(li2)'''

#pop:- remove a singe data in the lst position of list.
'''li1 = [10,20,30,40]
li1.pop()
print(li1)'''

#remove :- remove  a perticular data.
# li1 = [10,20,30,40]
# li1.remove(20)
# print(li1)


#clear:- remove the all the element from a list and just return a empty []

'''li = [10,20,30]
li.clear()
print(li)'''

#copy

'''li = [10,20,30]
var = li.copy()
print(li)'''

'''import copy
#shllow copy
#deep copy

li = [10,20,[30,31]]

var = copy.copy(li)

var[2][0]=300
print(var)
print(li)
'''

'''li = [90,76,56,34,89,23,121,31,345,32]
li.sort()
li.reverse()
print(li)'''

#count :- count the occurnace of the list element

'''li = [1,2,1,2,1,2,3,4,5]
print(li.count(5))'''
'''li = [1,2,1,2,1,2,3,4,5]
print(len(li))'''

'''tu = (1,2,34)
print(dir(tu))'''

# set, frozenset,bytes,bytes

'''set:- 


behaviour:-

it is enclosed in {}, and {}represent him as a tuple.
set  is a  contain the data or element.
here indexing is not possiable (positioning)
duplicate element sould not allowed in tuple.
manupulation is  possibale(mutable)
'''

'''se = {1,7.8,8+9j,True,'trung',1,1,7.8}
print(type(se))
print(dir(se))
se.clear()
print(se)'''

# frozenset

# type casting or type coresion
'''when we want to chnage our data with a another type of data, its called casting, 

int,  float, complex, bool
str
list,tuple,set,frozenset,bytes,bytearray'''

# a = 10
# b = bool(a)
# print(b)

'''li = [10,20,30,10,20,30,30,40]
con = dict(li)
print(con)'''

'''a = [10,20]
st = str(a)
print(st)
print(type(st))'''


'''st = '10'
a = int(st)
print(a)'''


#bytes and byterarray
'''li = [38,39,40,255]
by = bytearray(li)
print(by)'''

#dictionary
'''dict is key and value pair, key should be always unq, value may be same. 
a key value pair separate with each other help of : (colon)
and a dictionary enclosed in {}.
'''

di = {'Name':'Maonj','Age':23,'Manager':'Satish',}
'''
syntax
var[key]
'''
'''var = di['Manager']
print(var)'''

'''di['address']='Bhubaneswar'
print(di)'''



'''di1 = {'Name':'Gudu','Age':23,'Manager':'Gudu',}
print(di1)'''

'''table

cl1     cl2       cl3

R11     R12     R13
R21    R22     R23
R31    R32     R33


Name       Age      MngName   (keys)
Manoj       23        Satish         (values)  
Ayesha     20        Rukmini
Gudu         27       Gudu'''




# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

'''di1 = {'Name':'Gudu','Age':23,'Manager':'Gudu'}

di1.clear()
print(di1)'''

'''di = {'Name':'Gudu','Age':23,'Manager':'Gudu'}

qw = di.copy()
print(qw)'''

# shallow copy and deep copy
import copy

'''copy.copy()''' #shallow copy

'''li = [45,78,[90,91],[67,89]]

ty = copy.copy(li)
ty[3][1] = 68
print(ty)
print(li)
'''

'''copy.deepcopy()'''#deep copy

'''li = [45,78,[90,91],[67,89]]

ty = copy.deepcopy(li)
ty[3][1] = 68
print(ty)
print(li)'''


#get:- provide the key , it's return the value
'''di = {'Name':'Gudu','Age':23,'Manager':'Gudu'}
var = di.get('Age')
print(var)'''

#items:- fetch the key-value pair in a tuple.
'''di = {'Name':'Gudu','Age':23,'Manager':'Tushar'}
var = di.items()
print(var)
'''

#keys :- return the dictionary keys in a list.
'''di = {'Name':'Gudu','Age':23,'Manager':'Tushar'}
var = di.keys()
print(var)'''

#values :- return the dictionary values in a list.
'''di = {'Name':'Gudu','Age':23,'Manager':'Tushar'}
var = di.values()
print(var)
'''

#popitem:- it will delete last key and value pair.
'''di = {'Name':'Gudu','Age':23,'Manager':'Tushar'}
di.popitem()
print(di)'''

#pop:- provide a key, it will delete same key and value pair
'''di = {'Name':'Gudu','Age':23,'Manager':'Tushar'}
di.pop('Name')
print(di)'''

#setdefault:-provide a key and value it will add on your dictionary
'''di = {'Name':'Gudu','Age':23,'Manager':'Tushar'}
di.setdefault('Address','BBSR')
print(di)'''

#update :- merge the two dict.

'''di1 = {'Name':'Gudu','Age':23,'Manager':'Tushar'}
di2 = {'Address':'BBSR','Pin':789000}
di1.update(di2)
print(di1)'''

#None:- when you have nothing to return the python represent this data as a None. None means nothing.

'''a =None
print(a)
'''

'''def f1():
    a= 10

print(f1())
'''


