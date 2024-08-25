"""
    + Combobox
    + Scrolltext
    + Google Translator 
"""

import tkinter as tk
from tkinter import ttk,messagebox
from calendar import month_name
from datetime import datetime

def show(event):
    selected_month = cur_month.get()
    messagebox.showinfo("Succes", message= f"Your selected {selected_month}")
    
root = tk.Tk()
root.title("Combobox")
root.geometry("400x200")

cur_month = tk.StringVar()
ttk.Label(root,text = "Please select a month:",font = ("Arial", 18, "bold"),anchor=tk.CENTER).pack(fill= tk.X,padx = 5, pady=5)

months = [month_name[m][:3] for m in range (1,13)]
month = ttk.Combobox(root,values = months, textvariable= cur_month)
month.pack(fill = tk.X)
root.bind("<<ComboboxSelected>>",show)

months = datetime.now().strftime("%B")
month.set(months)

root.mainloop()