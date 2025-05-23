import json
import mysql.connector

json_file = open('data.json', 'r')
json_data = json_file.read()
json_data = json.loads(json_data)

conn = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'Password@108',
    db ='AT18'
)


cursor = conn.cursor()

#table create
"""create_table_query = '''

create table if not exists JSONTable (
    id int,
    name varchar(25),
    category varchar(25),
    price int,
    stock int,
    description varchar(255)
    );

'''

cursor.execute(create_table_query)
conn.commit()"""

#inser query

insert_quer = 'insert into JSONTable (id,name,category,price,stock,description) value (%s,%s,%s,%s,%s,%s)'


for i in json_data:
    values = (i['id'],i['name'],i['category'],i['price'],i['stock'],i['description'])
    cursor.execute(insert_quer,values)

conn.commit()


#
# cursor.close()
# conn.close()