#decorater:- decorater is  a function it's  take another functioname as parameter to modify the exitsting functionality
# of the exitsing function.for creating the relation with exiting function need to use @and decore function name above of the function.

'''def decore(func):
    def sub(a,b):
        res = a-b
        return res,func(a,b)
    return sub

@decore
def cal(a,b):
    res = a+b
    return res

print(cal(10,20))'''
from time import daylight

# def decore(func):
#     def f1_modify(name):
#         return f'Hi {name} Good morning'
#     return f1_modify
#
#
# @decore
# def f1(name):
#     return f'Hi good morning,{name}'
#
# print(f1('Sritam'))

'''def decore(func):
    def list_odd_fetch(li):
        return [i for i in li if i%2!=0]
    return list_odd_fetch

@decore
def list_even_fetch(li):
    return [i for i in li if i%2==0]

li = [90,78,67,91,23,43,66,44,34,57]
print(list_even_fetch(li))'''


'''def decore(func):
    def sum_li(li):
        res = 0
        for i in li:
            res = res+i
        return res,func(li)
    return sum_li


@decore
def list_even_fetch(li):
    return [i for i in li if i%2==0]

li = [90,78,67,91,23,43,66,44,34,57]
print(list_even_fetch(li))'''

'''def decore(func):
    def string_fetch(li):
        str_li = [i.capitalize() for i in li if type(i)==str if i.isalpha()]
        return str_li,func(li)
    return string_fetch


@decore
def new_li(li):
    res = sum([i for i in li if type(i)==int])
    return res

li = [10,20,'78','qwerty',90,'900','ctc']

print(new_li(li))'''


'''def decore(func):
    def cube(a,b):
        res = a**3+b**3
        return res, func(a,b)
    return cube



@decore
def function(a,b):
    res = a**2+b**2
    return res

print(function(10,20))'''

#what is decorator chaining


# def bold_decorator(func):
#     def inner_function():
#         return f'<b>{func()}</b>'
#     return inner_function
#
# def intalic_decoratoe(func):
#     def inner_function():
#         return f'<i>{func()}</i>'
#     return inner_function
#
# @bold_decorator
# @intalic_decoratoe
# def html_text():
#     return 'decorators are very powerfull'
#
# print(html_text())

'''def decore_price_tax_added(func):
    def inner_prepaid_tax_added(days,per_day_price=15):
        gst = 18/100
        total_amount_days = per_day_price * days
        gst_added = total_amount_days * gst
        total_calculate = total_amount_days + gst_added
        return total_calculate
    return  inner_prepaid_tax_added



def decore_price_change1(func):
    def inner_prepaid_bill(days,per_day_price=15):
        total_amount = per_day_price*days
        return total_amount
    return inner_prepaid_bill

@decore_price_tax_added
@decore_price_change1
def prepaid_bill(days,per_day_price=10):
    total_amount = per_day_price*days
    return total_amount

print(prepaid_bill(20))'''

#Generator :- Generator is a function , who generating obj one by one, instead of return keyword of it is using yiled keyword and next() function helps to  generating obj.


# def f1(li):
#     for i in li:
#         yield i
#
# li = [10,20,30,40,50]
#
# obj = f1(li)
#
# for i in range(5):
#     print(next(obj))


# action_chain ----
# wifi
# port
# 64,71,89
#
# signal
# 5 , 4
#
# WAN -- 3
#
# LAN - 2
#
#
# []


'''
def wifi(li):
    for i in li:
        yield i

device_check_list = ['port-64','post-71','port-89','signal-5g','signal-4g','WAN-CBL-1','WAN-CBL-2','WAN-CBL-3','LAN-CBL-1','LAN-CBL-2']

wifi_check = wifi(device_check_list)

for i in range(10):
    print(next(wifi_check))'''



iter()
recursion or recurive function

(programming)


Module and Pachages-- 2days