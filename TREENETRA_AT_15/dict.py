'''
dict is a datatype in python and enclosed in {}
it is key-value pair
key is always immutable
value is both mutable and immutable
key is not duplicate and not repeated in dict
value are allowed duplicate
dict is growable in nature, so we called it is a mutable data type


'''
from select import kevent
from webbrowser import Konqueror

# Name   age  salary  Manager
# A       21    45K       A
# B       22    78k
# C       23    67K

'''di = {'name':'A','age':21,'Salary':'45K','Manager':['A','B'],'age':26}

# var['Key_name']
# print(di['Name'])
di['Dept']='IT'
di['name']='AA'
print(di)
'''



# set = {1,2,3}
# print(type(di))

'''key:value 

var  = 10'''

# print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

'''di = {1:2,2:3}
di.clear()
print(di)'''

#copy
'''di = {'name':'A','age':21,'Salary':'45K'}
di1 = di.copy()
print(di1)'''

# get:-
'''di = {'name':'A','age':21,'Salary':'45K'}
print(di.get('name'))
print(di['name'])'''

#keys:-
# di = {'name':'A','age':21,'Salary':'45K'}
# print(di.keys())

#values
'''di = {'name':'A','age':21,'Salary':'45K'}
print(di.values())'''

#items
'''di = {'name':'A','age':21,'Salary':'45K'}
print(di.items())

for key,value in di.items():
    print(key,value)'''

#popitem
'''di = {'name':'A','age':21,'Salary':'45K'}
di.popitem()
print(di)'''

#pop():-

# di = {'name':'A','age':21,'Salary':'45K'}
# di.pop('age')
# print(di)

#setdefault
'''di = {'name':'A','age':21,'Salary':'45K'}
di.setdefault('manager_name','ABCD')
# di['manager_name']='ABCD'
print(di)'''

#update

''' '''












