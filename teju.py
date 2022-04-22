import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="teju"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE detail (id int(25), customer_name VARCHAR(255), item_name VARCHAR(255), price VARCHAR(255), transactiondate VARCHAR(255))")

def insertitem ():
    sql = "INSERT INTO item (id, item_name, price) VALUES (%s, %s, %s)"
    id=input("enter id:")
    item_name= input("enter item name: ")
    price= input("enter item price: ")
    val=(id, item_name, price)
    mycursor.execute(sql, val)
    mydb.commit()
def insertcustomer():
    sql = "INSERT INTO customer (customer_name, address, contact_no) VALUES (%s, %s, %s)"
    customer_name= input("enter customer name: ")
    address= input("enter address: ")
    contact_no= input("enter contact_no: ")
    val=(customer_name, address, contact_no)
    mycursor.execute(sql, val)
    mydb.commit()
def insertbilling():
    sql = "INSERT INTO billing (customer_id, item_id) VALUES (%s, %s)"
    customer_name= input("enter customer name: ")
    item_name=input("enter item name customer had eaten: ")
    mycursor.execute("SELECT * FROM customer where customer_name like '%"+str(customer_name)+"%'")
    myresult = mycursor.fetchone()
    customer_id= myresult[0]
    print ("customer id: ", customer_id)
    mycursor.execute("SELECT * FROM item where item_name like '%"+str(item_name)+"%'")
    result=mycursor.fetchone()
    item_id=result[0]
    print ("item id: ", item_id)
    val=(customer_id, item_id,)
    mycursor.execute(sql, val)
    mydb.commit()
#insertbilling()
def printallrecords():
    abc="SELECT customer.customer_name as customername, customer.contact_no as contactnumber, item.item_name as item_eaten, item.price from customer join item join billing on customer.id=billing.customer_id and item.id=billing.item_id"
    mycursor.execute(abc)
    myresult=mycursor.fetchall()
    for i in myresult:
        print(f"{i[0]} {i[1]}  {i[2]}  {i[3]} ")
#printallrecords()
def printdetail():
    customer_name=input("enter the customer name whose detail you want: " )
    '''bc="SELECT customer_name, contact_no, address from customer where customer_name like '%"+str(customer_name)+"%'"
    mycursor.execute(bc)
    result=mycursor.fetchall()
    print (result)'''
    abc="SELECT item_name, price from item where id= (select item_id from billing where customer_id=(SELECT id FROM customer where customer_name like '%"+str(customer_name)+"%'))"
    mycursor.execute(abc)
    myresult=mycursor.fetchall()
    print(myresult)
    '''
    for i in myresult:
        print(f"{i[0]} {i[1]} ")
    total=0
    for i in myresult:
        mycursor.execute("select price from item where id="+str(i[0]))
        price=mycursor.fetchone()
        total=total + int(price[0])
    print (" "+str(customer_name) + " Your total bill is: " +str(total))'''
printdetail()
'''def printbill():
    customer_name=input("enter the customer name whose bill you want: " )
    abc="SELECT item_id, order_date from billing where customer_id=(SELECT id FROM customer where customer_name like '%"+str(customer_name)+"%')"
    mycursor.execute(abc)
    myresult=mycursor.fetchall()
    total=0
    for i in myresult:
        mycursor.execute("select price from item where id="+str(i[0]))
        price=mycursor.fetchone()
        total=total + int(price[0])
    print (" "+str(customer_name) + " Your total bill is: " +str(total))
#printbill()
  '''