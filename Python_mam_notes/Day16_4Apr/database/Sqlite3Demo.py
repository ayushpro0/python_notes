import sqlite3 
conn = sqlite3.connect('test')#test is a local file
cursor = conn.cursor()
print ("cursor = ",cursor)
#cursor.execute("create table studentdata4Apr(name text, count integer)")
cursor.execute("insert into studentdata4Apr (name, count) values (?, ?)",("ABC", 50))
result = cursor.execute("select * from  studentdata4Apr")
print(result.fetchall())
conn.commit()
conn.close()
