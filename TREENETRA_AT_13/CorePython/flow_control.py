'''name = input('Enter your name:-')

if name == 'Rahul':
    print(name,'Good morning')
else:
    print('Rahul not avl')'''

'''num = int(input('Enter a number:-'))

if num%2==0:
    print('Even')
else:
    print('Odd')'''

#take a string from end user and check string is pallindrom or not
'''user = input('Enter your name:-')

if user == user[::-1]:
    print('Pallindrom')
else:
    print('Not a pallindrom')'''

'''num = int(input('Enter your num:-'))

if num%2==0 and num%3==0:
    print(True)
else:
    print(False)'''

'''num = int(input('Enter your num:-'))

if num%2==0 and num%3==0:
    print('This num div by both 2 and 3')

elif num%2==0:
    print('This num div by only 2')

elif num%3==0:
    print('This num div by only 3')

else:
    print('This num not div by 2 and 3')'''

'''if
if - else
else (np)
if - elif 
elif (np)
if - elif - else
elif - else(np)'''

#for loop
# li = [10,20,30,40]
#
# for var in li:
#     print(var*2)

'''li = [10,24,31,43,66,87,89,21,26,90]

even_li = []
odd_li = []

for i  in li:
    if i%2==0:
        even_li.append(i)
    else:
        odd_li.append(i)
print(even_li)
print(odd_li)'''

'''li = [433,212,563,898,566,333,221,454,3113,67,89]

for i in li:
    if str(i)==str(i)[::-1]:
        print(i,'pall')
    else:
        print(i,'n Pall')'''

'''li = [10,89.90,78,98.9,9+9j,'77','qwerty',67,89]

for i in li:
    if isinstance(i,str):
        print(i)'''





'''li = [[1,2],[3,4],[5,6],(8,9)]

for i in li:
    for j in i:
        print(j)'''


'''li = [1,2,[3,4]]

for i in li:
    if type(i)==list:
        for j in i:
            print(j)
    else:
        print(i)'''




'''li = [1,2,(89,90),7,8,[90,91]]
# 1 2 89 90 7 8 90 91

for i in li:
    if type(i)==list or type(i)==tuple:
        for j in i:
            print(j)
    else:
        print(i)'''


#str - for

# st = 'bhubaneswar'
'''new_st = ''

for i in st:
    new_st = new_st+i.upper()
print(new_st)'''

'''new_st = ''

for i in st:
    new_st = i+new_st
print(new_st)'''

'''st = 'King Kong Is GrEat'

upper = ''
lower = ''
for i in st:
    if i.isupper():
        upper = upper+i
    elif i.islower():
        lower= lower+i
print(upper)
print(lower)'''

#range()

# range(start,end+1,steps)

# for var in range(2,51,2):
#     print(var)

# *
# *
# *
# *
# *

# *
# **
# ***
# ****
# *****

# *****
# ****
# ***
# **
# *

# for i in range(1,6):
#     print('*'*(6-i))


# *
# **
# ***
# ****
# *****

'''num = int(input('Enter a number:-'))
for i in range(1,num+1):
    print('*'*((num+1)-i))'''


# *****
# ****
# ***
# **
# *

'''
     *
    **
   ***
  ****
 *****
******'''

'''for i in range(1,7):
    print(' '*(7-(i+1))+'*'*i)'''
'''
*****
 ****
  ***
   **
    *'''

# for i in range(1,7):
#     print(' '*(i-1)+'*'*(7-i))

# import os
# print(__file__)
# print(os.path.abspath(__file__))
# BASE_DIR=os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR = os.path.join(BASE_DIR+'templates')

#dictionary use for

# di = {'Name':'A','Age':26,'Salary':67000}
# print(di['Age'])

# for key,value in di.items():
#     print(key)


# li = [
# {'Name':'A','Age':26,'Salary':67000,'Subjcet':['Python','Java','C']},
# {'Name':'B','Age':27,'Salary':89000,'Subjcet':['Ruby','Golang ','C']},
# {'Name':'C','Age':34,'Salary':65000,'Subjcet':['.Net','SQL ','Perl']},
# {'Name':'D','Age':33,'Salary':72000,'Subjcet':['Python','Perl ','Ruby']},
# {'Name':'E','Age':38,'Salary':60000,'Subjcet':['SQL','Java ','PLSQL']},
# ]
#
# enumerate()
#
# for i in li:
#     if 'Python' and 'Java' in i['Subjcet'] :
#         print(i['Name'])


# di ={
#     "page": 2,
#     "per_page": 6,
#     "total": 12,
#     "total_pages": 2,
#     "data": [
#         {
#             "id": 7,
#             "email": "michael.lawson@reqres.in",
#             "first_name": "Michael",
#             "last_name": "Lawson",
#             "avatar": "https://reqres.in/img/faces/7-image.jpg"
#         },
#         {
#             "id": 8,
#             "email": "lindsay.ferguson@reqres.in",
#             "first_name": "Lindsay",
#             "last_name": "Ferguson",
#             "avatar": "https://reqres.in/img/faces/8-image.jpg"
#         },
#         {
#             "id": 9,
#             "email": "tobias.funke@reqres.in",
#             "first_name": "Tobias",
#             "last_name": "Funke",
#             "avatar": "https://reqres.in/img/faces/9-image.jpg"
#         },
#         {
#             "id": 10,
#             "email": "byron.fields@reqres.in",
#             "first_name": "Byron",
#             "last_name": "Fields",
#             "avatar": "https://reqres.in/img/faces/10-image.jpg"
#         },
#         {
#             "id": 11,
#             "email": "george.edwards@reqres.in",
#             "first_name": "George",
#             "last_name": "Edwards",
#             "avatar": "https://reqres.in/img/faces/11-image.jpg"
#         },
#         {
#             "id": 12,
#             "email": "rachel.howell@reqres.in",
#             "first_name": "Rachel",
#             "last_name": "Howell",
#             "avatar": "https://reqres.in/img/faces/12-image.jpg"
#         }
#     ],
#     "support": {
#         "url": "https://reqres.in/#support-heading",
#         "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
#     }
# }
#
# id_end = int(input('Enter your id number:-'))
#
# for i in di['data']:
#     if i['id']==id_end:
#         print(i['email'])

#while
#
# Syntax
#
# while Condition:
#     statement

#in while loop id the condition True then while statemenet will execute and iterated till condition false

#while print 1 to 10

'''num = 1
end_num = 10
sum = 0
while num<=end_num:
    print(num)
    sum = sum+num
    num = num+1
print(sum)
'''

# write pallindrom num with help of while loop without using str.

#transfer statement
# break, continue , pass

# break :- its break loop with the help condition , once break the loop its not start again

# for i in range(1,11):
#     if i ==7:
#         break
#     print(i)

#1 to 6

# continue-- skip
#based on the condition its skip the iteration

'''for i in range(1,11):
    if i%2==0:
        continue
    print(i)
'''

for i in range(1,11):
    pass

# while True:
#     pass














