import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host = "localhost",
                                         database = 'test',
                                         user = 'root',
                                         password = 'root')

    mysql_create_table_query = """CREATE TABLE Laptop (
                                Id int(11) NOT NULL,
                                Name varchar(250) NOT NULL,
                                Price float NOT NULL,
                                Purchase_date Date NOT NULL,
                                PRIMARY KEY (Id))"""

    cursor = connection.cursor()

    result = cursor.execute(mysql_create_table_query)

    print("Laptop Table Created Successfully")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
