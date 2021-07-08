from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()
try:

    sql="UPDATE employee_info SET dept = 'Management' WHERE dept = 'Officer'"

    cursor.execute(sql)
    myresult="SELECT * FROM employee.employee_info"

    cursor.execute(myresult)
    result = cursor.fetchall()

    for x in result:
        print(x)
except Exception as e:
    print(e)

cursor.close()
myCursor.close()

