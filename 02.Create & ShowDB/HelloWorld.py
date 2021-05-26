import mysql.connector

dbobj = mysql.connector.connect
  host="localhost",
  user="sername",
  password="password"
)

command_obj = dbobj.cursor()

command_obj.execute("CREATE DATABASE NewDB")

command_obj.execute("SHOW DATABASES")

for i in command_obj:
  print(i) 
