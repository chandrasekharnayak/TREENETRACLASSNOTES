'''import file1


print(file1.a)
print(file1.b)
print(file1.armstrong(153))'''

import math


# print(dir(math))

'''('acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign',
 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial',
 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan',
 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi',
 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod',)
'tan', 'tanh', 'tau', 'trunc', 'ulp']'''

# res = math.sqrt(16)
# print(res)

# res = math.pow(3,8)
# print(res)

# res = math.floor(467.99876)
# print(res)

# res = math.fabs(-7)
# print(res)

# res = math.factorial(5)
# print(res)

# res = math.gcd(54,24)
# print(res)

# res = math.pi
# print(res)

# res = math.tan(45)
# print(res)


import random
# print(dir(random))

# res = random.random() # 0 to 1
# print(res)

# res = random.randint(1000,9999)
# print(res)

# f = ['apple','bananna','grape','orange','cherry']
# ran_fruit = random.choice(f)
# print(ran_fruit)

# f = ['apple','bananna','grape','orange','cherry']
# random.shuffle(f)
# print(f)


import os

#getcwd
# current_dir = os.getcwd()
# print(current_dir)

#chdir
# os.chdir('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_16/ExceptionHandeling')
# print(os.getcwd())

#listdir
# files = os.listdir('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_15')
# for i in files:
#     print(i)

#mkdir
# print(os.getcwd())
# os.mkdir('qwerty')

#rmdir
# os.rmdir('qwerty')

#rename
# os.rename('file1.py','file111.py')

#os.path.exits()

'''if os.path.exists('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_1888'):
    print('File exits')
else:
    print('File not exits')'''

# os.path.join()

# full_path = os.path.join('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_19/Module','user','admin','file2.py')
# print(full_path)

# os.getpid()
# process_id = os.getpid()
# print(process_id)

# os.system()
# print(os.system('ls -ll'))


from datetime import datetime,timedelta

# current_time = datetime.now()
# print(current_time)

# today = datetime.today()
# print(today)

# utc_time = datetime.utcnow()
# print(utc_time)

# future version pe kaam karge
# print(datetime.now(datetime.UTC))

# date_string = '10-03-2023 10:15:23'
#
# date_obj = datetime.strptime(date_string,'%d-%m-%Y %H:%M:%S')
# print(date_obj)

#date
# now = datetime.now()
# current_date = now.date()
# print(current_date)

#time
# now = datetime.now()
# current_time = now.time()
# print(current_time)

#timedelata

'''now = datetime.now()
two_day_ago = now-timedelta(days=2)
print(two_day_ago)'''

# import time

# print(time.time())

# time.sleep(10)

# print(time.ctime())

# from faker import Faker
#
# fake = Faker()
#
# data = []
# for i in range(10):
#     new_data = {}
#     new_data['first_name']= fake.first_name()
#     new_data['last_name']= fake.last_name()
#     new_data['address']= fake.address()
#     new_data['city']= fake.city()
#     new_data['state']= fake.state()
#     new_data['country']= fake.country()
#     data.append(new_data)
#
# for i in data:
#     print(i)


li = [10,10,20,30,40,50,70]

tup = tuple(li)
se = set(li)
fz = frozenset(li)
by = bytes(li)
bya = bytearray(li)
print(bya)