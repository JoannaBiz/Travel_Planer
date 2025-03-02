import pyodbc
print()
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()

    sqlCommand =(""" 
    SELECT dbo.uFnGetCategory(?) AS Category
    """)
    prmID =1

    cursor.execute(sqlCommand,prmID)

    print("User - defined Function call reuslt....")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("Category for ID",prmID,"-",row.Category)
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
