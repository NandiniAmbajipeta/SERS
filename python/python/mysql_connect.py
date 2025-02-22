import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Srnm@111",
	database="AmbulanceAlertingSystem"
)
mycursor = mydb.cursor()
sql="INSERT INTO user(name,Email_Id,proffession) VALUES('Hari','ex@example.com','dtr')"
# sql="INSERT INTO user(name,Email_Id,proffession) VALUES('Nandini','ambajipetanandini@gmail.com','student')"
mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record inserted.")