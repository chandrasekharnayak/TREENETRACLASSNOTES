'''
text file(text,csv,excel,word)
binary file(image,png,jpeg,mp3,mp4)
'''

'''syntax

open(file_path,mode)'''

# var = open(r'T:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_41_oops_class_1.txt','r')
# data = var.readlines()
# n = len(data)
#
# for i in range(n):
#     if i==10-1:
#         break
#     print(data[i])


'''read mode :-
read()
read(n)
readline()
readlines()
'''

#escape char in python
# print('hi it\'s hello')

#write :-

# var = open(r'T:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\gogo.txt','a')
# var.write('\nhuman\nAnimal')

# var = open(r'T:\dataFile.csv','w')
# # var.write()
# var.close()
# print(var.closed)

'''with open(r'T:\dataFile.csv','r') as var,open(file_path,'r') as var1:
    var.read()
print(var.closed)'''

# how handel csv file and excel handel
# how handel json file in python
# how handel binary file in python

#how to create a csv file and insert the data.

'''import csv

data_column = ['id','Name','Age','Salary']

data_rows = [
    [101,'Sarat',27,89000],
    [102,'Debasish',28,88000],
    [103,'Akash',29,90123]
]

with open('output.csv',mode='w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(data_column)
    csv_writer.writerows(data_rows)'''

# how to read the data from csv

'''import csv

with open('output.csv',mode='r') as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        for j in i:
            print(j,end=' ')
        print()'''


#Handel a json file
import json
# print(dir(json))
# dumps:- convert a dict to byte string(json)
# loads = convert byte string to dict
'''
with open('new_data.json',mode='r') as file:
    json_reader = file.read()
    json_loads = json.loads(json_reader)
    print(type(json_loads))'''


#create a json file help of python.
'''import json

json_data = {
    'id':101,
    'salary':89000,
    'Age':27
}

with open('create_json.json',mode='w') as file:
    dict_convert_json = json.dumps(json_data)
    json_writer = file.write(dict_convert_json)'''


#read a binary file

with open(r'C:\Users\TREENETRA\Downloads\WhatsApp Image 2024-07-12 at 6.09.51 PM.jpeg',mode = 'rb') as file:
    print(file.read())





