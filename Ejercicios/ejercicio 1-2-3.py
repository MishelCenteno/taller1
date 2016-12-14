from tkinter import *

def ejercicio1():
    root = Tk()
    etiqueta1= Label(root, text="HOLA SOY  TKINTER")
    etiqueta1.pack()
    root.mainloop()

def ejercicio2():
    master = Tk()
    whatever_you_do = "PROGRAMACION AVANZADA 2016-B TALLER"
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
            print ("Aprendiendo a usar Tkinter en Programacion Avanzada!")
    
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

def ejercicio6():
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

def ejercicio7():
    master = Tk()
    var1 = IntVar()
    Checkbutton(master, text="Hombre", variable=var1).grid(row=0, sticky=W)
    var2 = IntVar()
    Checkbutton(master, text="Mujer", variable=var2).grid(row=1, sticky=W)
    mainloop()

def ejercicio8():
    ventana = Tk()
    print("Ejercicio 8")
    def estados_P():
        print("Hombre: ",var1.get())
        print("Mujer: ",var2.get())

    Label(ventana, text="Indicar el sexo:").grid(row=0, sticky=W)
    var1 = IntVar()
    Checkbutton(ventana, text="Hombre", variable=var1).grid(row=1,
    sticky=W)
    var2 = IntVar()
    Checkbutton(ventana, text="Mujer", variable=var2).grid(row=2,
    sticky=W)

    Button(ventana, text='Salir', command=ventana.quit).grid(row=3,
    sticky=W, padx=4)

    Button(ventana, text='Imprimir', command=estados_P).grid(row=4,
    sticky=W, pady=4)

    mainloop()
    #sirve para permitir usar la funcion ventana.quit()
    
    #row=fila
    #column = columna
    #pady es el espacio entre widgets
    #sticky == donde centrar el widged(opcion W es horizontal y centrado)


def ejercicio9():
    ventana = Tk()
    print("Ejercicio 9")
    Label(ventana, text="Nombre").grid(row=0)
    Label(ventana, text="Apellido").grid(row=1)

    e1 = Entry(ventana)
    e2 = Entry(ventana)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    mainloop( )


def ejercicio10():
    print("Ejercicio 10")
    def entrada_datos():    
        print("Nombre: " +  e1.get() + "\nApellido: " + e2.get())

    ventana = Tk()
    Label(ventana, text="Nombre").grid(row=0)
    Label(ventana, text="Apellido").grid(row=1)

    e1 = Entry(ventana)
    e2 = Entry(ventana)    
    e1.grid(row=0, column=1)  #manda los datos a la ventana y los imprime
    e2.grid(row=1, column=1)

    Button(ventana, text='Imprimir',
    command=entrada_datos).grid(row=3, column=1,  #crea boton y le asigna
    sticky=W, pady=4)  #que haga algo

    Button(ventana, text='Salir', command=ventana.quit).grid(row=3,
    column=0, sticky=W, pady=4)

    mainloop( )

def switch():
    print("Uso de Tinker con 10 Funciones diferentes 1 -10")
    selec = int(input("Ingrese el numero de la funcion a realizar\n"))
    if selec == 1:
        ejercicio1()
    if selec == 2:
        ejercicio2()
    if selec == 3:
        ejercicio3()
    if selec == 4:
        ejercicio4()
    if selec == 5:
        ejercicio5()
    if selec == 6:
        ejercicio6()
    if selec == 7:
        ejercicio7()
    if selec == 8:
        ejercicio8()
    if selec == 9:
        ejercicio9()
    if selec == 10:
        ejercicio10()

switch()   
