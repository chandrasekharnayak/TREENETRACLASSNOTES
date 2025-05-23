'''var = open('/Users/macos/Desktop/XpsBackup/TREENETRA/Treenetra_class_notes/TREENETRA_AT-5/class_1_2_python_introduction.txt','r')

data = var.read()
print(data)'''
from os import write


# file = open('treenetra.txt','r')
'''
read method, read the file contains from core as string.
if the file is not thier, then its return no such file or directory on File NotFoundError.
each and every file come from in python as string, every line using \n for create it.
read()
read(n)
readline()
readline()
'''



'''data = file.read(100)
print(data)'''

'''data = file.readline()
print(data)

data1 = file.readline()
print(data1)

data2 = file.readline()
print(data2)'''

# data = file.readlines()
# print(data)
# print(data[1])

'''for i in data:
    print(i)
'''
# print("qwerty \"poiuy")

'''there is a file many lines
open a file, read the last line of this file'''

'''file = open('treenetra.txt','r')

data = file.readlines()
print(data[-1])'''

# i want the check the data, in mid position list 'Kureshi' is avl or not

'''file = open('name.txt','r')
data = file.readlines()
mid = (len(data)//2)+1

if 'Kureshi' == data[ mid-1][:-1]:
    print('Kureshi is avl')
else:
    print('Kureshi is not avl')'''

#there is a file, file have 20 names line by line, print those name whose first char of the name is starts from A and position

'''var = open('name.txt','r')
data = var.readlines()'''

'''li = [10,20,30,40]

for index,value in  enumerate(li):
    print(index,value)'''


'''for index,value in enumerate(data):
    if value.startswith('A'):
        print(index,value)'''


#write
# if the file is not avl on spesific location, then its create a own file.
#if file is avl, and inside the file data also avl, then its override the old data.


#append
# if the file is not avl on spesific location, then its create a own file.
#if file is avl, and inside the file data also avl, then its not override the old data
'''


write
writelines
'''

'''li = ['\nABCD\n','EFGH\n','XYZ']
var = open('treenetra.txt','a')
# var.write('\ncurrently we are in file handleing chapter')
var.writelines(li)'''

'''
create file help of write mode
serach in google , "green house theorm", fetch text in python,
write all the data in a file. and read it
read the file and collect data.
append in a new file.'''

'''file1= open('file1_write','w')
data = ["The greenhouse effect is a natural process that occurs when greenhouse gases in the Earth's atmosphere trap heat from the sun\n"," warming the planet and making it habitable\n","The gases act like the glass walls of a greenhouse, which is where the term comes from.\n "]
file1.writelines(data)'''

'''read_file = open('file1_write','r')
read_data = read_file.readlines()
print(read_data)

file2 = open('file2_append','a')
file2.writelines(read_data)'''

#with statement :- open the file and close the file carefully. and based on req, its working multiple files.

'''with open('name.txt','r') as file, open('rough.txt','r') as file2:

    data = file2.read()
    print(data)
    data1 = file.read()
    # print(file.closed)
    print(data1)
'''
#---------------------
'''csv file(comma separated values)
excel file
zip'''

import csv
# print(dir(csv))
# writerow,
# writerows

'''data = [
    ['Name','Age','Salary','Adreess'],
    ['Aditya',26,56000,'Bhubaneswar'],
    ['Apurv',27,58000,'Cuttack'],
    ['Rahul',27,540000,'baleswar'],
    ['Satish',27,870000,'RKL'],
]


with open('data1.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)
'''

'''data = [
    ['Nigam',28,67000,'Baripada'],
    ['Nilanchal',28,780000,'BRM']
]

with open('data1.csv','a',newline='\n')  as csv_file_append:
    csv_writer = csv.writer(csv_file_append)

    for i in data:
        csv_writer.writerow(i)'''

'''import csv

with open('data1.csv','r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)'''

#read the csv file and store the all data in list of dictionary

# How to zip a file.
from zipfile import ZipFile
# print(dir(ZipFile))

'''file_to_zip = 'data1.csv'
zip_file_name = 'data1_csv.zip'

with ZipFile(zip_file_name,'w') as zipf:
    zipf.write(file_to_zip)
    print('Zip Successful')
'''
# extractall:- unzip all files

# zip_file_name = 'data1_csv.zip'
#
# with ZipFile(zip_file_name,'r') as zipf:
#     zipf.extractall('unzipped_files')

'''
get the email, compose a email, put the email id and write normal message,
zip a file with python, attached this zip file in mail.
then click sent

'''



















