import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="tejucafe"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE items (id INT(25), item_name VARCHAR(255), price INT(25,2), food_type VARCHAR(255))")