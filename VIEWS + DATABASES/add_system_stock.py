import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Database setup
conn = sqlite3.connect('stock_database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                inner_qty INTEGER NOT NULL,
                loose_qty INTEGER NOT NULL,
                outer_qty INTEGER NOT NULL
            )''')
conn.commit()

# List of common medications
medications = ["Paracetamol", "Ibuprofen", "Aspirin", "Amoxicillin", "Metformin"]

# Function to add stock to the database
def add_stock():
    item_name = combo_medication.get()
    inner_qty = entry_inner_qty.get()
    loose_qty = entry_loose_qty.get()
    outer_qty = entry_outer_qty.get()

    if not item_name or not inner_qty or not loose_qty or not outer_qty:
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        inner_qty = int(inner_qty)
        loose_qty = int(loose_qty)
        outer_qty = int(outer_qty)
    except ValueError:
        messagebox.showerror("Error", "Quantities must be numbers")
        return

    try:
        c.execute("INSERT INTO stock (item_name, inner_qty, loose_qty, outer_qty) VALUES (?, ?, ?, ?)",
                  (item_name, inner_qty, loose_qty, outer_qty))
        conn.commit()
        messagebox.showinfo("Success", "Stock added successfully")
        
        # Clear entries
        combo_medication.set(medications[0])
        entry_inner_qty.delete(0, tk.END)
        entry_loose_qty.delete(0, tk.END)
        entry_outer_qty.delete(0, tk.END)
    except sqlite3.Error:
        messagebox.showerror("Error", "Failed to add stock")

def mv_open():
    root.destroy()
    import main_view

# Tkinter setup
root = tk.Tk()
root.title("Add Stock")
root.geometry("1400x720")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Create styles
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel',
                background='#f0f0f0',
                font=('Helvetica', 12))
style.configure('TButton',
                padding=10,
                font=('Helvetica', 12))
style.configure('Header.TLabel',
                font=('Helvetica', 32, 'bold'))

# Main container
main_frame = ttk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Title
title_label = ttk.Label(root,
                       text="Add Stock",
                       style='Header.TLabel')
title_label.pack(pady=50)

# Form frame
form_frame = ttk.Frame(main_frame)
form_frame.pack(padx=20, pady=20)

# Item Name
ttk.Label(form_frame, text="Item Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
combo_medication = ttk.Combobox(form_frame, values=medications, state='readonly', width=30)
combo_medication.set(medications[0])
combo_medication.grid(row=0, column=1, padx=10, pady=10)

# Inner Quantity
ttk.Label(form_frame, text="Inner Quantity:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_inner_qty = ttk.Entry(form_frame, width=32)
entry_inner_qty.grid(row=1, column=1, padx=10, pady=10)

# Loose Quantity
ttk.Label(form_frame, text="Loose Quantity:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_loose_qty = ttk.Entry(form_frame, width=32)
entry_loose_qty.grid(row=2, column=1, padx=10, pady=10)

# Outer Quantity
ttk.Label(form_frame, text="Outer Quantity:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
entry_outer_qty = ttk.Entry(form_frame, width=32)
entry_outer_qty.grid(row=3, column=1, padx=10, pady=10)

# Buttons frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

add_button = ttk.Button(button_frame, text="Add Stock", command=add_stock)
add_button.pack(pady=10)

back_button = ttk.Button(root, text="Back", command=mv_open)
back_button.pack(anchor='nw', padx=20, pady=20)

root.mainloop()