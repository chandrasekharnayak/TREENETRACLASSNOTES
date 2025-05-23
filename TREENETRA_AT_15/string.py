# st = 'vhgvHVGVg456453453%$%^$%7897*&*(  '
# print(type(st))
#
# st1 = "vhgvHVGVg456453453%$%^$%7897*&*(  "
# print(type(st1))
#
# st2 = '''vhgvHVGVg456453453%$%^$%7897*&*(  '''
# print(type(st2))
#
# st3 = """vhgvHVGVg456453453%$%^$%7897*&*(  """
# print(type(st3))

# doc string :- documenation string
# multiline comment

# st = ''
# print(type(st))

# string methods


'''capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format
)format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower
isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans(', '
partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip(', '
split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''

# 1.capitalize:- if first char of the string is lower, then it converts as upper char.

'''st = 'india'
var = st.capitalize()
print(var)
print(st)'''

#2. startswith :- it's check first char of the string, in given char start or not, it's return a boolean value.

'''st = 'india is best'
print(st.startswith('e'))'''

#3. endswith :- it's check last char of the string, in given char start or not, it's return a boolean value.
# st = 'india is best'
# print(st.endswith('t'))

#4 upper():- if any char in string is in lower, then its convert as a upper char.

# st = 'IndIa Is Best'
# print(st.upper())

#5. lower():- if any char in string is in upper, then its convert as a lower char.

# st = 'InDia Is Best'
# print(st.lower())

#swapcase:- its converts upper char to lower and lower char to upper.

'''st = 'InDia Is Best'
print(st.swapcase())'''

#count :- check the occurance of each char.
'''st = 'india is the best country'
print(st.count('t'))'''

#find and index
'''st = 'india is the best country'
# print(st.index('tr'))

print(st.find('z'))
print(st.index('z'))'''

#strip:- remove the whitespaces from start and end.
# st = '       qwer           tyu         '
# print(st.strip())

#replace

# st = 'Ji Johny'
#
# print(st.replace('Ji','Hi'))

# st = '234'
# print(st.isdigit())

#split

st = 'Abhishek Adarsh Rohan Rahul Rakesh'
# collection --- strore , it will encapluate the adata
'''
sp = st.split()
print(sp)'''

#join
# li = ['Abhishek', 'Adarsh', 'Rohan', 'Rahul', 'Rakesh']
# join_str = '/'.join(li)
# print(join_str)

#format - fstring

'''a = 10
b= 20
add = a+b

print(f'{a} and {b} , add together and the answer is {add}')'''






# slicing:-

st = 'hjfghf hjgh jguygy'

# position --- index --- indexing
#
# +ve --- (left to right)
# -ve --- (right to left)

st = 'banglore'

# syntax
# var_name[start:end+1:step]

# print(st[0:3:1])
# print(st[3:6])
# print(st[3:])
# print(st[:3])


# st = 'India is best, good to go'
#
# '''1. best(both postitive and negetive)
# 2. good to go (both postitive and negetive)
# 3.India((both postitive and negetive))
# 4.best, goo((both postitive and negetive))
# 5.Idai(both postitive and negetive)'''
#
# print(st[:7:2])

# st = 'india'
# # op 'aidni'
# print(st[::-1])

# string addition and string multiplication
# a string add with a string only.

# print('ab'+'ab')
# print('ab'*5)

# #collection
# store the data type in a collection
#
# # Data strc.
# list,tuple,set,frozenset,bytes,bytearray,rane,dict


# 14
# 12
# 89.9
# 8+9j
# True False
# 'vghvcgVYUYVytg8756756^%^$%^'
# ""
# ''''''
#
# s = 'banglore'
# s = s.capitalize()
# print(s)

[]
()



