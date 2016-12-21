##TIBANTA MARIA FERNANDA
##EJERCICIO DE SUMA, RESTA Y MULTIPLICACION
from tkinter import*

def suma():
    total=int(entrada1.get())+int(entrada2.get())
    Label(ventana,text=total).pack()

def resta():
    total=int(entrada1.get())-int(entrada2.get())
    Label(ventana,text=total).pack()
    
def multiplicacion():
    total=int(entrada1.get())*int(entrada2.get())
    Label(ventana,text=total).pack()
    


ventana=Tk()
ventana.geometry("500x300")
ventana.title("OPERACIONES  BASICAS")
Label(ventana,text="Ingrese dos numeros: ").pack()

num1=IntVar()
num2=IntVar()

entrada1=Entry(ventana,textvariable=num1)
entrada1.pack()

entrada2=Entry(ventana,textvariable=num2)
entrada2.pack()

suma=Button(ventana,text="suma",command=suma)
resta=Button(ventana,text="resta",command=resta)
multiplicacion=Button(ventana,text="multiplicacion",command=multiplicacion)


suma.pack()
resta.pack()
multiplicacion.pack()


