import mysql.connector

class DBconnect:
  def __init__(self,host="localhost",user="root",password="",database="employee"):
    self.__host = host
    self.__user = user
    self.__password = password
    self.__database= database

  def db_connector(self):
    db_conn= mysql.connector.connect(
      host=self.__host,
      user = self.__user,
      password = self.__password,
      database= self.__database
    )
    return db_conn


