import sqlite3

conn = sqlite3.connect('test8June') #test is a local file, it will get created if not present
print("connection object = ", conn) #connection object =  <sqlite3.Connection object at 0x000001524B162540>

cursor = conn.cursor()

print("cursor = ", cursor) #cursor =  <sqlite3.Cursor object at 0x000001E8FCF4CC40>

# creating a table in the 'test' database
# cursor.execute("create table studentdata1(name text, count integet)")

#inserting into 'studentdata1' table
cursor.execute("insert into studentdata1(name, count) values (?, ?)", ("Saket", 22))

# saving the output from the database in the result object
result = cursor.execute("select * from studentdata1")
print("Table Contents:\n", result.fetchall())

# commit the changes to the database
conn.commit()

# close the connection at the end
conn.close()