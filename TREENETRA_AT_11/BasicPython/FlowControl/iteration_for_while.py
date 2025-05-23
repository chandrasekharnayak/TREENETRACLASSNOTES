#iteration st ---- for and while

# li = [1,2,3,4,5]
#
# for var in li:
#     print(var+10)


'''li = [11,14,17,18,19,24,56,77,79,34,31,23,28,91,93,97,94,98]

even_li = []
odd_li = []

for var in li:
    if var%2==0:
        even_li.append(var)
    else:
        odd_li.append(var)

print(even_li)
print(odd_li)'''
#---------------------------------------------

# li = [10,80,'78','qwerty',78+9j,45,'chiku',12.90,'zxcvbn']

# op = ['78','qwerty','chiku','zxcvbn']
# str_li = []
# for i in li:
#     if type(i)==str:
#         str_li.append(i)
# print(str_li)

#range
# range(start,end+1,step)
# range(11) ------ 0,1,2,3....10
# range(1,11)---- 1,2,3,....10
# range(1,11,2)----- 1,3,5,7,9

# print(range(11))
# print(range(1,11))

# for i in range(700,801,2):
#     print(i)

#write loop in range generating the odd number between 40 to 75.

# for i in range(40,76):
#     if i%2!=0:
#         print(i)


'''li = [78,556,68,2563,937,2573,473,2739,37839,5279,3636,7849,2537,38389,2637,36]
# print(len(li))

count = 0
for i in li:
    print(count,i)
    count = count+1
print(count)'''


'''di = {'Name':'Ankit','Age':28,'Salary':340000}
# print(di.items())
for i,j in di.items():
    print(i,j)'''

employees = [
    {'Name':'Vishal','Age':25,'Language':['Python','Java','C#']},
    {'Name':'Ankit','Age':28,'Language':['Javascript','Golang','dotnet']},
    {'Name':'Dibya','Age':31,'Language':['SQL','Java','React']},
    {'Name':'Kalpana','Age':28,'Language':['Python','Java','SQL']},
    {'Name':'Sudhanshu','Age':34,'Language':['Angular','Python','R']},
    {'Name':'Sonu','Age':38,'Language':['SQL','Bash','C#']},
    {'Name':'Monu','Age':25,'Language':['Python','Java','Golang']}
    ]

# 1.those candidates age is greater than 30, wants his name
#. 2. find the candidates name , those are using language :- Python
# 3. find the candidates name , those are using language :- Python and Java

'''for data in employees:
    if data['Age']>=30:
        print(data['Name'])'''

'''for data in employees:
    for k,v in data.items():
        if k=='Age' and v>=30:
            print(data['Name'])'''



# print(employee['Language'])

# for k,v in employee.items():
#     if k =='Language':
#         print(v)

#. 2. find the candidates name , those are using language :- Python
'''for i in employees:
    if 'Python' in i['Language']:
        print(i['Name'])'''

'''for i in employees:
    for k,v in i.items():
        if k=='Language':
            if 'Python' in v:
                print(i['Name'])
'''

# 3. find the candidates name , those are using language :- Python and Java

'''for i in employees:
    if 'Python' in i['Language'] and 'Java' in i['Language']:
        print(i['Name'])'''

#create a unique list without using set function.
'''li = [1,2,34,7,8,34,7,2,2,2,45,45,21,21,2,9]

unq_li = []

for i in li:
    if i not in unq_li:
        unq_li.append(i)
print(unq_li)'''


# 5-list
# 5-list
# 5-str
# theory question


# while loop:- conditional loop

'''
syntax:

while condition:
    statement
'''

'''number = int(input('Enter a user value:-'))

while number>10:
    print('Ok')'''

'''number = 1

while number<11:
    print(number)
    number = number+1'''

#print 1,50 all the odd numbers, and print sum of all the odd numbers

'''num = 1
sum = 0

while num<51:
    if num%2!=0:
        print(num)
        sum = sum+num
    num = num+1
print(sum)'''

#create while condition from 1,1000 and check which numbers are pallindrom

num = 100
while num<1001:
    if str(num) == str(num)[::-1]:
        print(num,':-Pallindrom')
    num = num+1

#transfer statement :- break, continue, pass





















