"""
    + Entry : 1 đối tượng có thể nhập đối tượng vào
    + Buton : nút bấm
    + Grid  : lưới
"""

#Entry
import tkinter as tk
from math import *

# def show():
#     print(e1.get())
#     print(e2.get())
#     e1.delete(0, tk.END)
#     e2.delete(0,tk.END)
    
def show(event = None):
    result = eval(e.get())
    lab = tk.Label(root,text = "Result: "+ str(result))
    lab.grid(row = 1,column=0,columnspan=2)
      
    
root= tk.Tk()
root.title("Tkinter Entry")
root.geometry("400x200")
root.iconbitmap("star.ico")

# #Fame
# main_frame = tk.Frame(root)
# main_frame.pack(fill = tk.BOTH,expand = True,padx = 10,pady = 10)


# tk.Label(main_frame,text= "First Name").grid(row = 0, column  = 0)
# e1 = tk.Entry(main_frame)
# e1.grid(row = 0,column= 1)
# e1.insert(0,"To")

# tk.Label(main_frame,text = "Last Name").grid(row = 1, column = 0)
# e2 = tk.Entry(main_frame)
# e2.grid(row = 1,column= 1)
# e2.insert(0,"Tai")

# tk.Button(main_frame,text = "Login",command = show).grid (row = 2,column= 1,sticky = "w",pady =(10,0))


#VD2 
tk.Label(root,text = "Your expression").grid(row = 0, column= 0)
e = tk.Entry(root)
e.grid(row = 0, column=  1)

#bind
root.bind("<Return>",show)


root.mainloop()