from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()

sql = "DELETE FROM employee_info WHERE name = 'Fazle Rafi'"
cursor.execute(sql)

myCursor.commit()
print(cursor.rowcount, "record(s) deleted")