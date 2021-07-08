from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()

cursor.execute("SHOW DATABASES")

for databases in cursor:
  print(databases)