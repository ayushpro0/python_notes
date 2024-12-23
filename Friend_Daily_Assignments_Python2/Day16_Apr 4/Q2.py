'''2.	Write Python script for database connectivity using mysql.connector module.
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
Write different methods for all these functionalities.
'''
import mysql.connector
from mysql.connector import Error
def insertVariblesIntoTable(id, name, ph_no, email, pswd):
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO users12 (Id, Name, Ph_no, email, pswd) 
                                VALUES (%s, %s, %s, %s, %s) """

        recordTuple = (id, name, ph_no, email, pswd)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')
    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) PRIMARY KEY,
                             Name varchar(250),
                             Ph_no int(11),
                             email varchar(20),
                             pswd varchar(20)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        #cursor.close()
        #connection.close()
        #print("MySQL connection is closed")
        pass



insertVariblesIntoTable(101, 'Ravi Verma','9923849335','ravi_verma@gmail.com','tough@password!!')
insertVariblesIntoTable(102,'Riya Das','9923849907','riya_das@gmail.com','triya@password!!')

cursor = connection.cursor()
cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)
  
cursor.close()
connection.close()
