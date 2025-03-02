import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()


    sqlCommand="""CREATE PROCEDURE uspCategoryUpdate (@ID int)
    AS 
    UPDATE Category SET Rodzaj_kategorii=Rodzaj_kategorii+' - Updated from SP' where id=@ID
    """

    # Create Stored Procedure
    cursor.execute(sqlCommand)
    connection.commit()

    print()

    sqlCommand2="""
    EXEC dbo.uspCategoryUpdate @ID=?;
    """

    # Set the parameter value
    prmID=2

    # Call Stored Procedure
    cursor.execute(sqlCommand2,prmID)
    connection.commit()

    # SELECT Query After Stored Procedure Call - Check table contents
    cursor.execute("SELECT * FROM Category")

    print("[After SP Call...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.ID,row.Rodzaj_kategorii)

    cursor.close()
    connection.close()

except pyodbc.Error as ex:
    print()
    print("Exeption: ",ex)
    print("Closing program....")
    print()
    exit()
print()
