'''a = 10

b = 20

def armstrong(num):
    sum = 0
    for i in str(num):
        sum = int(i)**(len(str(num)))+sum
    return sum ==num'''

'''
 module is a python file , and it is a idenifier in python.
 where we are writeing our query and code. when it is required python
 with help of import keyword , we call that module and module functionality
 in python file or another file module,
 
 importing helps to use reuse code, and its help to programming optimization.


there are two types of module in python 

inbuilt module 
user define module


math
os
sys
randam
time
datetime
subprocess
abc
faker

'''

# /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/__phello__

# how to call a moduel

'''import math as m
print(dir(m))'''

# call multiple module in a single time.
# import math,os,sys,subprocess

# # Call specific function a module
# from math import factorial
# factorial(5)

#call multiple function in a specific module

from math import factorial,pi,cos,log
print(pi)

















