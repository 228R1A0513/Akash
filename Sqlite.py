import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
#cur.execute("create table student1(name varchar(50),roll_no varchar(50),password varchar(50))")
#cur.execute('insert into student1 values("Akash","513","A")')
#cur.execute('insert into student1 values("Jeeva","532","B")')
#cur.execute('insert into student1 values("Hari","511","C")')
cur.execute('update student1 set name="Hari" where roll_no="532" ')
x=cur.execute('select * from student1')
print(x.fetchall())
con.commit()
print(x)