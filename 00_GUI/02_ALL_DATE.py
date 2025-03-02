from tkinter import *
from tkinter import ttk  # Nowoczesna tabela Treeview
import pyodbc

# Tworzenie głównego okna aplikacji
root = Tk()
root.geometry('800x400')
root.title('Tabela kosztów')

# **Dodanie tabeli Treeview**
tree = ttk.Treeview(root)
tree["columns"] = ("ID", "Category", "Name_Cost", "Plan_Cost", "Real_cost", "Paid", "Date", "Who_paid", "Who_need_return_money", "Is_returned")

# **Definiowanie nagłówków kolumn**
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=100)  # Szerokość kolumny

tree.pack(expand=True, fill='both')

def load_costs():  
    try:
        # Połączenie z SQL Server
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER=HOMEPC\SQL2K24;'
                                    'DATABASE=Planer_travel;'
                                    'Trusted_Connection=yes;')
        cursor = connection.cursor()
        
        # Pobranie wszystkich rekordów z tabeli COST
        cursor.execute("SELECT * FROM COST")
        rows = cursor.fetchall()

        # Usunięcie poprzednich danych (jeśli istnieją)
        for item in tree.get_children():
            tree.delete(item)

        # Dodanie nowych danych do tabeli
        for row in rows:
            tree.insert("", "end", values=row)

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception:", ex)
        cursor.close()
        connection.close()
        exit()

# Przycisk do pobrania danych
btnLoad = Button(root, text="Pobierz dane", command=load_costs)
btnLoad.pack(pady=10)

# Uruchomienie głównej pętli GUI
root.mainloop()