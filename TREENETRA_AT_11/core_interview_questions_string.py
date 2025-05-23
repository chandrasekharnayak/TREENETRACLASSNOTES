#string
#1.reverse a string without using inluid function
#
# str1 = 'qwerty'
# print(str1[::-1]

"""empty_str = ''

for i in str1:
    empty_str = i+empty_str
print(empty_str)"""

#2.reverse a string ,but special char remains same

# str1 = 'A/B$C'
# excpeted_op = 'C/B$A'

'''alphas = [i for i in str1 if i.isalpha()]
special = [i if not i.isalpha() else None for i in str1]
reversed_alphas = alphas[::-1]#CBA

result = []

for i in str1:
    if i.isalpha():
        result.append(reversed_alphas.pop(0))
    else:
        result.append(i)
exp_str = ''.join(result)
print(exp_str)'''


'''str1 = 'AbCdEfGh'
# exp =  'GbEdCfAh'

upper_fetch = [i for i in str1 if i.isupper()]
# print(upper_fetch)
lower_fetch = [i for i in str1 if i.islower()]
# print(lower_fetch)

reversed_upper_fetch = upper_fetch[::-1]
# print(reversed_upper_fetch)
result = []

for i in str1:
    if i.isupper():
        result.append(reversed_upper_fetch.pop(0))
    else:
        result.append(i)
exp = ''.join(result)
print(exp)'''

#what is list comprehension
# ans :- it is a single line code, in list we will iteatare a loop, and those elements are produce we store in the list.

'''li_com = [i for i in range(1,21) if i%2==0]
print(li_com)

li = []

for i in range(1,21):
    if i%2==0:
        li.append(i)
print(li)'''

# li = [19,90,'67','qwerty',6+9j,[89,90],('Y','U')]

# expeted_op = ['67','qwerty',6+9j]

# exp = [i for i in li if type(i)==str or type(i)==complex]
# print(exp)


# uppers=[i for i in str1 if i.isupper()]
# lowers=[i for i in str1 if i.islower()]
#
# #print(uppers)
# #print(lowers)
#
# rev_up=uppers[::-1]
# result=[]
# for i in str1:
#     if i.isupper():
#         result.append(rev_up.pop(0))
#     else:
#         result.append(i)
# print(result)


#3
"""str1 = 'aaabbce'
'''ecp :- a3b2c1e1'''

count = {}

for i in str1:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
# print(count)

emp_str = ''

for k,v in count.items():
    emp_str=emp_str+k+str(v)
print(emp_str)"""
# -------------------------------------------
'''str1 = 'bB,CcC,Dd,ZZzZ'
# exp = 'B2C3D2Z4,3'

supper_str = str1.upper()

count = {}

for i in supper_str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)'''

#4:- Home work

"""str1 = 'aaabbaabccdcdd'
exp = a3b2a2b1c2d1c1d2"""


def alphacount_in_str(s):
    out_str = ''
    count_char = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count_char += 1
        else:
            out_str += s[i] + str(count_char)
            count_char = 1

    out_str += s[-1] + str(count_char)

    return out_str


str1 = 'aaabbaabccdcdd'
print(alphacount_in_str(str1))


