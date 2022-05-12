import random
from tkinter import *
import numpy

poblacionInicial = []

def deltaX(bits):
    resulBits = pow(2,bits) - 1
    print(resulBits)
    resultado = bits / resulBits
    # print ("{0:.3f}".format(resultado))
    return "{0:.3f}".format(resultado)

def valorX(bits,i):
    x = int(entrada_intervalo.get().split(',')[0]) + int(i) * float(deltaX(bits))
    print('X es igual a '+str(x))

def iniciar():
    intervalo = entrada_intervalo.get().split(',')

    presicion = (int(intervalo[1]) - (int(intervalo[0]))) / float(entrada_precision.get()) + 1

    print(presicion)
    for bits in range(1,9):
        if presicion <= pow(2,bits):
            print(bits)
            valorX(bits,2)
            break

    print('Fuera del Siclo For')
    binario = decimal_a_binario(presicion)
    print(f"El número {presicion} es {binario} en binario")
    poblacion_Inicial(presicion)

def completar_vinario():
    print('entre a completar los binarios mi buen')


def poblacion_Inicial(presicion):
    for decimal in range(int(entrada_poiniciaL.get())):
        decimal = random.randint(0, int(presicion))
        binario = decimal_a_binario(decimal)
        if len(binario) < 7:
            completar_vinario()

        poblacionInicial.append(binario)
        print('poblacion inicial ' + str(binario))

    for n in poblacionInicial:
        print('Imprimiendo poblacion inicial' + str(n))


def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario


ventana = Tk()
ventana.geometry('648x700')
ventana.config(bg='#E5E6E8')
ventana.title('Algoritmo Gentico')

entrada_intervalo = StringVar()
entrada_precision = StringVar()
entrada_funcion = StringVar()
entrada_poiniciaL = StringVar()
entrada_pomaxima = StringVar()
entrada_iteracion = StringVar()
salida = StringVar()

label = Label(ventana, text='ALGORITMO GENETICO', fg='#72A7E9')
label.place(x=115, y=44)
label.config(font="Inter 27 italic", bg='#E5E6E8')

label_rango = Label(ventana, text='RANGO')
label_rango.place(x=30, y=200)
label_rango.config(font="Inter 10", bg='#E5E6E8')

label_precision = Label(ventana, text='PRECISIÓN')
label_precision.place(x=380, y=200)
label_precision.config(font='Inter 10', bg='#E5E6E8')

label_funcion = Label(ventana, text='FUNCIÓN')
label_funcion.place(x=30, y=300)
label_funcion.config(font='Inter 10', bg='#E5E6E8')

label_inicial = Label(ventana, text='PO INICIAL')
label_inicial.place(x=30, y=400)
label_inicial.config(font='Inter 10', bg='#E5E6E8')

label_maxima = Label(ventana, text='PO MAXIMA')
label_maxima.place(x=200, y=400)
label_maxima.config(font='Inter 10', bg='#E5E6E8')

label_iteracion = Label(ventana, text='NÚMERO DE ITERACIÓN')
label_iteracion.place(x=370, y=400)
label_iteracion.config(font='Inter 10', bg='#E5E6E8')

caja_rango = Entry(ventana, font='arial 13', justify='center', textvariable=entrada_intervalo, bg='#D3DAE2', bd=0)
caja_rango.place(x=30, y=225, width=229, height=36)

caja_precision = Entry(ventana, font='arial 13', justify='center', textvariable=entrada_precision, bg='#D3DAE2',
                           bd=0)
caja_precision.place(x=380, y=225, width=229, height=36)

caja_funcion = Entry(ventana, font='arial 13', justify='center', textvariable=entrada_funcion, bg='#D3DAE2', bd=0)
caja_funcion.place(x=30, y=325, width=578, height=36)

caja_inicial = Entry(ventana, font='arial 13', justify='center', textvariable=entrada_poiniciaL, bg='#D3DAE2', bd=0)
caja_inicial.place(x=30, y=425, width=144, height=36)

caja_maxima = Entry(ventana, font='arial 13', justify='center', textvariable=entrada_pomaxima, bg='#D3DAE2', bd=0)
caja_maxima.place(x=200, y=425, width=144, height=36)

caja_iteracion = Entry(ventana, font='arial 13', justify='center', textvariable=entrada_iteracion, bg='#D3DAE2',
                           bd=0)
caja_iteracion.place(x=370, y=425, width=238, height=36)

boton = Button(ventana, text='ACEPTAR', command=iniciar)
boton.place(x=200, y=550, width=205, height=38)
boton.config(font='Inter 15', bg='#F8E000', fg='black', bd=0)

ventana.mainloop()