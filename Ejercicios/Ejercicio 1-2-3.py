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

ejercicio1()
ejercicio2()
ejercicio3()
