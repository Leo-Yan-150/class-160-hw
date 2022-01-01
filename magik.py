from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background='lightskyblue')

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.25,rely=0.04,anchor=CENTER)

input_file_name = Entry(root, background='aliceblue')
input_file_name.place(relx=0.49,rely=0.04,anchor=CENTER)

my_text = Text(root,height=35,width=80,background='azure')
my_text.place(relx=0.51,rely=0.56,anchor=CENTER)

root.mainloop()