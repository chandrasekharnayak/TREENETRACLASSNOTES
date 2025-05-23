#To Create Zip

'''from zipfile import *
# print(dir(zipfile))

file = ZipFile('file_csv.zip','w',ZIP_DEFLATED)
file.write(r'T:\output_csv.csv')
file.write(r'T:\data_csv_handel.csv')'''

#unzip

from zipfile import *
file = ZipFile('file_csv.zip','r',ZIP_STORED)
name = file.namelist()
print(name)
for file_name in name:
    if file_name == 'output_csv.csv':
        f1 = open(file_name,'r')
        print(f1.read())

