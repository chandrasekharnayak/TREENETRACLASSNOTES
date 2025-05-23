# if condition:
#     hrvghtreui
#     jhrjkfgbvhik
#     jkhbjkrfgh

# else


'''
name = input('Enter your name:-')

if name == 'Sourav':
    print('Good Morning Sourav')
else:
    print('Please call Sourav')'''

#WAP take the value from end user and check the number is even or odd

'''num = int(input('Enter your number'))

if num%2==0:
    print(num,'Even')
else:
    print(num,'Odd')'''

#WAP the a string from end user and check the string is pallindrom or not.

'''st = input('Enter your string:-')

if st == st[::-1]:
    print(st,'is pallindrom')
else:
    print(st,'is not pallindrom')'''

#elif --- multicondition

'''soft_drink = input('Enter your drink_name:-')

if soft_drink == 'Thumsup':
    print('Salaman Khan')
elif soft_drink=='Mount & Dew':
    print('Hritik')
elif soft_drink == 'Slice':
    print('Katrina')
else:
    print('Go for badam shake')'''

#WAP take a number from end user and check the number is div 2 , then number div 3 and number div by both 2 and 3.
#
# num = int(input('Enter a number:-'))
#
# if num%2==0 and num%3==0:
#     print(num,'is div by both 2 and 3')
# elif num%2 ==0:
#     print(num,'is div by 2 only')
# elif num%3==0:
#     print(num,'is div by 3 only')



#iterative statement

# li = [10,20,30,40,50]
#
# for var in li:
#     add = var+5
#     print(add)

# my_house = ['Kalia','Lucky','Rupali','Chiku','Pipi','Chiki']

'''for var in my_house:
    print(var+' Ladu')'''


'''li = [1,9,89,76,54,35,67,84,21,24,32,55,45,43,44]

# for var in li:
#     if var%2!=0:
#         print(var,'odd')
        
even_li = []
odd_li = []

for var in li:
    if var%2==0:
        even_li.append(var)
    else:
        odd_li.append((var))
        
print(even_li)
print(odd_li)'''


#range :- generating the sequenece of numbers

# for var in range(100,201,10):
#     print(var)

# [start:end+1:step]
#
# range(start,end+1,step)

#i want to print start(*) 5 time

'''for i in range(5):
    print('*',end=' ')'''

'''
*
**
***
****
*****
'''

'''num = int(input('Enter your rows number:-'))

for i in range(num):
    print('*'*(i+1))'''

# for i in range(1,num+1):#1,2,3,4,5
#     print('*'*i)

'''**
****
******
********
**********'''

'''for i in range(2,num+1):
    if (i % 2==0):
        print('*'*i)'''

'''for i in range(2,num+1,2):
    print('*'*i)'''

'''
*****
****
***
**
*
'''

'''for i in range(1,6):
    print('*'*(6-i)) '''

'''
*******
*****
***
*'''

'''for i in range(1,8,2):
    print('*'*(8-i))'''

'''
*
***
*****
***
*
'''

#what is nested for loop

'''total_lines = 5
max_lines = 5

for i in range(total_lines):#0,1,2  3  4
    if i<= total_lines//2:
        num_starts = 1+2*i
        # print(num_starts)
    else:
        num_starts = max_lines -2*(i-total_lines//2)
        # print(num_starts)

    for j in range(num_starts):
        print('*',end='')
    print()'''


# for var in range(5):
#     print(var)

'''li = [
    [1,2,3],[20,30,40],[78,98,88],[67,68,69,56,45,34]
]


for i in li:
    for j in i:
        print(i,j)'''

'''
for i in range(5):
    for j in range(3):
        print(i,j)'''

#Write a for loop, if a list and check those element of  non collection remove him and those collection
# element print all element.


li = [
    10,20,8+9j,'qwerty',[90,89,78],[56,89,76]
]

'''output = [[1,2,3],[7,8,9]]

1
2
3
7
8
9'''

# for i in li:
#     if type(i)==list:
#         for j in i:
#             print(j)

'''for i in li:
    if type(i) != list:
        li.remove(i)
print(li)'''

'''di = {
    'Name':'Rahul','Age':27,'Salary':890000,'Languages':['Python','Java']
}

for k,v in di.items():
    print(k,v)'''



li = [
{'Name':'Rahul','Age':27,'Salary':890000,'Languages':['Python','Java']},
{'Name':'Ankit','Age':26,'Salary':990000,'Languages':['Python','SQL','C']},
{'Name':'Sudeer','Age':25,'Salary':790000,'Languages':['Python','Java','SQL']},
{'Name':'Maxwel','Age':29,'Salary':1090000,'Languages':['R','GoLang']}
]

'''for i in li:
    for k,v in i.items():
        if v=='Rahul':
            print(i['Salary'])
'''

'''for i in li:
    for k,v in i.items():
        if k =='Age' and v >26:
            print(i['Name'])'''


'''for i in li:
    for k,v in i.items():
        if k =='Languages' and 'Java' in v:
            print(i['Name'])'''

'''for i in range(1,11):
    print(i)'''

#while

# while condition:
#     statement


'''start = 1
end = 10

while start<=end:
    print(start)
    start = start+1'''

'''while True:
    print(1)'''


#write even number 1 to 100 using while loop.

'''start = 1
end = 1000

while start<=end:
    if start%2==0:
        print(start)
    start=start+1'''


#write program in while , print 1 to 100 prime number


'''num = 2

while num<=100:
    is_prime = True
    i = 2
    while i*i<=num:
        if num%i==0:
            is_prime = False
            break
        i+=1

    if is_prime:
        print(num)
    num +=1'''
#Transfer statement(break,continue,pass)

'''for i in range(1,16):
    if i==9:
        break
    print(i)'''


'''for i in range(1,16):
    if i%2==0:
        continue
    print(i)'''


for i in range(1,6):
    pass








