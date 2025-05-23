'''                        BaseException


Exception                                    SystemExit     GeneratorExit     KeyboardInterrupt

AttributeError  ArithmeticError EOFError  NameError LookupError   OSError  TypeError  ValueError
                ZeroDivisionError                   IndexError    FileNotFoundError
                FloatingPointError                  KeyError      InterruptedError
                OverflowError                                     PermissionError
                                                                  TimeoutError'''


'''AttributeError
ZeroDivisionError
NameError
IndexError
KeyError
FileNotFoundError
PermissionError
TimeoutError
ValueError
TypeError'''

#attribute Error
'''class A:
    def f1(self):
        pass

obj = A()
obj.f2()'''

'''li = [10,20,30]
print(li[3])'''

'''di = {'name':'a','age':21}
print(di['salary'])'''

# a = int(input("Enter your nu"))

'''try 
except
else
finally'''

'''try:
    first_num = eval(input('Enter a number:-'))
    sec_num = int(input('Enter a number:-'))

    result = first_num/sec_num

except (ZeroDivisionError,ValueError) as msg:
    print(f'Check the error and Resolve it:- {msg}')

except Exception as msg:
    print(f'Check the error and Resolve it:- {msg}')

else:
    print(result)

finally:
    print('please check answer')'''



'''from selenium import webdriver
from selenium.common.exceptions import WebDriverException


driver = webdriver.Chrome()
try:
    driver.get('https://www.facebook')
except WebDriverException as msg:
    print(f'Some error is happen:-{msg}')

finally:
    print('check')
    driver.quit()'''


#How to create a custom error

'''class AgeLimitError(Exception):
    def __init__(self,message):
        self.mesaage = message
        super().__init__(message)

def validate_age(age_in_month):
    max_age_in_month = 12*120
    min_age_in_month = 1

    if age_in_month <min_age_in_month or age_in_month >max_age_in_month:
        raise AgeLimitError(f'Age {age_in_month} month is out of allowed range(1month to 120 years).')


age = int(input('Enter your age'))

try:
    data_age = age*12
    validate_age(data_age)
except AgeLimitError as msg:
    print(msg)
else:
    print(f'perfcer age:-{age}')'''



'''Batch12 Testing

#selenium :- 8am (Tushar sir)
#Manul testing :- 7pm (Amir sir)

Batch12 Dev + Batch11 Dev
#Django:- 9:20am to 10:20am(me)

Batch 13(T+D)
#Python :- 8:15am to 9:15am

#AT 11 (Testing) + Int grp all can
#Robot Frame: 7:10am to 8:10am'''








