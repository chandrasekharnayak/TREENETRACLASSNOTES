# var = open('rough.txt', 'r')
# read_all_data = var.read()
# print(type(read_all_data))

# read_line_by_line_data = var.readlines()
# print(read_line_by_line_data)


#write :- if file is already exits , the what ever data had written in that file, all the datas going to overriden
            # if the file is not avl, then in that same path it's a another file.
# and append

# var = open('/Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_19/PythonConnectWithMysql/rough1.txt','w')
# var.write('wersrtfdcghvg')

#write
#writelines

'''var = open('rough.txt','a')
# var.write('\n jkghvghvhjgvcjftjy')
# var.writelines(['\nabcd\n','DEF\n'])
var.close()
print(var.closed)'''


'''with open('rough.txt', 'r')  as file,open('abcd.txt','a') as file2:
    data = file.readlines()

    file2.writelines(data)

print(file.closed)'''


#csv :- comma separated vlaue

import csv
'''print(dir(csv))
# writer
# reader'''

colms = ['Name','Age','Salary']

rows = [
    ['Aditya',27,90],
    ['buzzzy',29,110],
    ['Sima',24,78],
]
file_name = 'data.csv'

with open(file_name,'a') as file:
    write = csv.writer(file)
    # write.writerow(colms)
    # write.writerows(rows)
    for i in rows:
        write.writerow(i)