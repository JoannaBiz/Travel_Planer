import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()
    print()
    print("Successfully connected to SQL Server")
    print()
    cursor.close()
    connection.close()
except pyodbc.Error as ex:
    print()
    print("Exeption: ",ex)
    print("Closing program....")
    print()
    exit()
print()
