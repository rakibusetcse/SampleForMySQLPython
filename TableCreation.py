from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()

sql= "CREATE DATABASE clients"
cursor.execute(sql)