import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()
    prmID=2

    cursor.execute("SELECT * FROM COST WHERE ID=?",prmID)
    print("[Query Results ...]")
    while 1:
        row = cursor.fetchone()
        if not row:
                break
        print(row.ID,row.Category,row.Name_Cost,row.Plan_Cost)

    cursor.close()
    connection.close()
except pyodbc.Error as ex:
    print()
    print("Exeption: ",ex)
    print("Closing program....")
    print()
    exit()
print()
