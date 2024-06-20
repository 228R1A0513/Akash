import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AKASHSUNNY143@",
    database="mydb"
)

mycurs = mydb.cursor()
#mycurs.execute("CREATE TABLE users (name VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")
mycurs.execute("SHOW TABLES")
sql="insert into users(name,email,password) values(%s,%s,%s)"
val=("Akash","akash613@gmail.com","Akash@123")
#result=mycurs.execute(("select * from users"))
#mycurs.execute(sql,val)
print()

for table in mycurs:
    print(table)