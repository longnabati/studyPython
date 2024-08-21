import tkinter as tk
from tkinter import messagebox,ttk
#Main Window
USER_NAME = "totai"
PASSWORD = "1234"


def click():
    username = txt_user_name.get()
    password = txt_password.get()
    if username == USER_NAME and password == PASSWORD:
        messagebox.showinfo("Info","Login thanh cong")
        
    else:
        messagebox.showerror("Error","Login that bai")
    
    
    
root = tk.Tk()
root.title("Drawing")
root.geometry("400x200+200+50")
root.iconbitmap("star.ico")
# root.resizable(False, False)
root.config(bg = "black")


#grid layout mannger
lbl_text = tk.Label(root, text = "User_name",bg = "orange", fg= "white")
lbl_text.grid(row = 0, column = 0,padx = (30,0))

txt_user_name = tk.Entry(root, width = "30")
txt_user_name.grid(row = 0 , column = 1,padx = (30,0))

lbl_pass = tk.Label(root,text = "Password", bg = "orange", fg = "white")
lbl_pass.grid(row = 1, column = 0,padx = (30,0),pady=(20,0))

txt_password = tk.Entry(root,width = "30")                                    #Row là cột, Column là hàng
txt_password.grid(row = 1, column= 1,padx = (30,0),pady = (20,20))

btn_submit = ttk.Button(root, text = "Login",command= click)
btn_submit.grid(row= 2,column=1,ipadx = 20, ipady = 5)

root.mainloop()