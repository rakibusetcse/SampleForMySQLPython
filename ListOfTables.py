from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()

cursor.execute("SHOW TABLES")

for databases in cursor:
  print(databases)