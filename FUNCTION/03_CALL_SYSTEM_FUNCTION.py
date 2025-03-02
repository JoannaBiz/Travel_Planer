import pyodbc
print()
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()

    cursor.execute("SELECT HOST_NAME () AS HostName")
    print("Host_Name - Results....")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("HostName: ",row.HostName)
    print()

    cursor.execute("SELECT DB_NAME () AS CurrentDBName")
    print("DB_NAME - Results....")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("Current Database Name: ",row.CurrentDBName)
    print()

    prmIsNumeric ="a20"
    cursor.execute("SELECT ISNUMERIC (?) AS IsNumericValue",prmIsNumeric)
    print("is numeric - Results....")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("Checking if : ",prmIsNumeric,"is numeric. Check Results (0- False, 1 - True):",row.IsNumericValue)
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
