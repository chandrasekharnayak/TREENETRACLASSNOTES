#mysql-connector-python

import mysql.connector

conn  = mysql.connector.connect(
    host='127.0.0.1',
    port= '3306',
    user='root',
    password = 'Password@108',
    database = 'AT18'# after creating the database line 23 to 27

)
#
#
#
# cursor = conn.cursor()
#
# #connection check
# '''if conn.is_connected():
#     print('Conncetd to Mysql database')
#
#
# #Db Creation with help python to mysql
# '''db_name = 'MysqlConnection'
# cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
#
# print(f'Database created {db_name}')'''
#
#
#
#
# #Excute your sql query
# '''cursor.execute('SHOW DATABASES')'''
# #fetch all database
# '''datbases = cursor.fetchall()
#
# for db in datbases:
#     print(db[0])'''
#
#
#
#
# #create table
# '''cursor.execute(f"""
# CREATE TABLE IF NOT EXISTS employees(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     department VARCHAR(200)
#     )"""
# )
#
# print("Table created.")'''
#
# #insert the data
# '''
# query = "INSERT INTO employees (name,age,department) VALUES (%s, %s, %s)"
# data = ("Subhasis",28,'Civil')
# cursor.execute(query,data)
# conn.commit()
# print('data inserted ....')
# cursor.close()
#
# #if nth number of data
# # create a list of tuple
#
# data = [(),(),(),()]
#
# for i in data:
#     cursor.execute(query,i)
#     conn.commit
#
#
# '''
#
# #fetch the table data and show
# '''cursor.execute("SELECT * FROM employees")
# for i in cursor.fetchall():
#     print(i)'''
#
# conn.close()
#
#
#
