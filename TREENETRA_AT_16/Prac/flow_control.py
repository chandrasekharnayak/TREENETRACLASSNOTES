'''user_num = int(input('Enter a number:-'))
st_num = str(user_num)

if st_num == st_num[::-1]:
    print('Pallindrom')
else:
    print('Not a Pallindrom')'''
import string

from reportlab.lib.validators import Validator

'''brand  = input('Enter your brand name:-')


if brand  == 'Luicphilf':
    print('yes it is good brand')

elif brand == 'Peteregland':
    print('yes it is one kind of ok brand')

elif brand == 'J&K':
    print('not a worthless')

else:
    print('this brand is not avl.')'''


# for (collectional itration)--- through the collection iterate over each element.

'''
str   
list
dict
'''

st = 'bhubaneswar'


# syntax

'''for var in collection_name:
    based on item write the statements.'''

'''for i in st:
    print(i)'''

'''new_st = ''

for i in st:
    new_st = i+new_st
print(new_st)'''

'''st = 'i love india'

se = set()

for i in st:
    se.add((i,st.count(i)))
print(se)'''
'''st = 'suhhass'

di = {}
for i in st:
    if i in di:
        di[i]+=1
    else:
        di[i]=1'''


#anagrams

st1 = 'cat'
st2 = 'care'

'''1.check the length first of both the string.if match the it is forward to next
2.check the count of each occurance of both string .
3.Validate both the string count same or not.a
4.if same then it is a anagram. if not same then  it is not a anagram.'''

# list and diction help of for

'''if len(st1)==len(st2):
    count_st1= {}
    count_st2 = {}

    for i in st1:
        if i in count_st1:
            count_st1[i]+=1
        else:
            count_st1[i]=1

    for i in st2:
        if i in count_st2:
            count_st2[i]+=1
        else:
            count_st2[i]=1

    if count_st1 == count_st2:
        print('Anagram')
    else:
        print('Not a Anagram')
else:
    print('Not a anagram')'''


#-------------------------------------

'''li = [10,2,3,22,45,32,16,19,91,25]

for i in li:
    if i%2==0:
        print(i,'even')
    else:
        print(i,'odd')'''



'''li = [890,768,212,455,636,228,909]

for i in li:
    if str(i)==str(i)[::-1]:
        print(i,'Pallindrom')
    else:
        print(i,'not a pallindrom')'''

'''li = [10,78.89,7+9j,'qwertyt',[78,90],'erty']

for i in li:
    if type(i)==str:
        print(i)'''


'''li = [10,20,30,[40,50]]

for i in li:
    if type(i)==list:
        for j in i:
            print(j)
    else:
        print(i)'''
# # 10
# # 20
# # 30
# # 40
# 50


# li = [
#     [10,20,21],[40,45,50],[80,90],[78,91],[21,2]
# ]
#
# for i in li:
#     for j in i:
#         print(j)



'''li = [91,56,32,45,61,77,11,31,9,70,4]
# [4, 9, 11, 31, 32, 45, 56, 61, 70, 77, 91]

n = len(li)

for i in range(n):
    for j in range(0,n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)'''

#for with dictionary

# di = {
#     'name':'A','age':26,'salary':56000
# }
#
# for key,value in di.items():
#     print(key,value)


li = [
    {'Name':'A','age':26,'salary':56000},
    {'Name':'B','age':23,'salary':78000},
    {'Name':'C','age':24,'salary':91000},
    {'Name':'D','age':21,'salary':67000},
    {'Name':'E','age':27,'salary':45000},

]

'''for i in li:
    for key,value in i.items():
        print(key,value)'''

'''for i in li:
    if i.get('Name')=='C':
        print(i.get('salary'))'''

'''for i in li:
    if i.get('age')<25:
        print(i.get('Name'))'''

'''sum = 0
for i in li:
    if i.get('age')>25:
        sum = sum+i.get('salary')
print(sum)'''


di = {
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
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}


'''for i in di.get('data'):
    if i.get('id')==8:
        print(i.get('first_name'))
'''
id_8_li = None
id_9_li = None

for i in di.get('data'):
    if i.get('id')==8:
        id_8_li = i.get('avatar').split('/')

for i in di.get('data'):
    if i.get('id')==9:
        id_9_li= i.get('avatar').split('/')
print(id_8_li)
print(id_9_li)

#id -8
for i in id_8_li:
    if i not in id_9_li:
        print(i)

#id -8
for i in id_9_li:
    if i not in id_8_li:
        print(i)







