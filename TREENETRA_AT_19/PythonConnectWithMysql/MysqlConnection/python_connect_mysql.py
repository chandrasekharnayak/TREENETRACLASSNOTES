import mysql.connector

#Database Connection help parameter


conn  = mysql.connector.connect(
    host='127.0.0.1',
    port= '3306',
    user='root',
    password = 'Password@108',
    database = 'AT18',
    # after creating the database line 23 to 27

)

# check db is connected or not
if conn.is_connected():
    print('Yes connted')
else:
    print('Not Connected')
#
# #pointer
cursor = conn.cursor()

#insert query
'''query_insert = 'insert into emp_filtering (emp_id,emp_name,emp_age,emp_dept,emp_salary) values (%s,%s,%s,%s,%s)'

values = (8,"Rahuk",24,"QA",89000)

cursor.execute(query_insert,values)

conn.commit()'''

#select

query_select = 'select * from emp_filtering'

cursor.execute(query_select)

results = cursor.fetchall()

print(results)


