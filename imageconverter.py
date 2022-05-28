import tkinter as tk
from tkinter import Button, Widget, font 
from PIL import Image
from tkinter import Label, filedialog as fd
import os 

def jpg_to_png():
    filename=fd.askopenfilename()
    if filename.endswith('.jpg'):
        Image.open(filename).save("Sample.png")
    else:
        Label_2=Label(window,text="Error!", width=20,fg="red", font=("bold",15))
        Label_2.place(x=80,y=280)

def png_to_ico():
    filename=fd.askopenfilename()
    if filename.endswith('.png'):
        Image.open(filename).save("Sample.ico")

    else:
        Label_2=Label(window,text="Error!", width=20,fg="red", font=("bold",15))
        Label_2.place(x=80,y=280)


window = tk.Tk()
window.geometry("400x400")
window.title("Image converter")
window.resizable(False, False)

label1 = Label(window, text="Select the image", width=20, font=("Bold", 15))
label1.place(x=80,y=80)

label3 = Label(window, text="Author: DarkSnake", width=80, font=("Bold",10))
label3.place(x=10,y=365)

button = Button(window,text="Jpg to Png", width=20, height=2, bg="brown",fg="white",command=jpg_to_png).place(x=120,y=120)
button2 = Button(window,text="Png to ICO", width=20, height=2, bg="brown",fg="white", command=png_to_ico).place(x=120,y=220)

if __name__ == "__main__":
    window.mainloop()
