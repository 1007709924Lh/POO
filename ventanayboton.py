from tkinter import *

window = Tk()

window.title("Ventana")

window.geometry('210x200')

lbl = Label(window, text="Escribe tu nombre")

lbl.grid(row=2, column=0, sticky="WE", padx=10, pady=10)

txt = Entry(window,width=30)

txt.grid(row=3, column=0, sticky="WE", padx=10, pady=5)

def clicked():

    res = "Hola, " + txt.get() + "\n un gusto conocerte."

    lbl.configure(text= res)

btn = Button(window, text="Presionar", command=clicked)

btn.grid(row=6, column=0, padx=10, pady=30)

window.mainloop()