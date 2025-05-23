import sqlite3
con = sqlite3.connect("my_test_db1")

cursor = con.cursor()

# cursor.execute('''
# create table if not exists stud_info(
#     id integer primary key,
#     name text not null,
#     marks integer not null)
#     ''')

# cursor.execute("insert into student_info (id,name,marks) values (?,?,?)",(1,'Adarsh',87))
# cursor.execute("insert into student_info (id,name,marks) values (?,?,?)",(2,'Rakesh',67))
#
# con.commit()
#
# cursor.execute("select * from student_info")
#
# rows = cursor.fetchall()
#
# print(rows)
#
# con.close()