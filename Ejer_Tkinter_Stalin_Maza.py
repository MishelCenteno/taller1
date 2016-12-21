#EPN-ESFOT 2016-B
#MAZA CAÑAR STALIN
#PROGRAMACION AVANZADA USO DE TKINTER

from tkinter import *
from tkinter import messagebox

def Suma():
   n1=int(ventana1.get())
   n2=int(ventana2.get())
   resultado=n1+n2
   imprimir(resultado)
   
def Resta():
   n1=int(ventana1.get())
   n2=int(ventana2.get())
   resultado=n1-n2
   imprimir(resultado)
   
def Mult():
   n1=int(ventana1.get())
   n2=int(ventana2.get())
   resultado=n1*n2
   imprimir(resultado)
  
def Div():
   n1=float(ventana1.get())
   n2=float(ventana2.get())
   resultado=n1/n2
   imprimir(resultado)

def borrar():
    ventana2.delete(0, END)
    ventana1.delete(0, END)
    
def imprimir(resultado):
    messagebox.showinfo("RESULT","El resultado es: " + str(resultado))   

def salir():
   messagebox.showinfo("WARNING","Usted Ha Salido!!" )
   pantalla.destroy()
   
pantalla = Tk() #creando la pantalla 
pantalla.title("Calculadora") #dandole un titulo a la pantalla
pantalla.geometry("225x280") #Dimensiones (ancho,alto)

label1 = Label(pantalla,text="Primer Numero",height = 2)
label1.pack() #creacion de una ventana ingreso datos y su label
ventana1=Entry(pantalla,bd=4)
ventana1.pack()

label2 = Label(pantalla,text="Segundo Numero",height = 2)
label2.pack()
ventana2=Entry(pantalla,bd=4)
ventana2.pack() #creando ventana ingreso datos y su label

boton1 = Button(pantalla, text = "Suma", command = Suma,
width=15,fg='green')  #Boton para la suma
boton1.pack()

boton2 = Button(pantalla, text = "Resta", command = Resta,
width=15,fg='blue')
boton2.pack() #Boton para la resta

boton3 = Button(pantalla, text = "Multiplicacion", command = Mult,
width=15,fg='green') #Boton para multiplicacion
boton3.pack()

boton4 = Button(pantalla, text = "Division", command = Div,
fg='blue',width=15) #Boton para la division
boton4.pack()

boton5 = Button(pantalla, text = "Borrar",
command = borrar,width=15)#Boton para borrar
boton5.pack(side=LEFT)

boton6 = Button(pantalla, text = "Salir", command = salir,
fg='red',width=15)#Boton Salir
boton6.pack(side=LEFT)

mainloop()
