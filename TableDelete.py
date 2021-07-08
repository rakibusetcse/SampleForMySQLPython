from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()

sql = "DROP TABLE employee_info"

cursor.execute(sql)