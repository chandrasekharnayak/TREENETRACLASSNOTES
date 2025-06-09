# from werkzeug.serving import connection_dropped_errors
#
# try:
#     Risky code
#
# except:
#     Handel the exception based on exception name
#
# finally:
#     unrisky code
#
# #db coonection
#
# try :
#     db connection_dropped_errors
#
#
# except:
#
# finally:
#     connect_break
from TREENETRACLASSNOTES.TREENETRA_AT_15.Selenium.wait.explicit_wait import click_became_a_seller

#

try:
    li = []
    data1 = eval(input('Enter a number1:-'))
    data2 = eval(input('Enter a number2:-'))
    res = data1/data2
    li.add(res)

except ZeroDivisionError as msg:
    print('not possiable divided with zero, please provide a non-zero number')
    data1 = eval(input('Enter a number1:-'))
    data2 = eval(input('Enter a number2:-'))
    res = data1 / data2
    print(res)


except TypeError as msg:
    print('not use different type data when division is going on')


except Exception as msg:
    print(msg)

all the exception name,
each exception use case
custom exception











