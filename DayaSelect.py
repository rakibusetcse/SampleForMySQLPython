from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()
try:

    #sql="SELECT * FROM employee.employee_info"
    #sql="SELECT * FROM employee_info WHERE dept ='Engineer'"
    #sql = "SELECT * FROM employee_info ORDER BY name"
    sql= "SELECT * FROM employee_info LIMIT 3"

    cursor.execute(sql)

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
except Exception as e:
    print(e)

cursor.close()
myCursor.close()

