# st = 'SDFGdrtyfb34567#$%E&^'
# print(type(st))
#
# st1 = "driytfugDRFTUGY34567$#%^"
# print(type(st1))
#
# #a =10
#
# #triple code
# '''single_triple_cot = ''''''
# double_triplr_cot = """"""
# multiline comment
# doc string'''
#
# """softkwlist = [
#     '_',
#     'case',
#     'match',
#     'type'
# ]
#
# iskeyword = frozenset(kwlist).__contains__
# issoftkeyword = frozenset(softkwlist).__contains__"""
#
#
# var = 'Banglore'
#
# # print(var[0:4:1])
# # print(var[-8:-4:1])
#
# st = 'Banglore'
# 're'
# 'ng'
# 'an'
# # both positive and negetive
# # print(st[-2::])
# # print(st[2:4:])
#
# #Bnlr
# # print(st[0:-1:2])
#
# '''se = 'Hello World'
# #HloWrd
# print(se[::2])'''
#
# '''se = 'Hello World'
# print(se[-11::2])'''
#
# """st = 'I love india'
# # Io d'
# print(st[0:13:3])
# print(st[:-2:3])"""
#
# """name = 'Santosh Ku Behera'
# dob = '17/6/1997'"""
#
# #Adhar card :- name first 4 char and dob last 4 char
#
# # String mathmetical implimetation(+,-,*,/)
# # print('Ashutosh'*200)
#
# # password = name[0:4]+dob[-4:]
# # print(password)
#
# '''bank = 'STATE BANK OF INDIA'
# bran-ch_code = '000010927'
# #ifsc ---- SBIN0010927
#
# ifsc = bank[0]+bank[6]+bank[-5:-3]+branch_code[-7:]
# print(ifsc)'''
# """
# house_no = 'LIG-1010'
# street_no = 'Balaji-34'
# vechile = 'MH-01-AB-0108'
# mobile_no = '1234567890'"""
#
# #LI10Blj011470
# # password = house first two and last two char + street first word with 2 steps  like 'Baj'+Vechile RTO code '01'+mobile 3steps
#
# '''password = house_no[:2]+house_no[-2:]+street_no[:6:2]+vechile[3:5]+mobile_no[::3]
# print(password)'''

'''st = 'batch#12'
print(type(st))

print(dir(st))'''

#capitalize
#upper,lower,swapcase,endswith,startswith
#count,index,find,replace
#strip,split,join,format
#isalnum,isascii,isdigit,

'''st = 'raghu'
var = st.capitalize()
print(st)
print(var)'''

'''#upper/lower
st = 'hjgVuynbbnGCTY'
var = st.upper()
print(var)

var_low = st.lower()
print(var_low)'''

'''#swapcase
st = 'hjgVuynbbnGCTY'
var = st.swapcase()
print(var)'''

'''#'startswith/endswith
st = 'I love my india'
print(st.startswith('I'))
print(st.endswith('z'))'''

'''#count

st ='i love my india, india is best'
# print(len(st))
print(st.count('i'))
print(st.count('t'))
print(st.count(' '))'''

'''#find/index

st ='i love my india, india is best'
print(st.find('Z'))
print(st.index('Z'))'''

#strip
'''
st  = '     jhgbuihgb       '
print(st.strip())'''

'''#split

st = 'Ramesh/Suresh/Kamlesh/Rakesh'
var = st.split('/')
print(var)'''

# #join

'''li = ['Ramesh', 'Suresh', 'Kamlesh', 'Rakesh']
var = '-'.join(li)
print(var)'''


#format

'''a = 678
b = 678768

c = a+b
print(f'The value of c is , {c}')'''

'''s = '345678'
print(s.isdigit())

s1 = 'Gjuh4565678&^%&^%'
print(s1.isascii())'''

'''#replacee
st = 'ji jacky'
print(st.replace('ji','hi'))'''