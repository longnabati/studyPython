"""
    Label in Tkinter
    
"""
import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title ("Tkinter Label Demo")
root.geometry("300x150")
root.resizable(False,False)
root.iconbitmap("Clock-digital.ico")
root.config(bg= "black")

TEMP = [f"Thứ {i}" for i in range (2,8)]
WEEK_DAYS = ["Chủ nhật"] + TEMP


def update_label():
    week_day = int(time.strftime("%w"))
    week_day = WEEK_DAYS[week_day]
    
    hour = int(time.strftime("%H"))
    if hour > 12:
        hour = hour - 12
    cur_time = time.strftime(f"{hour:02}: %M: %S %p\n%d - %m - %Y\n    ") + week_day
    clock_label.config(text = cur_time)
    clock_label.after(1000,update_label)


clock_label = ttk.Label(root,background="black",foreground="cyan",font=("Arial",18,"bold"))
clock_label.pack(pady= 20)

update_label()
# lbl1 = ttk.Label(root, text = "This is a Label",background="cyan",borderwidth = 1,relief = tk.SOLID)
# lbl1.config(font=("Arial", 16),anchor = tk.CENTER)
# lbl1.grid(row= 0,column=0,ipadx = 10, ipady = 10,padx = (10,10))

# photo = tk.PhotoImage(file = "Discord logo.png")
# lbl2 = ttk.Label(root, image= photo,text = "Discord",compound="top")
# lbl2.grid(row= 1,column=0,ipadx = 10, ipady = 10,padx = (10,10))



root.mainloop()