'''
1. in a list check the element datatype and add in a anothe list.
2.work with nested and how it is working
3.li = [10,20,30,[78,90]]
op = [10,20,30,78,90]

4.sort a list in acceding without using any inbuild function
5. Write a factorial number and add in a list.
6. li = [12,13,11,15,10,26,12]

7.divide list into 2 sub list where difference betwwen sum of the element is low
li1 = []
li2 = []

8. find max and second max in given li with optimum approch
li = [12,13,11,15,10,26,12]
'''

#1
'''li = [10,2.90,7,'yu',3+9j,'qwerty']

str_li = []
for i in li:
    if type(i)==str:
        str_li.append(i)
print(str_li)'''
#1 / 2nd approch
'''li = [10,2.90,7,'yu',3+9j,'qwerty']

str_li = list(filter(lambda a :type(a)==str, li))
print(str_li)'''


#2

'''li = [
    [10,20,30],
    [40,50,60],
    [70,80,90],
]

for i in li:
    for j in i:
        print(j)
'''



#3
'''li = [10,20,30,[78,90]]
op = [10,20,30,78,90]

new_li = []

for i in li:
    if isinstance(i,list):
        for j in i:
            new_li.append(j)
    else:
        new_li.append(i)
print(new_li)'''

#sort a list in acceding without using any inbuild function

# li = [90,56,32,12,45,67,54,32,12,68,94,99,44,36,102]
# n= len(li)
#
# for i in range(n):#
#     for j in range(0,n-i-1):j#11
#         if li[j]>li[j+1]:
#             li[j],li[j+1]= li[j+1],li[j]
# print(li)

#7
'''li = [12,13,11,15,10,26,12]

n=len(li)
for i in range(n):
    for j in range(0,n-i-1):
        if li[j]<li[j+1]:
           li[j],li[j+1]=li[j+1],li[j]

li1= []#26,12,11
li2 = []#15,13,12,10

sum_li1 = 0#26+12=38+11 = 49
sum_li2 = 0#15+13=28+12 = 40+10 = 50

for i in li:
    if sum_li1<=sum_li2:
        li1.append(i)
        sum_li1+=i
    else:
        li2.append(i)
        sum_li2+=i
print(li1)
print(li2)'''




# op
# li1= [12,11,26] = 49
# li2= [13,15,12,10] = 50

# li= [200]
# li2 = [12,13,11,15,10,26,12]

#8 max ans second max in a list , but without using inbuit function and indexing

li = [ 89,76,45,32,12,78,91,45]
# max = 91
# sec_max = 89


'''
n=len(li)
for i in range(n):
    for j in range(0,n-i-1):
        if li[j]<li[j+1]:
           li[j],li[j+1]=li[j+1],li[j]

print(li[0])
print(li[1])'''

#2 approch
li = [ 89,76,45,32,12,78,91,45,89,91]

max_val = float('-inf')#91
sec_max_val = float('-inf')

for i in li:#89
    if i >max_val:
        sec_max_val = max_val
        max_val = i
    elif i > sec_max_val and i!=max_val:
        sec_max_val = i
print(max_val,sec_max_val)







#Practi---- for loop

'''
*
*
*
*
*
'''
'''*****'''

'''n = int(input('Enter how much start you want:-')) #5

for i in range(n):
    print('*',end='')'''

'''
*
**
***
****
*****
'''
# n = int(input('Enter how much start you want:-'))

'''for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()'''

'''for i in range(1,n+1):
    print('*'*i)'''

'''
*****
****
***
**
*
'''
'''n=5
for i in range(n):
    for j in range(n-i):
        print("*",end='')
    print()
'''



