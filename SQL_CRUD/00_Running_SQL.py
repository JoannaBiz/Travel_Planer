import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()
 
    cursor.execute("SELECT @@VERSION as version")
    print("[Query 1 - Version: @@VERSION - Results...]")

    while 1:
        row = cursor.fetchone()
        if not row:
                break
        print(row.version)
        
     # Query 2 - System Global Variable: @@SERVERNAME
    cursor.execute("SELECT @@SERVERNAME as serverName")

    print("[Query 2 - System Global Variable: @@SERVERNAME - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.serverName)

    print()

    # Query 3 - Dynamic Management Views (DMVs): sys.dm_os_wait_stats 
    cursor.execute("SELECT TOP 10 wait_type, wait_time_ms FROM sys.dm_os_wait_stats where wait_time_ms>5 ORDER BY 2 DESC")

    print("[Query 3 - Dynamic Management Views (DMVs): sys.dm_os_wait_stats - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.wait_type,row.wait_time_ms)

    cursor.close()
    connection.close()
except pyodbc.Error as ex:
    print()
    print("Exeption: ",ex)
    print("Closing program....")
    print()
    exit()
print()
