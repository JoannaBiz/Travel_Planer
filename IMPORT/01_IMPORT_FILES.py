
# Import modules
import pyodbc
import csv

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # Create the table COSTFROMCSV
    createTableTSQL="""CREATE TABLE [dbo].[COSTFROMCSV](
	[ID] [int] NOT NULL,
	[Category] [varchar](max) NULL,
    [NameCost] [varchar](max) NULL,
	[Plan_Cost] [money] NULL,
	[Real_cost] [money] NULL,
    [Paid] [bit] NULL,
    [Date] [datetime2] NULL,
    [Who_paid] [varchar](50) NULL,
    [Who_need_return_money] [varchar](50) NULL,
    [IsReturned] [varchar](50) NULL,
    )"""
    
    cursor.execute(createTableTSQL)
    connection.commit()

    # SELECT Query Before INSERT
    cursor.execute("SELECT * FROM COSTFROMCSV")

    print("[Before INSERT...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.ID,row.Category,row.NameCost,row.Plan_Cost, row.Real_cost, row.Paid, row.Date, row.Who_paid, row.Who_need_return_money, row.IsReturned)

    print()

    #Read CSV File and Insert Rows to SQL Server Table
    print("[Reading CSV File and Insert Rows to SQL Server Table]")    
    with open(r"C:\Users\User\Desktop\Travel_Planer\IMPORT_FILES\cost.CSV", newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvReader:
          #  prmID=row[0]
           # prmCategory=row[1]
            #prmNameCost=row[2]
            #prmPlan_Cost=row[3]
            #prmReal_cost=row[4]
            #prmPaid=row[5]
            #prmDate=row[6]
            #prmWho_paid=row[7]
            #prmWho_need_return_money=row[8]
            #prmIsReturnedt=row[9]
            # Konwersja danych
            prmID = int(row[0])
            prmCategory = row[1]
            prmNameCost = row[2]
            prmPlan_Cost = float(row[3].replace(',', '.')) if row[3] and row[3] != 'NULL' else None
            prmReal_cost = float(row[4].replace(',', '.')) if row[4] and row[4] != 'NULL' else None
            prmPaid = int(row[5]) if row[5] and row[5] != 'NULL' else None  # `bit` wymaga liczby 0 lub 1
            prmDate = row[6] if row[6] and row[6] != 'NULL' else None
            prmWho_paid = row[7] if row[7] and row[7] != 'NULL' else None
            prmWho_need_return_money = row[8] if row[8] and row[8] != 'NULL' else None
            prmIsReturned = int(row[9]) if len(row) > 9 and row[9] and row[9] != 'NULL' else None  # Sprawdzenie, czy kolumna istnieje


            print('Inserting record: ',', '.join(row))
            cursor.execute("INSERT INTO [COSTFROMCSV] ([ID],[Category],[NameCost],[Plan_Cost], [Real_cost], [Paid], [Date], [Who_paid], [Who_need_return_money], [IsReturned]) VALUES (?,?,?,?,?,?,?,?,?,?)",(prmID,prmCategory,prmNameCost,prmPlan_Cost,prmReal_cost,prmPaid,prmDate,prmWho_paid,prmWho_need_return_money,prmIsReturned))

            connection.commit()
            
    print()

    # SELECT Query After INSERT
    cursor.execute("SELECT * FROM COSTFROMCSV")

    print("[After INSERT...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.ID,row.Category,row.NameCost,row.Plan_Cost, row.Real_cost, row.Paid, row.Date, row.Who_paid, row.Who_need_return_money, row.IsReturned)


    cursor.close()
    connection.close()

except pyodbc.Error as ex:
    print("Exception: ",ex)
    cursor.close()
    connection.close()
    print("Closing program...")
    print()
    exit()

print()