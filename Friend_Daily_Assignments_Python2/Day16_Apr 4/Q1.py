'''1.	Write Python script for database connectivity using sqlite3 module.
Create a table from the script, please drop it if it already exists.
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)

Accept some values for varaibles-
name1 ,phone1 ,email1, password1
e.g.
name1 = 'Ravi Verma'
phone1 = '9923849335'
email1 = 'ravi_verma@gmail.com'
password1 = 'tough@password!!'

Insert these values in table users.
Read the data back and display
Accept name from user, display the details for that user if it exists in table users.
'''
import sqlite3
con = sqlite3.connect("user1.db")
cur = con.cursor()

#Drop the table if already exists
cur.execute("DROP TABLE IF EXISTS USERS")
#creat a table
table = """ CREATE TABLE USERS (
            id INTEGER PRIMARY KEY, 
            name VARCHAR(20),
            phone VARCHAR(20), 
            email VARCHAR(20) unique, 
            password VARCHAR(20)
        ); """
 
cur.execute(table)
#add values in the table
data = ({'id1': 101, 'name1': 'Ravi Verma','ph1': '9923849335','email1': 'ravi_verma@gmail.com','pswd1':'tough@password!!'},
{'id1': 102, 'name1': 'Riya Das','ph1': '9923843450','email1': 'riya_das@gmail.com','pswd1':'triya@password!!'})


#cur.execute("INSERT INTO USERS(id, name, phone, email, password) VALUES(?, ?, ?, ?, ?)",
        #(101,'Ravi Verma','9923849335','ravi_verma@gmail.com','tough@password!!'))

#cur.execute("INSERT INTO USERS(id, name, phone, email, password) VALUES(?, ?, ?, ?, ?)",
        #(102,'Riya Das','9923849907','riya_das@gmail.com','triya@password!!'))

 
cur.executemany("INSERT INTO USERS VALUES(:id1, :name1, :ph1, :email1, :pswd1)", data)
res = cur.execute("SELECT * FROM USERS")
print(res.fetchall())


user_name = input("Enter name: ")
li = []
li.append(user_name)
tup = tuple((li))

cur.execute("SELECT * FROM USERS WHERE name=?", tup)
print(cur.fetchall())
con.commit()
con.close()