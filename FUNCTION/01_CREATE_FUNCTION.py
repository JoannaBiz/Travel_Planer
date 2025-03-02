import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()

    sqlCommand =(""" 
    CREATE FUNCTION uFnGetCategory(@ID int)
    RETURNS VARCHAR(50)
    AS
    BEGIN
    DECLARE @catName VARCHAR(50)
    SET @catName =(SELECT Category FROM COST WHERE ID=@ID)
    RETURN @catName
    END;

    """)

    cursor.execute(sqlCommand)
    connection.commit()

    print("Function created correctly")

    cursor.close()
    connection.close()
except pyodbc.Error as ex:
    print()
    print("Exeption: ",ex)
    print("Closing program....")
    print()
    exit()
print()
