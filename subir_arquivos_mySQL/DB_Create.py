import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxxxx"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE dbtestes")
