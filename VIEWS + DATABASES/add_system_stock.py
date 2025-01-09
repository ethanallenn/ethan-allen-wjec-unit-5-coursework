import sqlite3
import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('stock_database.db')
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                inner_qty INTEGER NOT NULL,
                loose_qty INTEGER NOT NULL,
                outer_qty INTEGER NOT NULL
            )''')

# List of common medications
medications = ["Paracetamol", "Ibuprofen", "Aspirin", "Amoxicillin", "Metformin"]

# Function to add stock to the database
def add_stock():
    item_name = selected_medication.get()
    inner_qty = int(entry_inner_qty.get())
    loose_qty = int(entry_loose_qty.get())
    outer_qty = int(entry_outer_qty.get())

    c.execute("INSERT INTO stock (item_name, inner_qty, loose_qty, outer_qty) VALUES (?, ?, ?, ?)",
              (item_name, inner_qty, loose_qty, outer_qty))
    conn.commit()

    # Clear the entry fields after adding the stock
    selected_medication.set(medications[0])
    entry_inner_qty.delete(0, tk.END)
    entry_loose_qty.delete(0, tk.END)
    entry_outer_qty.delete(0, tk.END)

    # Add a new row for the next entry
    add_new_row()

# Function to handle window closing
def on_closing():
    conn.close()
    root.destroy()

root = tk.Tk()
root.title("Pharmacy Stock Management")
root.geometry("1400x720")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Create a style for ttk widgets
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#f0f0f0')
style.configure('TButton', 
                padding=10, 
                font=('Helvetica', 12),
                background='#4a90e2',
                foreground='white')
style.configure('TEntry', 
                padding=5,
                font=('Helvetica', 12))
style.configure('TOptionMenu',
                padding=5,
                font=('Helvetica', 12))

main_frame = ttk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Header labels with modern styling
headers = ["Medication", "Inner Qty", "Loose Qty", "Outer Qty"]
for i, header in enumerate(headers):
    label = ttk.Label(main_frame, 
                      text=header,
                      font=('Helvetica', 14, 'bold'),
                      background='#f0f0f0')
    label.grid(row=0, column=i, padx=15, pady=(0, 20))

# Function to add a new row for entering stock
def add_new_row():
    row = len(main_frame.grid_slaves()) // 5
    selected_medication = tk.StringVar(value=medications[0])
    
    medication_menu = ttk.OptionMenu(main_frame, selected_medication, medications[0], *medications)
    medication_menu.grid(row=row, column=0, padx=15, pady=5)
    
    for i in range(1, 4):
        entry = ttk.Entry(main_frame, font=('Helvetica', 12))
        entry.grid(row=row, column=i, padx=15, pady=5)

# Function to save stock to CSV
def save_stock():
    rows = []
    for i in range(1, len(main_frame.grid_slaves()) // 5):
        item_name = main_frame.grid_slaves(row=i, column=0)[0].get()
        inner_qty = main_frame.grid_slaves(row=i, column=1)[0].get()
        loose_qty = main_frame.grid_slaves(row=i, column=2)[0].get()
        outer_qty = main_frame.grid_slaves(row=i, column=3)[0].get()
        rows.append([item_name, inner_qty, loose_qty, outer_qty])

    filename = f"stock_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item Name", "Inner Quantity", "Loose Quantity", "Outer Quantity"])
        writer.writerows(rows)

    # Clear the entry fields after saving the stock
    for widget in main_frame.winfo_children():
        widget.destroy()
    add_new_row()

# Button frame
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=0, column=4, rowspan=3, padx=(30, 0), sticky='n')

# Add styled buttons
add_btn = ttk.Button(button_frame, 
                     text="Add Stock",
                     command=add_stock,
                     style='TButton')
add_btn.pack(pady=5)

save_btn = ttk.Button(button_frame,
                      text="Save Stock",
                      command=save_stock,
                      style='TButton')
save_btn.pack(pady=5)

exit_btn = ttk.Button(button_frame,
                      text="Exit",
                      command=on_closing,
                      style='TButton')
exit_btn.pack(pady=5)

# Add initial row
add_new_row()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
