import pyodbc
try:
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=SampleDB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()

    cursor.execute("SELECT * FROM COST")
    print("[Before Insert ...]")
    while 1:
        row = cursor.fetchone()
        if not row:
                break
        print(row.ID,row.Category,row.Name_Cost,row.Plan_Cost)

    print()
    prmID=7
    prmCategory="Transport"
    prmName_Cost="Metro"
    prmPlan_Cost=1500

    print("[Inserting Record to Table...]")
    cursor.execute("INSERT INTO [COST]([ID],[Category],[Name_Cost],[Plan_Cost]) VALUES (?,?,?,?)",(prmID,prmCategory,prmName_Cost,prmPlan_Cost))
    connection.commit()
    print("Done.")
   

    print()
    cursor.execute("SELECT * FROM COST")
    print("[After Insert ...]")
    while 1:
        row = cursor.fetchone()
        if not row:
                break
        print(row.ID,row.Category,row.Name_Cost,row.Plan_Cost)

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
