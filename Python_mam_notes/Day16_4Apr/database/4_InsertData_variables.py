import mysql.connector
from mysql.connector import Error

def insertVariblesIntoTable(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='root')
        
        cursor = connection.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        recordTuple = (id, name, price, purchase_date) # upar wale arguments ko tuple bana diya

        cursor.execute(mySql_insert_query, recordTuple) # query aur uske sath banaye huye tuple dono ko sath me execute kar diya

        connection.commit()

        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertVariblesIntoTable(2, 'Area 51M', 6999, '2019-04-14')

insertVariblesIntoTable(3, 'MacBook Pro', 2499, '2019-06-20')




