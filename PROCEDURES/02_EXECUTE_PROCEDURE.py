import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()

    sqlCommand="""
    DECLARE @Plan_cost nvarchar(max);
    EXEC dbo.Cost_Details @ID=?, @Plan_cost = @Plan_cost OUTPUT;
    """

    prmID=1

    # Call the Stored Procedure
    cursor.execute(sqlCommand,prmID)

    print("[Stored Procedure Call Results...]")
    rows=cursor.fetchall()

    # Display the results
    while rows:
        print(rows)
        if cursor.nextset():
            rows =cursor.fetchall()
        else:
            rows = None

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
