# # li = [10,20,30]
# # li.apped(10)
#
# a = 10
# b = 0
#
# print(a/b)

# li =[10,20,30]
# li[4]

# di = {'name':'krishna','age':27}
# di['sda']

# print(10+'dfghj')

# def f1(a,b):
#     pass
# print(f1(10))
#
# a = [10,20,30]
# print(dict(a))


# data = int(input('enter a number:-'))


    #
    # try:
    #     data1 = int(input('Enter a number1:-'))
    #     data2 = eval(input('Enter a number2:-'))
    #     div = data1/data3
    #     print(div)
    #
    # except (ZeroDivisionError,ValueError,TypeError) as msg:
    #     print(msg)
    #
    # # except Exception as msg:
    # #     print(msg)
    #
    # finally:
    #     print('hello world')
    #
    #
    # age = 400

    # str = 'OK'
    # str.lwer()

# li = [10,20,30]
# print(li[4])

# di = {'Name':'Ankit','Age':24}
# print(di['Salary'])

# open('T:\\harishankar_3+_data_analysis.do','r')

# data = int(input())'Enter a number:-'


# def function(a,b):
#     try:
#         add = a+b
#         return add
#     except TypeError as msg:
#         print('please provide a valid number')
#
# print(function(10,'56'))
# d = 10
# def div(a,b):
#     try:
#         print(d)
#         c = int(input('Number:-'))
#         div = a/b
#         return div
#     except (ZeroDivisionError,TypeError,ValueError) as msg:
#         print(msg)
#     except Exception as msg:
#         print(msg)
#
# print(div(10,'op'))


class AgeOutRangeError(Exception):
    def __init__(self,message='Age out of range'):
        self.message = message
        super().__init__(self.message)


def validate_age(age):
    if age<1 or age>120:
        raise AgeOutRangeError('Age must be between 1year and 120 years')
    else:
        print('Age is valid')

try:
    validate_age(201)
except AgeOutRangeError as msg:
    print(msg,'Please provide a valid age')



























































































