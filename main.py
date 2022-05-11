from random import *
from tkinter import *
import numpy
import math
from matplotlib import pyplot


def VerificarRango(xInicial, xFinal, precision):
    print(xInicial, xFinal, precision)
    rango = ((float(xFinal)-float(xInicial))/float(precision))+1
    if(rango <= 0):
        print("datos No validos")
    else:
        return rango


def GenerarIndividuos(cantidad, bitsNecesarios, descendencia, rango):
    individuos = []
    descendencia = rango*descendencia
    print("descendencia: ", descendencia)

    for i in range(int(cantidad)):
        individuo = randint(0, bitsNecesarios[0])

        while(individuo > descendencia or individuo > rango):
            individuo = randint(0, bitsNecesarios[0])

        individuo = bin(individuo)[2:]
        individuos.append(str(individuo))

    for i in range(len(individuos)):
        while(len(individuos[i]) < bitsNecesarios[1]):
            individuos[i] = "0"+individuos[i]

    return individuos


def CalcularBitsNecesarios(rango):
    aux = 1
    bitsNecesarios = 1
    valores = []
    while(aux <= rango):
        aux = aux*2
        bitsNecesarios += 1

    valores.append(aux)
    valores.append(bitsNecesarios)
    return valores


def Cruza(individuos, mutacionIndividuo, mutaciongen, rango):
    descendientes = []

    for i in range(len(individuos)-1):
        punto = randint(1, len(individuos[i-1]))
        descendiente1 = individuos[i][:punto]+individuos[i+1][punto:]
        descendientes.append(descendiente1)
        descendiente2 = individuos[i+1][:punto]+individuos[i][punto:]
        descendientes.append(descendiente2)

    print("P0: ", individuos)
    print("Cruza: ", descendientes)
    mutacionInd = MutacionInd(descendientes, mutacionIndividuo, rango)
    print("Mutacion Individuo: ", mutacionInd)
    mutacionGene = MutacionGen(mutacionInd, mutaciongen)
    print("Mutacion Gen: ", mutacionGene)
    limpiado = Limpiar(mutacionGene, rango)
    print("Limpia: ", limpiado)
    poblacionTotal = limpiado + individuos
    ordenado = OrdenarMayorAMenor(poblacionTotal)
    print("Ordenado: ", ordenado)
    return ordenado

def CalcularMejores(individuos, rango, deltaX):
    valores= []
    for i in range(len(individuos)):
        valores.append(float(rango)+int(individuos[i],2)*float(deltaX))
    return valores

def MutacionGen(mutacionInd, mutaciongen):
    mutaciones = []
    for i in range(len(mutacionInd)):
        nuevoGen = ""
        for x in range(len(mutacionInd[i])):
            random = randint(0, 100)
            if(random < mutaciongen*100):
                indiv = mutacionInd[i][x]
                if(str(indiv) == "0"):
                    nuevoGen += "1"
                else:
                    nuevoGen += "0"
            else:
                indiv = mutacionInd[i][x]
                nuevoGen += str(indiv)
        mutaciones.insert(i, nuevoGen)

    return mutaciones


def MutacionInd(poblacion, mutacionIndividuo, rango):
    poblacionFinal = []
    limite = rango*mutacionIndividuo

    for i in range(len(poblacion)):
        decimal = int(poblacion[i], 2)
        if(decimal <= limite):
            poblacionFinal.append(poblacion[i])

    return poblacionFinal


def Limpiar(array, rango):
    listaLimpia = []
    for i in range(len(array)):
        if(int(array[i], 2) <= rango):
            listaLimpia.insert(i, array[i])

    return listaLimpia


def OrdenarMayorAMenor(lista):
    ordenado = []
    pos = 0
    for x in range(len(lista)):
        aux = 0
        for y in range(len(lista)):
            if(aux <= int(lista[y], 2)):
                aux = int(lista[y], 2)
                pos = y

        ordenado.append(bin(aux)[2:])
        lista.remove(lista[pos])
    return ordenado


def Poda(poblacionActual, poblacionMax):
    while(len(poblacionActual) > int(poblacionMax)):
        debil = poblacionActual[-1]
        poblacionActual.remove(debil)
    return poblacionActual

def Graficar():
    x= numpy.array(range(20))
    y= numpy.zeros(len(x))

    for i in range (len(x)):
        y[i] = math.sin(x[i])

    pyplot.plot(x, y)
    pyplot.show()

def Iniciar(xInicial, xFinal, precision, p0, poblacionMaxima):
    rango = VerificarRango(xInicial, xFinal, precision)
    text = Label(root, text="rango: "+str(rango))
    text.grid(row=0, column=3)

    bitsNecesarios = CalcularBitsNecesarios(rango)
    p0 = GenerarIndividuos(p0, bitsNecesarios, descendencia, rango)
    for i in range(len(p0)):
        listaInicial.insert(i, p0[i])

    cruza = Cruza(p0, mutacionIndividuo, mutacionGen, rango)
    for i in range(len(cruza)):
        listaCruza.insert(i, cruza[i])

    poda = Poda(cruza, poblacionMaxima)
    for i in range(len(poda)):
        listaLimpia.insert(i, poda[i])

    xi= CalcularMejores(poda, rango, precision)
    print("X(i): ", xi)


root = Tk()
root.title('Genetica')
root.geometry('500x300')

descendencia = 0.95
mutacionIndividuo = 0.25
mutacionGen = 0.40

xInicial = Entry(root)
xInicial.grid(row=0, column=0)
label1 = Label(root, text="Valor inicial de x:").grid(row=1, column=0)

xFinal = Entry(root)
xFinal.grid(row=0, column=1)
label2 = Label(root, text="Valor final de x:").grid(row=1, column=1)

precision = Entry(root)
precision.grid(row=0, column=2)
label3 = Label(root, text="Precisión:").grid(row=1, column=2)

p0 = Entry(root)
p0.grid(row=2, column=1)
label3 = Label(root, text="Poblacion inicial:").grid(row=3, column=1)

poblacionMaxima = Entry(root)
poblacionMaxima.grid(row=2, column=2)
label3 = Label(root, text="Poblacion maxima:").grid(row=3, column=2)

iniciar = Button(root, text="Iniciar", command=lambda: Iniciar(
    xInicial.get(), xFinal.get(), precision.get(), p0.get(), poblacionMaxima.get())).grid(row=2, column=0)

listaInicial = Listbox(root)
listaInicial.grid(row=4, column=0)
labelInicial = Label(root, text="Poblacion inicial").grid(row=5, column=0)

listaCruza = Listbox(root)
listaCruza.grid(row=4, column=1)
labelCruza = Label(
    root, text="Poblacion cruza + inicial").grid(row=5, column=1)

listaLimpia = Listbox(root)
listaLimpia.grid(row=4, column=2)
labelinicial = Label(root, text="Poblacion Podada").grid(row=5, column=2)

root.mainloop()
