import sqlite3
import tkinter as tk
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
root.title("User Menu")
root.geometry("1400x720")
root.config(bg="light blue")
root.resizable(False, False)  # Set the width and height of the window

frame = tk.Frame(root, bg="light blue")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
font_style = ("Helvetica", 16)

# Function to add a new row for entering stock
def add_new_row():
    row = len(frame.grid_slaves()) // 5
    selected_medication = tk.StringVar(value=medications[0])
    tk.OptionMenu(frame, selected_medication, *medications).grid(row=row, column=0, padx=10, pady=5)
    tk.Entry(frame, font=font_style).grid(row=row, column=1, padx=10, pady=5)
    tk.Entry(frame, font=font_style).grid(row=row, column=2, padx=10, pady=5)
    tk.Entry(frame, font=font_style).grid(row=row, column=3, padx=10, pady=5)

# Function to save stock to CSV
def save_stock():
    rows = []
    for i in range(1, len(frame.grid_slaves()) // 5):
        item_name = frame.grid_slaves(row=i, column=0)[0].get()
        inner_qty = frame.grid_slaves(row=i, column=1)[0].get()
        loose_qty = frame.grid_slaves(row=i, column=2)[0].get()
        outer_qty = frame.grid_slaves(row=i, column=3)[0].get()
        rows.append([item_name, inner_qty, loose_qty, outer_qty])

    filename = f"stock_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item Name", "Inner Quantity", "Loose Quantity", "Outer Quantity"])
        writer.writerows(rows)

    # Clear the entry fields after saving the stock
    for widget in frame.winfo_children():
        widget.destroy()
    add_new_row()

# Add initial row
add_new_row()

# Add buttons for adding new row and saving stock
tk.Button(frame, text="Add Stock", command=add_stock, font=font_style).grid(row=0, column=4, padx=10, pady=5)
tk.Button(frame, text="Save Stock", command=save_stock, font=font_style).grid(row=1, column=4, padx=10, pady=5)
tk.Button(frame, text="Exit", command=on_closing, font=font_style).grid(row=2, column=4, padx=10, pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
