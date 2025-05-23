try:
    number1 = int(input('Enter your first number:-'))
    number2 = int(input('Enter your second number:-'))

    div = number1/number2
    print(div)

except (ZeroDivisionError,ValueError,TypeError) as msg:
    print(msg)
except Exception as msg:
    print(msg)



