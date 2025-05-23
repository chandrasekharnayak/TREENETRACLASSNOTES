'''list  is a collection and it's behave like hetrogenous(allow all the inside him) object types.
list enclosed in squre bracket, []
every element separate with another element help comma.
list is allow the indexing, position is imp.
list is allow the duplicate element.
list is growbale and deletebale element in nature.
list is a mutable

'''
from webbrowser import Opera

# li = [10,7.90,8+9j,'hghj',[10,20],(89,90),10,101,10,10,10]
# print(type(li))
# li[0]= 100
# print(li)

# print(dir(li))
# append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#append :- add a single value in the last position of the list.

'''li = [10,20,30,40]
li.append(50)
li.append([12,3])
print(li)'''

#insert:- add a single element in a specific position

'''li = [10,20,30,40]
li.insert(1,15)
li.insert(2,(90,89,78))
print(li)'''

#extend:-

'''li1 = [10,20,30,40]
li2 = [89,90,70,60]
li1.extend(li2)
print(li1)
print(li2)
'''

#clear:- delete all the elemenets from the list and return a empty list.

'''li = [10,20,30,40]
li.clear()
print(li)'''

#pop:- remove the element from last index in a list

'''li = [10,20,30,40]
li.pop()
print(li)'''

#remove :- delete the specific  element in a list

'''li = [10,20,30,40,50]
li.remove(30)
print(li)'''

#copy:- copy the list in a another avriable.

'''li = [10,20,30,40]

li2 = li.copy()
print(li2)
'''

#reverse:- reverse the list all elements

'''li = [10,34,20,31,30,78,90,72,40,45,67,50]
li.reverse()
print(li)
'''

#sort :- accending order .

'''li = [10,34,20,31,30,78,90,72,40,45,67,50]
li.sort()
print(li)'''

#count :- count the occurance of the element.

'''li = [10,20,30,10,20,40,50,30,202,30]
print(li.count(10))'''

# mutable:- when we will change the elements of a data collection, this collection known as mutable.
#immutable:- we we will not change the elements of a data collection, this collection know as immutable,.


# tuple

'''tuple  is a collection and it's behave like hetrogenous(allow all the inside him) object types.
list enclosed in paraenthesis, ()
every element separate with another element help comma.
tuple is allow the indexing, position is imp.
tuple is allow the duplicate element.
tuple  is  not growbale and not deletebale element in nature.
tuple  is a immutable.

'''

'''tu = (1,2,3)
print(type(tu))

tu1 = 1,2,3
print(tu1)

print(dir(tu))'''

# operator

'''Arithmetic Opea
Relationship Op or Comparision op
Logical Opera
Assignment op ---- compound assignment op
Bitwise Opera
special op ---- idenity op and membership op.'''

# Arithmetic Opea:-
'''+(addition) -- int+int, int+flot, float+float, comp+comp, str+str
-(substraction) - int-int, int-float, float-float, comp-comp
*(multiplecation) int*int, int*float, Float*flaot, comp*comp, str*int
/(division):- int-int, int-float, float-float
//(floor division)
% modulus
**(expoentiation)'''

# %:- reminder

# print(10**6)

#realationship op or comparison op
# >,>=,<,<, == ,!=

# print(9!=9)

# Assignment op

# var = 10
#compound assignment op:- assignment op working a arth op.
# x = 0
#
# x+=10
#
# x+=90
# print(x)

#logical op:- and, or ,not

# and :- if both the condition are True then result return as a True value or it's False
# True   True     True
# True   False    False
# False  True     False
# False  False    False

# or :- atleast one condition True the result return a True value or it's False

# True    True    True
# True    False   True
# False   True    True
# False   False   False

#not :-

# print(not False)

#idenity op:-

# a = 10
# b = 11
# print(id(a))
# print(id(b))
#
# print(a is not b)

#membership op:- in

# li = [10,80,34,56,78]
#
# print(156  not in  li)

#user define variable
# a = 10
# b = 20
#
# res = a+b
# print(res)

# a = input('Enter a number:-')
# print(type(a))


a = '10'
b = int(a)
print(type(b))


# int
# float
# complex
# bool
#
# str
#
# list
# tuple
# set
# frozenset
# bytearray
# bytes

var = eval(input('Enter a number:-'))
# var2 = eval(input('Enter second number:-'))

print(type(var))
# print(res)


















