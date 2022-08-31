import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sistema_bancario',
                                         user='root',
                                         password='')

    sql_select_Query = "select * from cliente"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Apellido  = ", row[2])
        print("Telefono  = ", row[4])
        print("mail  = ", row[5])
        print("Usuario  = ", row[6])
        print("Password  = ", row[7],"\n")
        


except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")