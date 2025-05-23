'''li = [10,20]
li.add(30)'''

# 10/0

# print())

# li = [10,20,30]
# print(li[6])
'''
di = {'Name':'A','Age':27}
print(di['Address'])
AttributeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError'''

'''def f1(a,b):
    pass

print(f1(10))'''


# # var = int(input('Enter a number'))
#
# a = int(input('Enter a number:-'))
# b = int(input('Enter a number'))
#
# res = a/b
#
# print(res)


'''try:#Write Risky code
    a = eval(input('Enter a number:-'))
    b = eval(input('Enter a number'))

    res = a/b

    print(res)

except ZeroDivisionError as msg:# If code raise any issue, here we mention Exception name for handel the exceptions
    print('Please provide a non zero number:-',msg)

except ValueError as msg:
    print('Please provide int numberP:-',msg)

except Exception as msg:
    print(msg)'''





'''try:#Write Risky code
    a = eval(input('Enter a number:-'))
    b = eval(input('Enter a number'))

    res = a/b

    print(res)

except (ZeroDivisionError,ValueError,TypeError) as msg:
    print(msg)

except Exception as msg:
    print(msg)

finally:#100% execute code'''


'''try:
    file = open('rouh.txt','r')
    content = file.read()

except (FileNotFoundError,PermissionError) as msg:
    print(msg,'please provide the accurate file location')

else:
    print('File read successfully')
    print(content)

finally:
    file.close()
    print('Closing file')'''

#create a own custom exception

'''class AgeLimitError(Exception):

    def __init__(self,message):
        super().__init__(message)


def check_age(age):
    if age<18:
        raise AgeLimitError('Age is less than the minimum limit of 18.')
    elif age>60:
        raise AgeLimitError('Age is more than the maximum limit of 60.')
    else:
        print('Age is within the valid range')


try:
    age= int(input('Enter your age:-'))
    check_age(age)
except AgeLimitError as msg:
    print(msg)'''


print('C'+'D')
print('C'+2)
















