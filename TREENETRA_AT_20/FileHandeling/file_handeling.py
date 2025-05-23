# lofcation  --- oepn ---- data --- variable


# variable = open('location','mode')

'''
there are 3 types of modes are avl.
read---r
write---w
append---a
'''

'''
read mode 

read(), read(n)
readline()
readlines()

'''
# var = open(r'C:\Users\TREENETRA\PycharmProjects\TREENETRACLASS\TREENETRA_AT_20\FileHandeling\f1.txt','r')
# # read()
# res = var.read()
# print(res)

# readline
'''res = var.readline()
print(res)

res2 = var.readline()
print(res2)

res3 = var.readline()
print(res3)'''

#readlines
# res = var.readlines()
#
# for i in res:
#     print(i)


# String Escape char

'''
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace


'''

# print('hello ,it\'s a ball')
# print('hello world \thello pakistan ache ho, or \\ kuch chaheiye\b')


#write mode and append

# 1.if file is avilable , then modify the file.
#if file is avl, and inside the file contenet is avl, then the write method override all the data

# there are two methods in write mode
# write
# writelines
# var = open(r'C:\Users\TREENETRA\PycharmProjects\TREENETRACLASS\TREENETRA_AT_20\FileHandeling\f2.txt','w')
# var.write('I love india')
# data = ['I love india\n','here is beauty of states showing his capabilities\n','thanks']
# var.writelines(data)\

# var = open(r'C:\Users\TREENETRA\PycharmProjects\TREENETRACLASS\TREENETRA_AT_20\FileHandeling\f3.txt','w')
# var.write('I love india')

#append

# var = open(r'C:\Users\TREENETRA\PycharmProjects\TREENETRACLASS\TREENETRA_AT_20\FileHandeling\f3.txt','a')
# # var.write('\nqwerytylknkljbjkbhjk')
# data = ['\nI love india\n','here is beauty of states showing his capabilities\n','thank']
# var.writelines(data)

#testing ---- test data (csv,excel,json)

#csv and excel


data = [
    ['Name','Age','Salary'],
    ['Abhay',27,890000],
    ['Abnhilash',28,91000],
    ['Sulkant',29,98000]
]

#write the data in csv file.
# import csv
#
# file = open('test1.csv','w',newline='')
#
# writer = csv.writer(file)
# # writer.writerow(['Name','Age','Salary'])
# writer.writerows(data)

#read the data in csv file

# import csv
#
# var = open('test1.csv','r')
# reader = csv.reader(var)
#
# for i in reader:
#     print(i)



import pandas as pd

#Basic Read
# df = pd.read_csv('test1.csv')
# print(df)

#read without headers

# df = pd.read_csv('test1.csv',header=None)
# print(df)

#read with custom column name

# df = pd.read_csv('test1.csv',names=['Age','salary'])
# print(df)

#skip the rows

# df = pd.read_csv('test1.csv',skiprows=1)
# print(df)


#writing to csv file help of pandas

# import pandas as pd
#
# #write DataFrame to csv
#
#
# data = {
#     'Name':['Abhay','Anshuman','Bedant','Ragav','Abhishek'],
#     'Age':[23,24,25,26,27],
#     'Pincode':[751003,751004,751005,751006,751007]
# }
#
# df = pd.DataFrame(data)
#
# df.to_csv('output.csv',index=False)



#with statement

# with is statement, and its take care about the file opening and closing, as well with help of with statement, here we will work multiple
# files in a single time

# syntax
# with open(location , mode) as variable_name:
#     statement


# with  open(r'C:\Users\TREENETRA\PycharmProjects\TREENETRACLASS\TREENETRA_AT_20\FileHandeling\f1.txt','r') as file:
#     data = file.read()
#     print(data)
#     print(file.closed)
# print(file.closed)


#Read the excel data help panads

import pandas

# df = pd.read_excel('f1.xlsx')
# print(df)


#write the data in excel

data = {
    'Name':['Abhay','Anshuman','Bedant','Ragav','Abhishek'],
    'Age':[23,24,25,26,27],
    'Pincode':[751003,751004,751005,751006,751007]
}

df = pd.DataFrame(data)

df.to_excel('f2.xlsx',index=False)














