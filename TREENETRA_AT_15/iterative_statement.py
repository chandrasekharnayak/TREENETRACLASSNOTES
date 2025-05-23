# st = 'ABCD'


'''
syntax:

for variable in collection_name:
    logic/statement/expression

'''
'''for var in st:
    print(var+'Z')'''

'''li = [10,20.89,7+9j,'Hi']

for var in li:
    print(var)'''

# range()
'''
syntax

range(start,end+1,step)
'''

# for var in range(1,10):
#     print(var)

# for var in range(2, 11, 2):
#     print(var)
#
# for var in range(1,11,2):
#     print(var)

# count = 0
# for i in range(10):
#     count =count+1
# print(count)

# *
# *
# *
# *
# *

'''for i in range(5):
    print('*')'''

# *
# **
# ***
# ****
# *****

'''for i in range(5):
    print('*'*(i+1))'''
'''for i in range(1,6):
    print('*'*i)'''

# *****
# ****
# ***
# **
# *

# for i in range(1,6):
#     print('*'*(6-i))


# *****
# ***
# *

# for i in range(1,6,2):
#     print('*'*(6-i))

#     *
#    **
#   ***
#  ****
# *****
# (4-i)
# 0 1 2 3 4 i
# 4 3 2 1 0  - exp

# for i in range(5):
#     print(' '*(4-i)+'*'*(i+1))

# *****
#  ****
#   ***
#    **
#     *

# for i in range(5):
#     print(' '*(i)+'*'*(5-i))

# for i in range(1,6):
#     print(' '*(i-1)+'*'*(6-i))

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

'''for i in range(1,6):
    print(' '*(5-i),end='')
    print("* "*i)'''