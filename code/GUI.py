from tkinter import *
from tkinter import ttk

number = 4
window = Tk()
window.title("Mancala")
window.geometry('350x250')


def clicked():
    global number
    button = Button(window, text=number-1,
                    command=clicked, fg='black', bg='blue')
    button.grid(column=1, row=2, sticky='snew', ipadx=20, ipady=20)
    if(number != 1):
        number -= 1


button = Button(window, text=number, command=clicked, fg='black', bg='blue')
button.grid(column=1, row=2, sticky='snew', ipadx=20, ipady=20,)


window.mainloop()
