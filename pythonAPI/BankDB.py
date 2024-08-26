import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bank'
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE bank_info(accno int(30) primary key auto_increment,uname varchar(20) unique, fname varchar(20),lname varchar(20),balance decimal(15,2),password varchar(10))")
cursor.execute("ALTER TABLE bank_info AUTO_INCREMENT = 11111111")