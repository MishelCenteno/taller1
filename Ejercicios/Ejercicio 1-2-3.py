from tkinter import *

def ejercicio1():
    root = Tk()
    etiqueta1= Label(root, text="Hello Tkinter!")
    etiqueta1.pack()
    root.mainloop()

def ejercicio2():
    master = Tk()
    whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
    msg = Message(master, text = whatever_you_do)
    msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    msg.pack( )
    mainloop( )


def ejercicio3():
    class App:
        def  __init__(self, master):
            frame = Frame(master)
            frame.pack()
            self.button = Button(frame, text="SALIR",
            fg="red",command=frame.quit)
            self.button.pack(side=LEFT)
            self.slogan =Button(frame,text="ENTRAR",command=self.write_slogan)
            self.slogan.pack(side=LEFT)

    
        def write_slogan(self):
            print ("Estamos aprendiendo a usar Tkinter!")
    
    root = Tk()
    app = App(root)
    root.mainloop()
def ejercicio4():
    root = Tk()
    v = IntVar()
    Label(root,
     text="""Elija el lenguaje de programacion:""",
     justify = LEFT,
     padx = 20).pack()
    Radiobutton(root,
     text="Python",
     padx = 20,
     variable=v,
     value=1).pack(anchor=W)
    Radiobutton(root,
     text="Perl",
     padx = 20,
     variable=v,
     value=2).pack(anchor=W)

    mainloop()

    
    
def ejercicio5():
    root = Tk()
    v = IntVar()
    v.set(1) # initializing the choice, i.e. Python
    languages = [
     ("Python",1),
     ("Perl",2),
     ("Java",3),
     ("C++",4),
     ("C",5)
    ]
    def MostrarOpcion():
     print (v.get())
    Label(root,
     text="""Elije tu lenguaje favorito para programar:""",
     justify = LEFT,
     padx = 20).pack()
    for txt, val in languages:
     Radiobutton(root,
     text=txt,
     padx = 30,
    variable=v,
     command=MostrarOpcion,
     value=val).pack(anchor=W)
    mainloop()

from tkinter import *

root = Tk()
v = IntVar()
v.set(1) #El valor que va aqui indica en boton se inicializara al ejecutar
languages = [("Python",1),
             ("Perl",  2),
             ("Java",  3),
             ("C++",   4),
             ("C",     5)]

def ejercicio6():
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
    command=ejercicio6,
    value=val).pack(anchor=W)
mainloop()

def ejercicio7():

    master = Tk()
    var1 = IntVar()
    Checkbutton(master, text="Hombre", variable=var1).grid(row=0, sticky=W)
    var2 = IntVar()
    Checkbutton(master, text="Mujer", variable=var2).grid(row=1, sticky=W)
    mainloop()


ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()
ejercicio6()
ejercicio7()
