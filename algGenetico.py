

def deltaX():
    print('este es Delta X')

def iniciar():
    intervalo = int(interFinal) - int(interInicial)
    presi = intervalo / float(presicion) + 1
    print(presi)
    for n in range(1,9):
        if presi <= pow(2,n):
            print(n)
            break

    print('Fuera del Siclo For')
    binario = decimal_a_binario(presi)
    print(f"El número {presi} es {binario} en binario")

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



if __name__ == '__main__':
    interInicial = input(print('Ingresa Intervalo inicial'))
    interFinal = input(print('Ingresa el Intervalo Final'))
    presicion = input(print('Ingresa la Presicion'))
    iniciar()