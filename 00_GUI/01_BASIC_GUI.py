# Import modules
from tkinter import *
import pyodbc

# Variable initialization
SQLServerVer = "Not Available"

# Set the main GUI window properties
root = Tk()
root.geometry('600x400')
root.title('Sample Python GUI App')

# Define label
lblHelloWorld = Label(root, text =str(SQLServerVer),fg='red')

def COST (): 

    # Exception Handling
    try:

        # Trusted Connection to Named Instance
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEPC\SQL2K24;DATABASE=Planer_travel;Trusted_Connection=yes;')

        cursor=connection.cursor()

        # Retrieve  info
        cursor.execute("SELECT * FROM COST as COST")

        while 1:
            row = cursor.fetchone()
            if not row:
                break
            CostINFO=(row.ID,row.Category,row.Name_Cost,row.Plan_Cost, row.Real_cost, row.Paid, row.Date, row.Who_paid, row.Who_need_return_money, row.Is_returned)

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print()
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()

    # Set the label value
    lblHelloWorld.config(text = str(CostINFO))
    lblHelloWorld.pack()
  
# Create "Retrieve SQL Server Version" button
btnCostInfo = Button(root,command=COST, text = 'All cost in the table COST')
btnCostInfo.pack(side = TOP, pady = 100)

# Display the GUI window
root.mainloop()