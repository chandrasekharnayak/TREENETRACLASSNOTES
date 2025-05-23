'''import module1
# print(dir(module1))
# print(module1.)
# print(b)

print(module1.add(100,200))'''

# import math

# import math

'''import csv
print(dir(csv))
csv.DictReader.fieldnames'''

# import math
# print(dir(math))
# print(math.pi)
# print(math.pow(4,5))
# print(math.factorial(5))

'''from math import factorial,pow,pi
print(factorial(5))
print(pow(3,2))
print(pi)'''

'''import math as m
m.factorial()
m.pi
m.sin()
m.cos()'''

# math
# os
# sys
# random
# csv
# subprocess
# DATETIME
# time





# acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

import math

'''var = math.sqrt(64)
print(var)'''

'''var = math.pow(3,4)
print(var)'''

'''var = math.floor(4.7)
print(var)'''

'''var = math.fabs(-10.8)
print(var)'''

# var = math.factorial(5)
# print(var)

'''var = math.gcd(12,6)
print(var)'''

'''var = math.pi
print(var)'''


import os

# var = os.getcwd()
# print(var)

'''os.chdir('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_14/API')
print(os.getcwd())'''

'''var = os.listdir('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_15')
print(var)'''

# os.mkdir('create_new_os')

# os.rmdir('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_15/module_and_packages/create_new_os')

# os.rename('rough','module_rough.txt')

# var = os.path.exists('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_15/nkjghj')
# print(var)

# full_path = os.path.join('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_15/function','/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_15/module_and_packages')

# print(os.system('ls'))

# print(os.getpid())

'''import sys

for i in sys.path:
    print(i)'''

from datetime import datetime

# var = datetime.now()
# print(var)

'''var = datetime.today()
print(var)'''

# var = datetime.utcnow()
# print(var)

'''date_string = "2024-10-21 10:15:00"
var = datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S")
print(var)'''

# now = datetime.now()
# current_time = now.time()
# print(current_time)

#timedelta
'''from datetime import datetime, timedelta

now = datetime.now()
# print(now)
two_days_ago = now + timedelta(days=20)
print("Two days ago:", two_days_ago)'''

'''import random

var = random.random()
print(var)
'''

import time

# var = time.time()
# print(var)

'''time.sleep(3)
print('hi nana')'''

'''import random,time
for i in range(10):
   var= random.random()
   str_var = str(var)[-4:]
   time.sleep(3)
   print(str_var)'''

import json