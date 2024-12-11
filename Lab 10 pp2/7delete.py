#Implement deleting data from tables by username of phone
import psycopg2

conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='simbasimba.18',
	host='localhost',
	
)
cursor = conn.cursor()
conn.autocommit = True



#looking with the first and last name
first_old = str(input("Nanny"))
last_old = str(input("Kill"))

sql = f"select * from phonebook where first_name =\'{first_old}\' and last_name = \'{last_old}\' "
cursor.execute(sql)
info = cursor.fetchall()


if len(info) > 0:
    sql_update = f"Delete from phonebook where  first_name =\'{first_old}\' and last_name = \'{last_old}\'; " 
    cursor.execute(sql_update)
    print("successfully !!")
else:
    print("this people name is not in phonebook")


conn.commit()

conn.close()