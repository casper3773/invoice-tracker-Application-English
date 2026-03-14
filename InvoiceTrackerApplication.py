# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 03:15:18 2026

@author: muham
"""

import tkinter as tk
import csv
import os

def add_invoice():
    date = entry_date.get()
    description = entry_description.get()
    amount = entry_amount.get()
    vat = entry_vat.get()
    
    if date and description and amount and vat:
        listbox_invoices.insert(tk.END, f"{date} | {description} | {amount} € | VAT: {vat}%")
        
        file_path = os.path.join(os.path.dirname(__file__), "invoices.csv")
        
        try:
            with open(file_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([date, description, amount, vat])
        except PermissionError:
            print("Hata: invoices.csv dosyasına yazma izni yok.")
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")
        
        # Clear input fields
        entry_date.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_vat.delete(0, tk.END)

root = tk.Tk()
root.title("Invoice Tracker Application")

tk.Label(root, text="Date:").pack()
entry_date = tk.Entry(root)
entry_date.pack()

tk.Label(root, text="Description:").pack()
entry_description = tk.Entry(root)
entry_description.pack()

tk.Label(root, text="Amount:").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="VAT (%):").pack()
entry_vat = tk.Entry(root)
entry_vat.pack()

btn_add = tk.Button(root, text="Add", command=add_invoice)
btn_add.pack(pady=5)

listbox_invoices = tk.Listbox(root, width=50)
listbox_invoices.pack(pady=10)

root.mainloop()