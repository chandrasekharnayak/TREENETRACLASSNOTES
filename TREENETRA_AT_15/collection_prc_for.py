# st = 'qwerty'
# op=ytrewq
'''1.reverse a string without using inbuilt func or slicing'''
from os import mkdir

'''new_st = ''
for i in st:
    new_st = i+new_st
print(new_st)'''

#2. i have string, from use input , count the length of the string without using inbuilt function

# user = input('Enter a string:- ')
#
# count = 0
# for i in user:
#     count = count+1
# print(count)

#3. i have string, from use input , count the how many vowels in their without using inbuilt function

# user = input('Enter a string:- ')#deva
#
# vowels = 'AEIOUaeiou'
# count = 0
# for i in user:
#     if i in vowels:
#         count =count+1
#         print(i)
# print(count)

#4. have string, some upper,lower,digit and special, want separate them.

# st = 'Ok, Hello, 123,Yes,89 @,rt&^7vh$%^4354'

'''upper = ''
lower = ''
digit = ''
special_ch = ''

for i in st:
    if i.isupper():
        upper = upper+i
    elif i.islower():
        lower = lower+i
    elif i.isdigit():
        digit =digit+i
    else:
        special_ch = special_ch+i
print(digit)'''

#5, ave string, find out thr digit and print sum.

st = 'Ok, Hello, 123,Yes,89 @,rt&^7vh$%^4354'

digit = ''

'''for i in st:
    if i.isdigit():
        digit = digit+i
print(digit)

sum = 0#
for i in digit:
    var = int(i)
    sum = sum+var'''
# print(sum)

# -----------------------------------------------

# li = ['Rajesh','Mahesh','Suresh','Vaibhav','Kunal','Shruti']
#
# for i in li:
#     for j in i:
#         print(j)

'''li = [[10,11,13],[12,15,18],[90,23,42]]

new_li = []

for i in li:
    for j in i:
        if j%2==0:
            new_li.append(j)
print(new_li)'''

'''li = [['qwerty',12,'89'],[78.90,67,'rt','Vamshi'],['ty',90]]

new_str = []
for i in li:
    for j in i:
        # if type(j)==str:
        if isinstance(j,str):
            new_str.append(j)
print(new_str)'''

'''li = [10,30,[11,12],[34,56],67,89]
# op = [10,30,11,12,34,56,67,89]

op = []
for i in li:
    if isinstance(i,list):
        for j in i:
            op.append(j)
    else:
        op.append(i)

print(op)'''

#nested loop

# for i in range(1,6):#1,2
#     for j in range(1,6):#5,3
#         print(i,j)


#code
'''list1 = [1, 2]
list2 = ['a', 'b']
Example Output:

1 a
1 b
2 a
2 b'''

'''Find Maximum in Nested List
Problem: Write a Python program to find the maximum value in a nested list.

Example Input:

python
Copy code
nested_list = [[1, 5, 9], [12, 4], [7, 8, 15]]
Example Output:

op
15'''

'''list1 = [1, 2]
list2 = ['a', 'b']

for i in list1:
    for j in list2:
        print(i,j)'''

nested_list = [[1, 5, 9], [12, 4], [7, 8, 15]]

'''li = []
for i in nested_list:
    for j in i:
        li.append(j)

print(li)'''
'''print(max(li))'''

'''max = 0#15

for j in li:
    if j>max:
        max = j
print(max)'''

# li.sort()
# print(li[-1])

# li = [1, 5, 9, 12, 4, 15,7, 8]
#
# var = 1, 5, 9, 12, 4, 15, 7, 8
#
#
# n = len(li)
# for i in range(n):
#     for j in range(n-i-1):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
#
# print(li[0])

var1 = 'abcdeaabbcd'
'a3b3c2d2e1'



'''dict create a empty
iterate the loop
check if condition, if element present, do the +1
else element not presesnt enter key in dict value should be 1
print(dict)
'''

# di = {}
#
# for i in var1:
#     if i in di:
#         di[i]+=1
#     else:
#         di[i]=1
#
# st = ''
# for k,v in di.items():
#     var = str(v)
#     st = st+k+var
# print(st)

# var = {'a': 3, 'b': 3, 'c': 2, 'd': 2, 'e': 1}
# # print(var.items())
# for k,v in var.items():
#     print(k,v)


st = 'DO I jjfyf $56456 %%$$$%$%'

'''di = {}
for i in st:
    if i.isdigit():
        if i in di:
            di[i]+=1
        else:
            di[i]=1
print(di)
'''

#multi dict

# di = {'Name':'A','Age':21,'Salary':'67000','Subjcet':['Python','Java']}
# print(di['Salary'])
# print(di.get('Salary'))

# for key,value in di.items():
#     print(key,value)

'''li_dict = [
    {'Name':'A','Age':21,'Salary':'67000','Subjcet':['Python','C++','SQL'],'MName':'Ragav'},
    {'Name':'B','Age':23,'Salary':'78000','Subjcet':['Python','Java','Java Script'],'MName':'Ragav'},
    {'Name':'C','Age':32,'Salary':'120000','Subjcet':['SQL','Java','C#'],'MName':'Sachin'},
    {'Name':'D','Age':28,'Salary':'98000','Subjcet':['SQL','Java','R'],'MName':'Sachin'},
    {'Name':'E','Age':34,'Salary':'140000','Subjcet':['Python','R','Golang'],'MName':'Ragav'}
]'''

'''for i in li_dict:
    if i['Age']>30:
        print(i['Name'])
'''

'''for i in li_dict:
    if i['MName'] =='Ragav':
        print(i['Name'],i['Age'],i['Salary'])'''


'''for i in li_dict:
    if ('Python' in i['Subjcet']) and ('Java' in i['Subjcet']):
        print(i["Name"])
'''




data_di = {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

'''
1.help of data_di['data'] fetch the value, and get a list
2.iterate the list and get the each iteration dict
3. in list iteration will get the dict, each dict have email key . i['email']
4. in variable split the email string with help of . separater and store in a variable.
5.the we will get a list, then help of indexing, fetch list[0] as a first name
5.with the help of setdeafult make a key as 'name', and use first name as value

'''

for i in data_di['data']:
    values = i['email'].split('.')[0]
    i.setdefault('name',values)
print(data_di)


# key = data_di.keys()
# print(len(key))

'''for i in data_di['data']:
    if i['id'] ==8:
        print(i['email'])'''


# di = {'id':13,'email':'qwerty@gmail.com'}
# data_di['data'].append(di)
# print(data_di)
#







