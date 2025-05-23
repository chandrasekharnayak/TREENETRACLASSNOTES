'''what is an operator in python?
operator is a symbol or word or char , who have some spe. operation. those known as operator

1.Arithmetic operator
2.Relational Operator or comparision op.
3.Logical operator
4.assignment operator
5.Bitwise Opeartor
6.Special Operator :- (Idenitity op, Membership)

'''
# 1.Arithmetic operator(+,-,*,/,//(floor div), %(modulo), **(exponent))
'''int+int
float+float
complex+complex
string+string'''
# print('A'+'B')
# print('A'*3)
# print(10/2)
# print(10//3)
# print(10%3)
# print(3**3)


# 2.Relational Operator or comparision op.
# >,>=,<,<=, ==(check both the values are same or not), !=check both the values are differenet or not)
# print(10!=11)

#3 Assignemet op(=)
# x = 10
# # x = x+10 (compound  assignment op)
# y = 20


#logical operator (and, or , not)
# and (if bothe the condition is correct, then answer should be True,
'''True True  True
True False  False
False True  False
False False False '''

#or (if one of the cond is True, then answer should be True)
'''True  True   True
True False True
False True True
False False False '''

#not :- it's a complimement
'''print(not False)
'''

#Special op:-
'''
identity op:- (when both the values are in same place or location should be equal , then is called identity operator.)  is
membership op:- (its check the given element is present or not in collection)

'''

'''a = 10
b = 20

print(a is b)'''

'''li = [10,20,30]
print(10 in li)'''


# input and output statement

# user inputs :- take the data from end user and customer. input is python inbuilt function who take data from user end.

'''input is a function, its use for take data from user, but every data taken by only string, and based on our requirement, we should type cast data.'''


'''var = float(input('Enter a number:-'))
print(type(var))'''