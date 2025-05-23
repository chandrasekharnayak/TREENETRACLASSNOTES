'''
text file(txt, tabular)
binary file (image,music, video)
'''
'''
how to handel a file.
1.we will open that file.:- open()
2.in variable we declare that file
3.file_name or location , mode(read, write, append)
'''

var = open('class_3_datatype_int_float,comp,bool.txt','r')
#read :- read entire the file, what ever present in it.
#readlines :-
'''data = var.read()
print(data)'''

'''data = var.readlines()
print(data)'''

'''#escape charcter
print('\n \n it\'s')'''


'''var = open('a.txt','r')
data = var.read()
split_data = data.split()

count = {}

for i in split_data:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)'''

'''var = open('aa.txt','r')
data = var.readlines()
for i in data:
    print(i.capitalize())'''


'''
read mode

1.based on file name and location it will open the file.
2.if file is nor Present , then w=i will raise a FileNotFoundError
3.read mode mainly use two methods
    i> read() :- read the entier file
    ii> readlines() :- read the number of line in file and closed in a list.

'''

'''var = open('a.txt','r')
data = var.read()
var.close()
print(var.closed)'''



#write mode and append mode
#with statement
#csv file and excel file work

#with statememnt :-
# with open a file and take care of close file automatically. no need to close a file by the programmer.
#with help of with keyword it will handel a nth number of file.

'''
with open(filename or location) as variable:
    statement
    
with open(filename or location) as variable1,open(filename or location) as variable2....nth:
    statement 

'''

'''with open('a.txt','r') as f1, open('class_3_datatype_int_float,comp,bool.txt','r') as f2:
    data = f1.read()
    print(data)

    dat2 = f2.readlines()
    print(dat2)
print(f1.closed)'''

#write and append :-

'''
it will serach file and modify it.
if file is not avl in mentioned location,then what ever file name given by the programmer , write create the same file.
if file is avl, and inside the file data also avl, then write mode overwrite all the data.

#append :- same as write.
if file avl, and inside file data is avl , then it will continue data after the old data completed.

'''

#write
#writelines

'''with open('a.txt','w') as f1:
    f1.write('i love india')'''

'''with open('a.txt','a') as f1:
    f1.write('\nindian is the best one')'''

'''with open('b.txt','a') as f:
    f.write('qwerty')'''

'''with open('a.txt','r') as f1, open('b.txt','a') as f2:
    data_f1 = f1.readlines()
    f2.writelines(data_f1)'''

#binary file (img, video, mp3, mp4, pptx)

'''with open('JAVA.png','rb') as f:
    data = f.read()
    print(data)'''

#how to handel CSV file and excel file.

#how create a csv file with help of the python and how to insert the data in that file.

import csv

'''data = [
    ['Ajit',26,78000],
    ['Antaryami',29,91000],
    ['Chandan',29,87000]
]

with open('test_data.csv','w') as f1_csv:
    writer = csv.writer(f1_csv)
    writer.writerow(['Name','Age','Salary'])
    writer.writerows(data)'''


#create csv file with hepl of python, write insert some data.
#name,age,salary,address
'''data = [
    ['Ajit', 26, 78000,'Bhadrak'],
    ['Antaryami', 29, 91000,'Chilika'],
    ['Chandan', 29, 87000,'Kendrapada'],
    ['Dezzi',29,93000,'Bhadrak'],
    ['Aishwarya',28,86000,'Bhadrak']
]

with open('test_data.csv','w') as f1_csv:
    writer = csv.writer(f1_csv)
    writer.writerow(['Name','Age','Salary','Address'])
    for i in data:
        if i[-1]=='Bhadrak':
            writer.writerow(i)'''

'''with open('test_data.csv','r') as f1_csv:
    reader = csv.reader(f1_csv)
    for data in reader:
        print(data)'''


'''import pandas

read_csv = pandas.read_csv('test_data.csv')
print(read_csv)'''

#how to handel excel file and work on it.

'''import pandas as pd

data = {
    'Name':['Chandan','Ajit','Antaryami'],
    'Age':[29,29,28],
    'salary':[89000,82000,91000]
}

df = pd.DataFrame(data)

df.to_excel('test_data.xlsx',index=False)'''


















