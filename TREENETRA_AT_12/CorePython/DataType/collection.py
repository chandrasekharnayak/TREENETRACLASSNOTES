#list

# li = [10,2.8,8+9j,'wertyu',True,[90,80],(678,90),10,20,10,20]
# print(li)
# print(type(li))
# print(li[-1])

# li[0]=1000
# print(li)

# print(dir(li))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

#append --one arg--
'''li =[10,20,10,20,30,40,30]
li.append(90)
print(li)'''

#insert
'''li =[10,20,10,20,30,40,30]
li.insert(1,15)
print(li)'''

#extend
'''
li1 = [10,20,30]
li2 = [40,50,60]

li2.extend(li1)

print(li2)
# print(len(li1))'''

'''#remove

li = [10,20,30,40,10,20]
li.remove(10)
li.remove(10)
print(li)'''

#pop

'''li = [10,20,30,30,203,40,20128,8]
print(li.pop())
print(li)'''

#clear

'''li = [10,30,40,50,25,36]
li.clear()
print(li)'''

#count

'''li = [10,20,30,202,20,10,20,40,50]
print(li.count(202))'''

#copy

'''li = [10,20,30,40]
li2 = li.copy()
print(li2)'''

#reverse
'''li = [102,3,40,450,32,76,89,56,34]
li.reverse()
print(li)'''

#sort -- dec to acc

'''li =[90,38,78,94,32,1,8,76,54,31,908]
li.sort(reverse=True)
print(li)'''

#Mutable and Immutable

#tuple
"""Tuple is enclosed in ()
Tuple is a hetrogenous object type
its accepting the index values
duplicate element allowed in tuple
but tuple is not growable , it's always fixed'"""

tu = (10,20,394,'kujhgu',9+9j,True,[768,90])
# print(type(tu))
print(dir(tu))














