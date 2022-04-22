import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)

mycursor = mydb.cursor()
def select():
    id=input("Please enter project ID: ")
    if id.isnumeric():
        id=int(id)
    else:
        print("Please Enter Number Only: ")
        exit()
    mycursor.execute("SELECT * FROM projects where id="+str(id))

    myresult = mycursor.fetchall()
    print(myresult)   
    
def insert():
    sql = "INSERT INTO projects (project_name, estimate_amount, contract_amount, contractor, project_detail) VALUES (%s, %s, %s, %s, %s)"
    project_name=input("Enter project name: ")
    estimate_amount=input("Enter estimate_amount: ")
    contract_amount=input("Enter contract_amount: ")
    contractor=input("Enter contractor: ")
    project_detail=input("Enter project_detail: ")
    val = (project_name, estimate_amount, contract_amount, contractor, project_detail)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
def edit():
    id=input("enter the project id you want to edit: ")
    if id.isnumeric():
        id=int(id)
    else:
        print("Please Enter Number Only: ")
        exit()
    mycursor.execute("SELECT * FROM projects where id="+str(id))
    myresult = mycursor.fetchone()
    if myresult == None:
        exit("data not found")
    project_name=input("Enter project name ( old : "+str(myresult[1])+")")
    estimate_amount=input("Enter project name ( old : "+str(myresult[2])+")")
    contract_amoun
    t=input("Enter project name ( old : "+str(myresult[3])+")")
    contractor=input("Enter project name ( old : "+str(myresult[4])+")")
    project_detail=input("Enter project detail ( old : "+str(myresult[6])+")")
    sql = "UPDATE projects SET project_name ='"+str(project_name)+"', estimate_amount="+str(estimate_amount)+", contract_amount="+str(contract_amount)+", contractor='"+str(contractor)+"', project_detail='"+str(project_detail)+"' WHERE id = "+str(id)
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

a=input(" For what purpose you want to use this software? (Press i for insert/ e for edit/ s for search) ")
if a=="i":
    insert()
elif a=="s":
    select()
elif a=="e":
    edit()
else:
    print("invalid function" )
    