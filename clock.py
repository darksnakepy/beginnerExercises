
from tkinter import *
from time import *

window = Tk()
window.resizable(False, False)
window.title("Clock :)")

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    time_label.after(1000, update)

    day_string = strftime("%d,%A,%B")
    day_label.config(text=day_string)


time_label = Label(window,font=("Arial", 50), fg="#7f15c2",bg="Black")
time_label.pack()

day_label = Label(window,font=("Ink Free", 30))
day_label.pack()

update()
window.mainloop()