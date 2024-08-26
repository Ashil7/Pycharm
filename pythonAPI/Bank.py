import mysql.connector

conn=mysql.connector.connect( #database connection
    host='localhost',
    user='root',
    password='',
    database='bank'
)

cursor = conn.cursor() #cursor creation
cursor.execute("ALTER TABLE bank_info AUTO_INCREMENT = 11111111") #setting initial accno.
def register(): #function to register
    query = "INSERT INTO bank_info(uname,fname,lname,password)VALUES(%s,%s,%s,%s)"
    while True: #checking whether username already exists or not
        name = input("Enter username:")
        query1 = "SELECT uname from bank_info WHERE uname=%s"
        val1 = (name,)
        cursor.execute(query1,val1)
        result = cursor.fetchall()
        if result:
            print("username already exists")
        else:
            break
    fname = input("Enter First name:")
    lname = input("Enter Last name:")
    pwd = input("Enter password:")
    val = (name, fname, lname, pwd)
    cursor.execute(query, val)
    print("Account created successfully!!")
    conn.commit()
def log(): #function to log in, withdraw, deposit and view details
    while True: #validating username and password
        name=input("Enter your username:")
        pwd=input("Enter your password:")
        query="SELECT uname,password FROM bank_info WHERE uname=%s AND password=%s"
        val=(name,pwd)
        cursor.execute(query,val)
        result=cursor.fetchall()
        if result:
            break
        else:
            print("username or password incorrect!!")
    while True:
        print("1. Deposit \n2. Withdraw \n3. View account details \n4. Exit")
        c=int(input("enter choice:"))
        if c==1: #deposit money
            n=int(input("Enter Amount:"))
            query1="UPDATE bank_info SET balance=balance+%s WHERE uname=%s"
            val1=(n,name)
            cursor.execute(query1,val1)
            print("Money deposited successfully!!")
            conn.commit()
        elif c==2: #withdraw
            num=int(input("Enter Amount:"))
            q2="SELECT balance FROM bank_info WHERE uname=%s"
            val2=(name,)
            cursor.execute(q2,val2)
            bal=cursor.fetchone()
            dif=bal[0]-num
            if dif <1000: #checking for min balance
                print("Balance:",bal[0])
                print("No minimum balance\nA minimum balance of 1000 should be kept!!")
            else:
                q3="UPDATE bank_info SET balance=balance-%s WHERE uname=%s"
                val3=(num,name)
                cursor.execute(q3,val3)
                print("Money withdrawn successfully!!")
                conn.commit()
        elif c==3:
            q4="SELECT * FROM bank_info WHERE uname=%s"
            val4=(name,)
            cursor.execute(q4,val4)
            result=cursor.fetchall()
            print("*******************************************")
            print("Account number :", result[0][0])
            print("Username :", result[0][1])
            print("First name :", result[0][2])
            print("Last name :",result[0][3])
            print("Balance :", result[0][4])
            print("*******************************************")
        elif c==4:
            break
        else:
            print("invalid choice")

while True:
    print("1. Register \n2. Login \n3. Exit")
    c=int(input("Choice:"))
    if c==1:
        register()
    elif c==2:
        log()
    elif c==3:
        exit()
    else:
        print("Invalid choice")