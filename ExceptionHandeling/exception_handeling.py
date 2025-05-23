# def division(a,b):
#     try:
#         result = a/b
#         return result
#     except (ZeroDivisionError,TypeError) as msg:
#         print('Handel the error',msg)
#
# division(10,0)
# division(10.,'10')

# WAF in try handel the ValueError in python.

# def function():
#     try:
#         user = int(input('data:-'))
#         return user
#     except ValueError as msg:
#         print(msg)

# print(function())

#write a function read a file and extract the line number1.

# def file_handel(file_path):
#     try:
#         with open(file_path,'r') as file:
#             data = file.readlines()
#             result = data[0]
#             return result
#
#     except (FileNotFoundError,TypeError) as msg:
#         print(f'Please provide another path, file is not avl:- {msg}')
#
#     except Exception as msg:
#         print(f'Please provide another path, file is not avl:- {msg}')

# file_handel('erty.txt')
# print(file_handel(r'T:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\Write\class_1_2_python_introduction.txt'))


'''KeyError,IndexError,NameError,ValueError

Customization Error, How to raise a error'''

'''logging.critical-----50
logging.warning---40
logging.ERROR--- 30
logging.debug-- 20
logging.info---10'''



# import logging
#
# logging.basicConfig(filename='error_log1.txt',level=logging.INFO,format='%(asctime)s -%(levelname)s - %(message)s')
# logging.info('Start the execution')
#
# def divide(x,y):
#     try:
#         result = x/y
#     except ZeroDivisionError as e:
#         print('Division by zero occured:-')
#         logging.exception(e)
#     except Exception as e:
#         print('An error occured')
#         logging.exception(e)
#     else:
#         return result
#
# result1 = divide(10,0)
#
#
# result2 = divide(10, 'qwert')
#
#
# result3 = divide(10,2)
# print(result3)






# import logging
# logging.basicConfig(filename='division_log.txt',level=logging.INFO)
# logging.info('A new inforomation request came')
#
# try:
#     x = eval(input('Enter a first number:-'))
#     y = eval(input('Enter a second number:-'))
#     print(x/y)
#
# except ZeroDivisionError as msg:
#     print("can not divided with zero")
#     logging.exception(msg)
#
# except TypeError as msg:
#     print("Only int value allowed")
#     logging.exception(msg)
#
# logging.info('Request Processing Completed')



# import logging
# logging.basicConfig(filename='exception.log',level=logging.INFO,format='%(asctime)s -%(levelname)s - %(message)s')
#
# logging.info('A new request came')
# def divide_by_two(a,b):
#     try:
#         result = a/b
#     except (ZeroDivisionError,TypeError,ValueError) as msg:
#         logging.exception(msg)
#     else:
#         return result
#
# logging.info('Request Processing Completed')
#
# divide_by_two(10,0)
# divide_by_two(10,'qw')
# divide_by_two(10,2)


#Custom Error

class InvalidAgeError(Exception):
    def __init__(self,age,message = 'Age must be between 1 and 120'):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.age}--> {self.message}'

def validate_age(age):
    if not 1 <= age <= 120:
        raise InvalidAgeError(age)
    else:
        print('Valid age:-',age)


try:
    userage = int(input('Enter a age:-'))
    validate_age(userage)
except InvalidAgeError as msg:
    print(msg)























