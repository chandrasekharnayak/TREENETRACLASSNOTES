#
# opeartor_name = 'soumya' #global variable
#
# def telecom_jan_bill(per_call = 2):
#     cdr_report_jan = 1245
#     global current_bill_jan
#     current_bill_jan = cdr_report_jan*per_call
#     return opeartor_name,current_bill_jan
#
# def telecom_feb_bill(per_call = 2):
#     cdr_report_feb = 1500
#     global current_bill_feb
#     current_bill_feb = cdr_report_feb*per_call
#     return opeartor_name,current_bill_feb
#
# def telecom_march_bill(per_call = 2):
#     cdr_report_march = 1600
#     global current_bill_march
#     current_bill_march = cdr_report_march*per_call
#     return opeartor_name,current_bill_march
#
# print(telecom_jan_bill())
# print(telecom_feb_bill())
# print(telecom_march_bill())
#
#
# def telecom_first_quater():
#     toatl_first_quater_bill =current_bill_jan+current_bill_feb+current_bill_march
#     return opeartor_name,toatl_first_quater_bill
#
#
# print(telecom_first_quater())
#
from gc import garbage

#Question paper discussion

# li = {i:i**2 for i in range(1,11)}


# print(li)


# python private heep.
#
# garbage collection


import copy

#shllow copy

'''li = [[90,91],[10,20]]

new_li = copy.deepcopy(li)
new_li[0][0]=90000
print(li)
print(new_li)'''



'''st = 'i love india'

char_count = {}

for i in st:
    if i in char_count:
        char_count[i]+=1
    else:
        char_count[i]=1

print(char_count)'''

'''li = [78,56,21,34,79,10]
n = len(li)


for i in range(n):
    for j in range(0,n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)'''


'''li = ['flow','flower',56,89,'fly']

list_count = []
string_count = 0
for i in li:
    if type(i)==str:
        for j in i:
            list_count.append(j)
        string_count+=1'''

# print(list_count)
# print(string_count)

'''char_count = {}
for count in list_count:
    if count in char_count:
        char_count[count]+=1
    else:
        char_count[count]=1

# print(char_count)

longest_prifix = ''
for k,v in char_count.items():
    if v==string_count:
        longest_prifix+=k


print(longest_prifix)'''




'''for i in range(100,1001):

    len = str(i)

    res = 0
    for j in str(i):
        res = res+ (int(j)**3)

    if res == i:
        print(i,'armstrong')'''


'''li = [90,56,21,34,101,58,29,62]

largest = 0
sec_largest = 0
third_largest = 0

for i in li:
    if i>largest:
        third_largest = sec_largest
        sec_largest = largest
        largest=i

    elif i>sec_largest and sec_largest!= largest:
        third_largest = sec_largest
        sec_largest = i
    elif i>third_largest and third_largest != sec_largest:
        third_largest = i




print(largest)
print(sec_largest)
print(third_largest)'''

li=['flow','flower',56,78,'floy']
a=[x for x in li if isinstance(x,str)]
prefix=a[0]
for a in a[1 :]:
    secpro=''
    for i in range(min(len(prefix),len(a))):
        if prefix[i]==a[i]:
            secpro += prefix[i]
        else:
            break
    prefix=secpro
print(prefix)












