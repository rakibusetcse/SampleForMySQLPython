from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()

sql= "CREATE TABLE employee_info(id int auto_increment primary key, name varchar(255), dept varchar(255))"

try:
    cursor.execute(sql)
    if cursor>0:
        print("Table Created")
    else:
        print("Table not created")
except Exception as e:
    print(e)