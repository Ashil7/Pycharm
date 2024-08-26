import mysql.connector

testdb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='login'
)

cursor = testdb.cursor()
cursor.execute("CREATE TABLE login_info(userid INT PRIMARY KEY AUTO_INCREMENT, username varchar(30) UNIQUE, password varchar(30),phone INT(10), Email varchar(50))")

