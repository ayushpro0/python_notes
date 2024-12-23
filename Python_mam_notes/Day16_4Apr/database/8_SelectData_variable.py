import mysql.connector
from mysql.connector import Error


def getLaptopDetail(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')

        cursor = connection.cursor(buffered=True)

        sql_select_query = """select * from laptop where id = %s"""

        cursor.execute(sql_select_query, (id,))

        record = cursor.fetchall()

        print("record : ", record)

        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Join Date = ", row[2])
            print("Salary  = ", row[3], "\n")

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed\n-------------------------------------\n")

id1 = 10
id2 = 20
getLaptopDetail(id1)
getLaptopDetail(id2)
