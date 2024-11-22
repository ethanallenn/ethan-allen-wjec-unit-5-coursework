import tkinter as tk
from tkinter import ttk
import csv
import sqlite3
from datetime import datetime

class StockManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Stock Management")

        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Initialize row counter
        self.row_counter = 0

        # Create initial item selection and stock entry
        self.create_item_selection(self.main_frame, self.row_counter)
        self.create_stock_entry(self.main_frame, self.row_counter)

        # Create add stock button
        self.create_add_stock_button(self.main_frame)

        # Create delete stock button
        self.create_delete_stock_button(self.main_frame)

        # Create upload stock button
        self.create_upload_stock_button(self.main_frame)

        # List to store stock data
        self.stock_data = []

    def create_item_selection(self, frame, row):
        ttk.Label(frame, text="Select Item:").grid(row=row, column=0, sticky=tk.W)

        item_var = tk.StringVar()
        item_dropdown = ttk.Combobox(frame, textvariable=item_var)
        item_dropdown['values'] = self.get_item_list()
        item_dropdown.grid(row=row, column=1, sticky=(tk.W, tk.E))
        item_dropdown.config(width=50)

        return item_var

    def create_stock_entry(self, frame, row):
        ttk.Label(frame, text="Stock Count:").grid(row=row, column=2, sticky=tk.W)

        stock_var = tk.IntVar()
        stock_entry = ttk.Entry(frame, textvariable=stock_var)
        stock_entry.grid(row=row, column=3, sticky=(tk.W, tk.E))
          # Adjust the width of the dropdown

        return stock_var

    def create_add_stock_button(self, frame):
        self.add_stock_button = ttk.Button(frame, text="Add Stock", command=self.add_stock)
        self.add_stock_button.grid(row=1000, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def create_delete_stock_button(self, frame):
        self.delete_stock_button = ttk.Button(frame, text="Delete Stock", command=self.delete_stock)
        self.delete_stock_button.grid(row=1000, column=2, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def create_upload_stock_button(self, frame):
        ttk.Label(frame, text="Stock Check Date:").grid(row=1001, column=0, sticky=tk.W)
        self.date_var = tk.StringVar()
        date_entry = ttk.Entry(frame, textvariable=self.date_var)
        date_entry.grid(row=1001, column=1, sticky=(tk.W, tk.E))

        self.upload_stock_button = ttk.Button(frame, text="Upload Stock", command=self.upload_stock)
        self.upload_stock_button.grid(row=1001, column=2, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def get_item_list(self):
        return [
            "Aches and Pains: Acetaminophen",
            "Aches and Pains: Ibuprofen",
            "Aches and Pains: Naproxen",
            "Upset stomach and/or indigestion: Antacid",
            "Upset stomach and/or indigestion: Polyethylene glycol",
            "Upset stomach and/or indigestion: Loperamide",
            "Upset stomach and/or indigestion: Bismuth subsalicylate",
            "Cold and flu: Thermometer",
            "Cold and flu: Pseudoephedrine",
            "Cold and flu: Dextromethorphan",
            "Cold and flu: Guaifenesin",
            "Cold and flu: Nasal saline",
            "Allergies: Diphenhydramine",
            "Allergies: Loratadine",
            "Allergies: Nasal saline",
            "Allergies: Fluticasone propionate nasal spray",
            "Sexually transmitted infections and pregnancy: Condoms",
            "Sexually transmitted infections and pregnancy: Emergency contraception",
            "Sexually transmitted infections and pregnancy: Pregnancy test",
            "Wound care: Adhesive bandages",
            "Wound care: Topical ointments",
            "Wound care: Gauze",
            "Wound care: Adhesive Tape",
            "Acne: Benzoyl peroxide",
            "Acne: Adapalene",
            "Acne: Gentle skin-care cleanser"
        ]

    def add_stock(self):
        item_var = self.create_item_selection(self.main_frame, self.row_counter)
        stock_var = self.create_stock_entry(self.main_frame, self.row_counter)
        self.stock_data.append((item_var, stock_var))
        self.row_counter += 1

    def delete_stock(self):
        if self.row_counter > 0:
            self.row_counter -= 1
            item_var, stock_var = self.stock_data.pop()
            item_var.set('')
            stock_var.set(0)
            for widget in self.main_frame.grid_slaves(row=self.row_counter):
                widget.grid_forget()

    def upload_stock(self):
        stock_check_date = self.date_var.get()
        if not stock_check_date:
            print("Please enter the stock check date.")
            return

        stock_entries = []
        for item_var, stock_var in self.stock_data:
            item = item_var.get()
            stock_count = stock_var.get()
            if item and stock_count:
                stock_entries.append((item, stock_count))

        if not stock_entries:
            print("No stock data to upload.")
            return

        # Save to CSV
        filename = f"{stock_check_date}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Item", "Stock Count"])
            writer.writerows(stock_entries)
        print(f"Stock data saved to {filename}")

        # Save to SQLite database
        conn = sqlite3.connect('stock.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS stock
                          (date TEXT, item TEXT, stock_count INTEGER)''')
        for item, stock_count in stock_entries:
            cursor.execute("INSERT INTO stock (date, item, stock_count) VALUES (?, ?, ?)",
                           (stock_check_date, item, stock_count))
        conn.commit()
        conn.close()
        print("Stock data saved to stock.db")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockManagementApp(root)
    root.mainloop()
