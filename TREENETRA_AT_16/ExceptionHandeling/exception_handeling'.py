'''error:- developer mistake
bug :- in time of testing tester found some issue thats called bug
defect:- after deployment in prod env client or tester found some issues that known as defect.'''
from asyncio import gather

from fastapi.openapi.models import APIKey
from sqlalchemy.dialects.oracle.dictionary import dictionary_meta

# developer -- develop something
#
# 1
# 2
# 3
# 4
# 5------ logic input + input -- str+str int+int  int+str--- error
# 6
# 7
# 8


'''what is the mean by automation :- process, use  machine , instead human , doing faster work, those human based knowdlege how to run the machine.

what is the mean by automation testing:- tools(machine), already tools and framework are avl, based on clinet requirement we are writing test case or script

automation develeopment? :-  Software development in Testing.(SDET), when  we are devloping the test framework from scractes.

what is the mean by development:- based on client req, developer develope, frontend , backend and database.'''

# what is a error :-  some unplaned event, that's break the flow of program , know as error.
#exception :- exception is the part of error, process.


'''
SyntaxError:- programmer not follow the rules and regulation of the program
RunTimeError:- When programm is running in that time, some issues is happedn based on the logic. ---- exception
'''

# Exception Handeling :- is a process, where as a program , we found the high risk area, based on that we are handel is point, when programming runing it will handel that sittuation.

# Types of imp errors
# AttributeError

'''li = [10,20,30]
li.appews(80)
print(li)
AttributeError: 'list' object has no attribute 'appews'. Did you mean: 'append'?'''

# ZeroDivisionError
# P/Q :- Q should not be 0.
# 10/0
# ZeroDivisionError: division by zero

# NameError:- when same name identifier not exits in workpage
'''print(a)
NameError: name 'a' is not defined'''

# IndexError
'''st = 'qwerty'
st[10]
IndexError: string index out of range'''

# KeyError
'''di = {'A':1,'B':2}
di['C']
KeyError: 'C'''

# TypeError
# 'ty'+9 TypeError: can only concatenate str (not "int") to str
# 'ty'*'ty' TypeError: can't multiply sequence by non-int of type 'str'


# ValueError
'''userinput = int(input('Enter a number:-'))
print(userinput)

ValueError: invalid literal for int() with base 10: '67.90'''

#how to handel exception in python.
'''try:
    Risky code

except ExceptionName:
        Solution
        10
        67
finally:
    Non Risky code'''

#write program  divded two number with differenet differnt user inputs.
'''try:
    num1 = int(input('Enetr a number:-'))
    num2 = eval(input('Enter a number:-'))
    res = num1/num2

except ZeroDivisionError as msg:
    print(msg)

except ValueError as msg:
    print(msg)
    
except TypeError as msg:
    print(msg)
    
finally:'''


'''server --- EOFError,FileNotFoundError,KeyError

server close'''


#write a program to handel a file in your local machine, read the data of the file. may be this file password protected?
# FileNotFoundError
# PermissionError

'''try:
    with open('a.txt','r') as file:
        data = file.read()

except FileNotFoundError as msg:
    print('File is not avl, please put correct file path',msg)
except PermissionError as msg:
    print('File is password protected , plz with auth',msg)'''

'''try:
    with open('a.txt','r') as file:
        data = file.read()

except (FileNotFoundError,PermissionError,EOFError) as msg:
    print(msg)'''

#CustomeException--oops

'''age = int(input('Enter your age:-'))

if age<=120:
    print('correct age')
else:
    print('age is not in range')'''


# class AgeLimitError(Exception):
#     '''Custom Exception for age limit validation'''
#     def __init__(self,age,message='Age is not within the allowed limit'):
#         self.age = age
#         self.message= message
#         super().__init__(self.message)
#
# def check_age(age):
#     if age<=18:
#         raise AgeLimitError(age,'Age is too low ,Must be 18 or older')
#     elif age>=60:
#         raise AgeLimitError(age,'Age is too high,must be 60 or younger')
#     else:
#         print('Age is within the allowed limit')
#
# age = int(input('Enter your age:-'))
# check_age(age)
#database connection with python




class FamilyMemeberlimit(Exception):
    '''Custom Exception for Familt Member limit validation'''
    def __init__(self,child_count,message='Age is not within the allowed limit'):
        self.child_count = child_count
        self.message= message
        super().__init__(self.message)

di = {'Father':'A','Mother':'B','Child':3}
def family_check(di):
    if di['Child']>2 or di['Child']<0:
        raise FamilyMemeberlimit(di['Child'],'for this program 2 or less than 2 child')
    else:
        print('Good')

family_check(di)

#check the ip adrees , if ip address is wrong then raise error.

#db connection
#re


Monday :- DB Mysql + ETL Testing (Database Testing)

UI
API
ETL


