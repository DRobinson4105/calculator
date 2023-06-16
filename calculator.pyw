from tkinter import *
from functions import *

def calc():
    label["text"] = solve(entry.get())

    # Run the function in every 100ms
    master.after(100, calc)

master = Tk()
master.title('Calculator')
master.geometry("250x50")

Label(master, text="Calculate").grid(row=0, sticky = E)

entry = Entry(master)
entry.grid(row=0, column=1)

label = Label(master)
label.grid(row=1, column = 1)

calc()

master.mainloop()