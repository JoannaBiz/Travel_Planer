from tkinter import *
from tkinter import ttk  
import pyodbc

# **Tworzenie głównego okna aplikacji**
root = Tk()
root.geometry('1000x600')
root.title('Planowanie Podróży')

# **Nowoczesna paleta kolorów**
bg_color = "#F7F1E5"  # Delikatny kremowy
btn_color = "#FF6969"  # Stylowe odcienie czerwieni
btn_hover = "#FF4141"  # Intensywniejszy czerwony na hover
text_color = "#333333"  # Ciemnoszary tekst
table_bg = "#FFFFFF"  # Tło tabeli
table_header = "#FFD700"  # Złote nagłówki

root.configure(bg=bg_color)

# **Nagłówek aplikacji**
header_label = Label(root, text="Witamy w planowaniu podróży", 
                     font=("Helvetica", 24, "bold"), fg=text_color, bg=bg_color)
header_label.pack(pady=50)

# **Ramka na przyciski**
btn_frame = Frame(root, bg=bg_color)
btn_frame.pack(pady=10)

# **Tabelka Treeview**
tree_frame = Frame(root, bg=bg_color)
tree_frame.pack(expand=True, fill='both')

tree = ttk.Treeview(tree_frame, style="mystyle.Treeview")

# **Własne nagłówki kolumn**
custom_columns = {
    "ID": "ID",
    "Category": "Kategoria",
    "Name_Cost": "Nazwa wydatku",
    "Plan_Cost": "Planowany koszt",
    "Real_cost": "Rzeczywisty koszt",
    "Paid": "Opłacone",
    "Date": "Data",
    "Who_paid": "Kto zapłacił",
    "Who_need_return_money": "Kto zwraca pieniądze",
    "Is_returned": "Zwrot dokonany"
}

tree["columns"] = list(custom_columns.values())

# **Definiowanie nagłówków kolumn**
for col in tree["columns"]:
    tree.heading(col, text=col, anchor="center")
    tree.column(col, anchor="center", width=120)  

# **Nowoczesny styl tabeli**
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Arial", 12), background=table_bg, fieldbackground=table_bg)
style.configure("mystyle.Treeview.Heading", font=("Arial", 13, "bold"), background=table_header)

# **Funkcja czyszcząca ekran**
def clear_screen():
    for item in tree.get_children():
        tree.delete(item)
    tree.pack_forget()
    header_label.config(text="Witamy w planowaniu podróży")

# **Funkcja pobierająca koszty**
def load_costs():  
    clear_screen()
    try:
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER=HOMEPC\SQL2K24;'
                                    'DATABASE=Planer_travel;'
                                    'Trusted_Connection=yes;')
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM COST")
        rows = cursor.fetchall()

        for row in rows:
            row_values = [value if value is not None else "-" for value in row]  # Zamiana None na "-"
            tree.insert("", "end", values=row_values)

        cursor.close()
        connection.close()

        header_label.config(text="Lista kosztów")
        tree.pack(expand=True, fill='both')  

    except pyodbc.Error as ex:
        print("Exception:", ex)

# **Funkcja pobierająca wersję SQL Server**
def show_sql_version():
    clear_screen()
    try:
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER=HOMEPC\SQL2K24;'
                                    'DATABASE=Planer_travel;'
                                    'Trusted_Connection=yes;')
        cursor = connection.cursor()

        cursor.execute("SELECT @@VERSION as version")
        row = cursor.fetchone()

        if row:
            header_label.config(text=f"Wersja SQL Server: {row.version}")

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception:", ex)

# **Tworzenie przycisków**
def create_button(parent, text, command):
    btn = Button(parent, text=text, command=command, 
                 bg=btn_color, fg="white", font=("Arial", 12, "bold"), 
                 padx=20, pady=10, relief="flat", borderwidth=2)
    btn.bind("<Enter>", lambda e: btn.config(bg=btn_hover))
    btn.bind("<Leave>", lambda e: btn.config(bg=btn_color))
    return btn

btnLoad = create_button(btn_frame, "Pobierz dane kosztów", load_costs)
btnLoad.grid(row=0, column=0, padx=20)

btnSQLVersion = create_button(btn_frame, "Pokaż wersję SQL Server", show_sql_version)
btnSQLVersion.grid(row=0, column=1, padx=20)

btnClear = create_button(btn_frame, "Anuluj", clear_screen)
btnClear.grid(row=0, column=2, padx=20)

# Uruchomienie głównej pętli GUI
root.mainloop()
