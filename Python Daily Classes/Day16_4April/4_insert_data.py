import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host = "localhost",
                                         database = 'test',
                                         user = 'root',
                                         password = 'root')

    mysql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
                                VALUES (20, 'Asus TUF F15', 50000, '2022-08-14')"""

    cursor = connection.cursor()

    cursor.execute(mysql_insert_query)

    connection.commit()

    print(cursor.rowcount, "Record inserted successfully into Laptop table")

    cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
