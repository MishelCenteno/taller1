

##Ejercicio 6

from tkinter import *

root = Tk()
v = IntVar()
v.set(1) #El valor que va aqui indica en boton se inicializara al ejecutar
languages = [("Python",1),
             ("Perl",  2),
             ("Java",  3),
             ("C++",   4),
             ("C",     5)]
def ShowChoice():
    print (v.get())
    Label(root,
    text=  "Escoja un lenguaje de programación:",
    justify = LEFT,
    padx = 20).pack()
for txt, val in languages:
    Radiobutton(root,
    text=txt, 
    indicatoron =0,
    width = 20,
    padx = 20,
    variable=v,
    command=ShowChoice,
    value=val).pack(anchor=W)
    
mainloop()

##Ejercicio 7

master = Tk()
var1 = IntVar()
Checkbutton(master, text="Hombre", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Mujer", variable=var2).grid(row=1, sticky=W)
mainloop()
