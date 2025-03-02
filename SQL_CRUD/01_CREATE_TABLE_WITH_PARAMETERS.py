import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()

    cursor.execute("SELECT name FROM sys.tables")
    print("[Before Create ...]")
    while 1:
        row = cursor.fetchone()
        if not row:
                break
        print(row.name)

    print()
    prmName_Table = "Category"
    prmID="ID"
    prmColumn1="Rodzaj_kategorii"
   

    print("[Add new Table...]")
    cursor.execute(f"""
                   BEGIN TRANSACTION 
                   SET QUOTED_IDENTIFIER ON 
                   SET ARITHABORT ON 
                   SET NUMERIC_ROUNDABORT OFF 
                   SET CONCAT_NULL_YIELDS_NULL ON 
                   SET ANSI_NULLS ON 
                   SET ANSI_PADDING ON 
                   SET ANSI_WARNINGS ON COMMIT
                BEGIN TRANSACTION
                
                CREATE TABLE {prmName_Table}
                    (
                    {prmID} int NOT NULL,
                    {prmColumn1} varchar(MAX) NOT NULL,
                    
                    )  ON [PRIMARY]
                    TEXTIMAGE_ON [PRIMARY]
                
                ALTER TABLE dbo.{prmName_Table} ADD CONSTRAINT
                    PK_{prmID} PRIMARY KEY CLUSTERED 
                    (
                    ID
	                ) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

                
                ALTER TABLE dbo.{prmName_Table} SET (LOCK_ESCALATION = TABLE)
            
                COMMIT""")
    connection.commit()
    print("Done.")
   

    print()
    cursor.execute("SELECT name FROM sys.tables")
    print("[After Create ...]")
    while 1:
        row = cursor.fetchone()
        if not row:
                break
        print(row.name)

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
