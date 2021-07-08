from connectivity import DBconnect

mydb= DBconnect()

myCursor = mydb.db_connector()
cursor = myCursor.cursor()

try:

    sql= "INSERT INTO employee_info(id,name,dept) VALUES(%s,%s,%s)"
    sql1= "INSERT INTO employee_info(id,name,dept) VALUES(%s,%s,%s)"
    sql2= "INSERT INTO employee_info(id,name,dept) VALUES(%s,%s,%s)"
    sql3= "INSERT INTO employee_info(id,name,dept) VALUES(%s,%s,%s)"
    val= (3, "Sumaiya Islam", "Student")
    val1= (4, "Abu Rayhan", "Officer")
    val2= (5, "Saiful Islam", "Technician")
    val3= (6, "Fazle Rafi", "Engineer")
    # inputValue= cursor.execute(sql,val)
    # print(inputValue)
    cursor.execute(sql, val)
    cursor.execute(sql1, val1)
    cursor.execute(sql2, val2)
    cursor.execute(sql3, val3)
    myCursor.commit()
    print(cursor.rowcount, "record inserted.")
    cursor.close()
    myCursor.close()
except Exception as e:
    print(e)


