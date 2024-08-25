"""
    ScrollText
    
"""

import tkinter as tk
from tkinter import ttk,scrolledtext
from translate import Translator
from threading import Thread
root = tk.Tk()
root.title("ScrollText DEMO")
root.geometry("400x400")
""" ScrollTEXT  """
# def show():
#     sc.delete("1.0",tk.END)

# root = tk.Tk()
# root.title("ScrollText DEMO")
# root.geometry("400x400")

# sc = scrolledtext.ScrolledText(root,width = 50, height = 10)
# sc.pack(padx =5, pady = 5)
# sc.insert("1.0","This is a cat!")

# ttk.Button(root,text="CLICK",command= show).pack(pady= 10)


"""Google Transletor"""

def on_click():
    _from = from_var.get()
    to = to_var.get()
    
    translator = Translator(from_lang = langs[_from], to_lang = langs[to])
    translattion = translator.translate(sc_from.get("1.0",tk.END))
    sc_to.insert("1.0",translattion)


def translate_text():
    Thread(target= on_click).start()

langs = {
    "Vietnamese":"vi",
    "English"   : "en",
    "Japanese"  : "ja",
    "Chinese"   : "zh"
}


main_frame = tk.Frame(root)
main_frame.pack(fill = tk.BOTH,expand=True, padx = 10, pady = 10)

ttk.Label(main_frame,text = "GooGle dich",font=("Arial",17,"bold")).grid(row= 0,column=0,columnspan=3)

from_var = tk.StringVar()
from_cb = ttk.Combobox(main_frame,textvariable=from_var, values = list(langs.keys()))
from_cb.grid(row = 1, column= 0,pady = 10,padx = (0,25))

to_var = tk.StringVar()
to_cb = ttk.Combobox(main_frame,textvariable=from_var, values = list(langs.keys()))
to_cb.grid(row = 1, column= 1,pady = 10)

sc_from = scrolledtext.ScrolledText(main_frame,width = 15, height = 5)
sc_from.grid(row = 2,column= 0,sticky="WE", padx =(0,25))

sc_to = scrolledtext.ScrolledText(main_frame,width = 15, height = 5)
sc_to.grid(row = 2,column= 1,sticky="WE")

ttk.Button(main_frame,text = "Dich", command=translate_text).grid(row= 3,column=0,columnspan=2,pady=(10,0))
root.mainloop()