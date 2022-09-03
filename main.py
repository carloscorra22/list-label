import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

label = ttk.Label(window, text="lista de cosas", background="gray")

lista = ['casa', 'auto', 'avion']
listaItems = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=15, listvariable=listaItems)

label.grid(column=1, row=0)
listbox.grid(column=1, row=1)
window.mainloop()