#In python there are 2 types of file is thier.

'''1.Text File (text,json,word,ppt,excel,csv)
2.Binary File (image,video,audio)'''
import csv

'''
 syntax:-
 
 open('file_path','mode')
 
 mode :- read, write and append --- r,w,a
 read --- only options
 w ----- write option(with override)
 a --- write option (without override)
 '''
'''Escpae char in python:- 
use \
\' :- single quote
\\ :- backslash
\n = new line
\t = tab
\b :- back space

'''

# s = 'hi, it\'s a ball ,\t ok come'
# print(s)

'''
read :-

read():- read all the file's contained
read(n):-read number char 
readline:- at a single time read single line.
readlines
'''

# var = open('T:\\TREENETRA\\Treenetra_class_notes\\TREENETRA_AT-5\\class_1_2_python_introduction.txt','r')
# print(var.read())
# print(var.read(8))

'''data1 = var.readline()
print(data1)

data2 = var.readline()
print(data2)

data3 = var.readline()
print(data3)'''

'''data = var.readlines()'''

'''enu_data = enumerate(data)

for index, value in enu_data:
    print(index,value)'''


#write and append mode
'''
write
writelines
'''

'''write :- 1.if file is exit and in the file some data thier, then write method override the data and insert the new data
            2. If the file is not avilable in mentioned path, then in the same path create mentioned file and then write the data'''

# var = open(r'T:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\Write\class_1_2_python_introduction.txt','a')
# var.write('sdrbjknlmtgfvyhjv234576890276890svjhbknlryctlvjhbknk\ndtyfgukhljdtfynhklcghvj')

# '''var = open(r'T:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\Write\a.txt','w')
# # var.write('xgj')
#
# li_str = ['hi how are\n','ok what is going on \n', 'how to manage']
# var.writelines(li_str)'''


# var = open('T:\\TREENETRA\\Treenetra_class_notes\\TREENETRA_AT-5\\Write\\a.txt','r')
# var.close()
# print(var.closed)

#Advanatage of with
'''with is open the file, as well it's only take the close of file and at a single time with handel multiple files'''

#with open('T:\\TREENETRA\\Treenetra_class_notes\\TREENETRA_AT-5\\Write\\a.txt','r') as var1,open(r'T:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\Write\class_1_2_python_introduction.txt','a') as var2:
    # data = var1.read()
    # print(data)

    
# print(var1.closed)


# how to handel csv file and excel file
#write
#read


#write csv data
# import csv
#
# with open('T:\\data_csv_handel.csv','w',newline='') as file:
#     csv_writer = csv.writer(file)
#     column_data = ['ID','Name','Salary','Dept']
#     csv_writer.writerow(column_data)
#
#     num = int(input('How many data you want to enter in csv:-'))
#
#     for i in range(num):
#         id = int(input('Enter a your id number:-'))
#         name = input('Enter a your name:-')
#         salary = int(input('Enter a your salary:-'))
#         dept = input('Enter a your dept name:-')
#         csv_writer.writerow([id,name,salary,dept])
#     print('Sucessfull')


# read csv data

# import csv
# with open('T:\\data_csv_handel.csv','r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)


#how  to handel csv(csv and panads
#How  to handel excel(pandas)
#how to handel binary files

#zip file handel

'''import csv


with open('T:\\dataFile.csv','a',newline='') as file:
    csv_writer = csv.writer(file)
    columns = ['Id','Name','Salary','Department']
    csv_writer.writerow(columns)
    num = int(input('How many datas:-'))

    for i in range(num):
        id = int(input('Enter your id:-'))
        name = input('Enter your name:-')
        salary = int(input('Enter your salary:-'))
        dept = input('Enter your dept:-')
        csv_writer.writerow([id,name,salary,dept])

    print('Sucessful')'''


'''with open('T:\\dataFile.csv','r') as file:
    read = csv.reader(file)
    # print(read)

    for i in read:
        for j in i:
            print(j,end= ' ')
        print()'''

               
#write the data in excel help of pandas

import pandas as pd

#dataFrame

data = {
    'ID':[101,102,103],
    'Name':['A','B','C'],
    'Salary':[67878,67897,56788],
    'Dept': ['QA','Dev','UAT']
}
df = pd.DataFrame(data)

df.to_excel('T:\\output_excel.xlsx',index=False)
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               










