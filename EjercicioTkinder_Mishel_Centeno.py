from tkinter import *

#funciones de procesamiento
def procesar():
    resultado = peso.get()/(altura.get()*altura.get())
    print ("Maza corporal:",resultado*10000)
    root = Tk()
    root.geometry('350x210+550+100')
    root.title("""Tabla de Referecnia""")
    lista=[
        ("30.00-34.99","""Obeso"""),
        ("25.00-29.99","""Sobrepeso"""),
        ("18.50-24.99","""Peso_Normal"""),
        ("17.00-19.49","""Delgadez_Aceptable"""),
        ("16.00-16.99","""Delgadez_Moderada"""),
        ("<16.00","""Delgadez_Severa"""),
        ("Indice_masa_corporal","""\t"Clasificacion""")
        ]
    listb = Listbox(root)
    for item in lista:
        listb.insert(0,item)
    listb.pack()
    root.mainloop()  
	
	
#Instancia de la clase Tk
ventana = Tk()
ventana.title('Calcular la Masa Corporal')

#Variables que almacenarán los datos
peso = IntVar()
altura = IntVar()

#generación de widgets
#peso
etiqueta_peso = Label(ventana, text='Peso en kg:')
entrada_peso = Entry(ventana, textvariable=peso)
etiqueta_peso.grid(row=1, column=1)
entrada_peso.grid(row=1, column=2)

#altura
etiqueta_altura = Label(ventana, text='Altura en cm: ')
entrada_altura = Entry(ventana, textvariable=altura)
etiqueta_altura.grid(row=2, column=1)
entrada_altura.grid(row=2, column=2)

#boton
boton = Button(ventana, text='Procesar', command=procesar, width=20)
boton.grid(row=8, column=3)

#ejecución de ventana
ventana.mainloop()
ventana
