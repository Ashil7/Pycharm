import mysql.connector

testdb=mysql.connector.connect( # database connection
    host='localhost',
    user='root',
    password='',
    database='login'
)

cursor=testdb.cursor() # Create Cursor

def Create():#Function to insert values from user
    query = "INSERT INTO login_info(username,password,phone,Email) VALUES(%s,%s,%s,%s)" #query to insert values
    name = input("Enter username:")
    pwd = input("Enter password:")
    phone = (input("Enter phone:"))
    mail = (input("Enter mail:"))
    val = (name, pwd, phone, mail)
    query1 = "SELECT username,password FROM login_info WHERE username=%s AND password=%s" #query to check whether username and password already exists
    val1 = ( name, pwd)
    cursor.execute(query1, val1)
    result=cursor.fetchall()
    if result:
        print("Username and password already exists")
    else:
        cursor.execute(query, val)
        print("inserted successfully")
        testdb.commit()

def Delete(): # function to delete record
    query="DELETE FROM login_info WHERE username=%s" #query to delete record
    name=input("Enter the username of record to be deleted:")
    val=(name,)
    cursor.execute(query,val)
    print("RECORD DELETED!!!!!")
    testdb.commit()

def Read(): # function to read record
    query="SELECT * FROM login_info" # query to read records
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("*****************************************************************")
        for i in result:
            print(i)
        print("*****************************************************************")

def Update(): # Update records
    while True:
        print("1. Username \n2. Password \n3. Phone \n4. Email \n5. Exit") # menu to choose whether which records to be updated
        c=int(input("Enter Choice:"))
        if c==1:
            name=input("Enter current username:")
            newName=input("Enter new username:")
            query="UPDATE login_info SET username=%s WHERE username=%s"
            val=(newName,name)
            cursor.execute(query,val)
            print("username updated")
        elif c==2:
            password=input("Enter current password:")
            newPassword=input("Enter new password:")
            query="UPDATE login_info SET password=%s WHERE password=%s"
            val=(newPassword,password)
            cursor.execute(query,val)
            print("Password updated")
        elif c==3:
            phone=input("Enter current Phone number:")
            newPhone=input("Enter new Phone number:")
            query="UPDATE login_info SET phone=%s WHERE phone=%s"
            val=(newPhone,phone)
            cursor.execute(query,val)
            print("phone number updated")
        elif c==4:
            mail=input("Enter current Email:")
            newMail=input("Enter new Email:")
            query="UPDATE login_info SET Email=%s WHERE Email=%s"
            val=(newMail,mail)
            cursor.execute(query,val)
            print("Email updated")
        elif c==5:
            break
        else:
            print("invalid choice")
        testdb.commit()

while True:
    print("1. Insert \n2. Delete \n3. Read \n4. Update \n5. Exit")
    c=int(input("Enter Choice: "))
    if c==1:
        Create()
    elif c==2:
        Delete()
    elif c==3:
        Read()
    elif c==4:
        Update()
    elif c==5:
        exit()
    else:
        print("INVALID CHOICE")
