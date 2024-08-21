import tkinter as tk 

root = tk.Tk()
root.title("Testing")
root.config(bg = "white")
root.geometry("400x400")

i=0
COLORS = ('red','green','blue','yellow')
def change_color():
    global i
    if i == len(COLORS):
        i = 0
    lbl.config(bg = COLORS[i])
    i+= 1
    root.after(1000,change_color)
lbl= tk.Label(root, text = "testing" )    
lbl.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 10)

change_color()
    
root.mainloop()