import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()
    print()

    cursor.execute("SELECT * FROM COST")
    while 1:
        row = cursor.fetchone()
        if not row:
                break
        print(row.ID,row.Category,row.Name_Cost,row.Plan_Cost)

    cursor.execute("SELECT COUNT(*) AS COST FROM [Planer_Travel].[dbo].[COST]")
    print()
    print("Aggregation by COUNT - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("Total Records: ", row.COST)

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
