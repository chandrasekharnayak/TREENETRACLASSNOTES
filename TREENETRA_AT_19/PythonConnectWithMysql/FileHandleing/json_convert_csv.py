import json
import csv
import mysql.connector



#json file handleing

'''with open('reqres.json','r') as json_file:
    json_reader = json_file.read()
    json_data = json.loads(json_reader)'''


#columns creation
'''json_clms = list(json_data['data'][0].keys())
'''
# rows
'''json_rows = []
'''
# rows creation
'''for i in json_data['data']:
    json_rows.append(list(i.values()))'''

#csv file creation
'''with open('json_data_csv.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(json_clms)
    writer.writerows(json_rows)'''


#csv file read


csv_data = []
with open('json_data_csv.csv','r') as csv_read:
    reader = csv.reader(csv_read)
    for i in reader:
        csv_data.append(i)

print(csv_data)


# db_connection
conn = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'Password@108',
    db ='AT18'
)

cursor = conn.cursor()

#table create
create_table_query = f"""create table if not exists CSVTable2 (
    {csv_data[0][0]} varchar(25),
    {csv_data[0][1]} varchar(250),
    {csv_data[0][2]} varchar(250),
    {csv_data[0][3]} varchar(250),
    {csv_data[0][4]} varchar(1000)
    );

"""

cursor.execute(create_table_query)
conn.commit()
#insert query
insert_quer = f'insert into CSVTable2 ({csv_data[0][0]},{csv_data[0][1]},{csv_data[0][2]},{csv_data[0][3]},{csv_data[0][4]}) value (%s,%s,%s,%s,%s)'


for i in csv_data[1:]:
    values = (i[0],i[1],i[2],i[3],i[4])
    cursor.execute(insert_quer,values)
    print(values)

conn.commit()


