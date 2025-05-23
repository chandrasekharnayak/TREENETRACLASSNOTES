#how top open a file and read a file and write file.

#how to open and handel file

#syntax
# var = open('file_path','mode')

# mode :- read(r),write(w),append(a)
'''read --- only read the file, no changes. If file is not their then raise Error(FileNotFoundError)
write:- If file is available based on the requirement is override the data and put the new data.
        if file is not available then in the same location create a file and write data.not

append :-If file is available based on the requirement is continue the data from next line and put the new data.
        if file is not available then in the same location create a file and write data.not'''


'''var = open('T:\\TREENETRA\\Treenetra_class_notes\\Treenetra_AT-4\\class_3_idenitifiers.txt','r')
#read, read(n), readline(),readlines()
# file_contenet = var.read()
# print(file_contenet)

file_contenet = var.readlines()
print(file_contenet[0:2])

var.close()
print(var.closed)'''


#with statement:-

'''with open('T:\\TREENETRA\\Treenetra_class_notes\\Treenetra_AT-4\\class_41_logging_1.txt','r') as var1, open('T:\\TREENETRA\\Treenetra_class_notes\\Treenetra_AT-4\\class_38_decorators.txt','r') as var2:

    file_content = var1.read()
    # print(file_content)

    file_content2 = var2.read()
    print(file_content2)'''


'''with open('pallindrom.py','w') as var1:
    # var1.write('var = lambda a:a==a[::-1]\nprint(var("madam"))\n#is override')
    var1.write('def is_pallindrom(s):\n    return s ==s[::-1]')'''

# with open('pallindrom.py','a') as var1:
#     var1.write('\nprint(is_pallindrom("madam"))')


'''with open('pallindrom.py','a') as var1:
    var1.writelines(['\nI am\n','I have\n','I was\n','I had\n'])'''

#handel the csv file and write some data in it

import csv
# print(dir(csv))

'''data = []

num_of_data = int(input('EN Num:-'))


for i in range(num_of_data):
    name = input('Enter your name:-')
    age = int(input('Enter your age:-'))
    salary = int(input('Enter your salary:-'))
    single_data = [name,age,salary]
    data.append(single_data)

print(data)

with open('C:\\Users\\TREENETRA\\OneDrive\\Desktop\\CSVPrac\\a1.csv','w',newline='') as var1:
    csv_write = csv.writer(var1)

    csv_write.writerow(['Name','Age','Salary'])
    csv_write.writerows(data)'''


#read csv

'''with open('C:\\Users\\TREENETRA\\OneDrive\\Desktop\\CSVPrac\\a1.csv','r') as var1:
    csv_reader = csv.reader(var1)
    for row in csv_reader:
        for i in row:
            print(i,end='     ')
        print()'''


'''import pandas as pd

df = pd.read_csv('C:\\Users\\TREENETRA\\OneDrive\\Desktop\\CSVPrac\\a1.csv')
print(df)'''
