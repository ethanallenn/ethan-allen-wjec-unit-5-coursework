import sqlite3
import tkinter as tk

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

# Update the placement of the widgets to be inside the frame
tk.Label(frame, text="Item Name:", font=font_style, bg="light blue").grid(row=0, column=0, padx=10, pady=5)
selected_medication = tk.StringVar(value=medications[0])
dropdown_medication = tk.OptionMenu(frame, selected_medication, *medications)
dropdown_medication.config(font=font_style)
dropdown_medication.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Inner Quantity:", font=font_style, bg="light blue").grid(row=1, column=0, padx=10, pady=5)
entry_inner_qty = tk.Entry(frame, font=font_style)
entry_inner_qty.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Loose Quantity:", font=font_style, bg="light blue").grid(row=2, column=0, padx=10, pady=5)
entry_loose_qty = tk.Entry(frame, font=font_style)
entry_loose_qty.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Outer Quantity:", font=font_style, bg="light blue").grid(row=3, column=0, padx=10, pady=5)
entry_outer_qty = tk.Entry(frame, font=font_style)
entry_outer_qty.grid(row=3, column=1, padx=10, pady=5)

tk.Button(frame, text="Add Stock", command=add_stock, font=font_style).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Exit", command=on_closing, font=font_style).grid(row=5, column=0, columnspan=2, pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
