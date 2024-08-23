import tkinter as tk
import os
import threading
from tkinter import messagebox
from pytube import YouTube

def on_click():
    try:
        ytb = YouTube(link.get())
        video = ytb.streams.get_highest_resolution()
        video.download(path.get())
        messagebox.showinfo("Succes","Download Success!!")
        os.startfile(path.get())
    except:
        messagebox.showerror("Error","Connection Problem!")

def dowload():
    threading.Thread(target=on_click).start()




root = tk.Tk()
root.title("Video Dowload")
root.geometry("400x200")

main_frame = tk.Frame(root)
main_frame.pack(fill = tk.BOTH, expand = True,padx = 40, pady = 10)

tk.Label(main_frame,text = "Youtube Downloader",font=("Arial",18, "bold")).grid(row = 0, column= 0,columnspan=2)

tk.Label(main_frame,text = "Enter Youtube URL: ").grid(row = 1,column=0)
link = tk.Entry(main_frame)
link.grid(row= 1, column= 1,sticky=" WE")

tk.Label(main_frame, text = "Enter Path: ").grid(row = 2,column=0)
path = tk.Entry(main_frame)
path.grid(row = 2, column= 1,sticky="WE",pady = (10,0))

tk.Button(main_frame,text = "Download Video",command=dowload).grid(row = 3, column= 0, columnspan=2,pady =(10, 0))
root.mainloop()