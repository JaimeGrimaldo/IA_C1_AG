import math
import random
import matplotlib.pyplot as plt
from tkinter import *


ventana = Tk()
ventana.title("191214 - Grimaldo Moreno - IA - IDS")

#? INTERFAZ GRAFICA TKINTER
#x1, x2, precision, tamaño poblacion, maximo de poblacion, generaciones

entradaA = Entry(ventana, font=("Arial 12"))
entradaA.grid(row=2, column=1, columnspan=1, padx=5, pady=1)
entradaB = Entry(ventana, font=("Arial 12"))
entradaB.grid(row=2, column=2, columnspan=1, padx=5, pady=1)
entradaPrecision = Entry(ventana, font=("Arial 12"))
entradaPrecision.grid(row=4, column=1, columnspan=3, padx=5, pady=1)
entradaPoblacionInicial = Entry(ventana, font=("Arial 12"))
entradaPoblacionInicial.grid(row=6, column=1, columnspan=3, padx=5, pady=1)
entradaPoblacionMaxima = Entry(ventana, font=("Arial 12"))
entradaPoblacionMaxima.grid(row=8, column=1, columnspan=3, padx=5, pady=1)
entradaGeneraciones = Entry(ventana, font=("Arial 12"))
entradaGeneraciones.grid(row=10, column=1, columnspan=3, padx=5, pady=1)

texto_1 = Label(ventana, font=("Arial 18"), text="Algoritmo Genetico - Max Min")
texto_1.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

texto_2 = Label(ventana, font=("Arial 12"), text="A")
texto_2.grid(row=1, column=1, columnspan=1, padx=5, pady=1)

texto_3 = Label(ventana, font=("Arial 12"), text="B")
texto_3.grid(row=1, column=2, columnspan=1, padx=5, pady=1)

texto_4 = Label(ventana, font=("Arial 12"), text="Precision")
texto_4.grid(row=3, column=1, columnspan=3, padx=5, pady=1)

texto_5 = Label(ventana, font=("Arial 12"), text="Población inicial")
texto_5.grid(row=5, column=1, columnspan=3, padx=5, pady=1)

texto_6 = Label(ventana, font=("Arial 12"), text="Población máxima")
texto_6.grid(row=7, column=1, columnspan=3, padx=5, pady=1)

texto_7 = Label(ventana, font=("Arial 12"), text="Cantidad de generaciones")
texto_7.grid(row=9, column=1, columnspan=3, padx=5, pady=1)

textoVacio = Label(ventana, font=("Arial 12"), text=" ")
textoVacio.grid(row=11, column=1, columnspan=3, padx=5, pady=5)
textoVacio2 = Label(ventana, font=("Arial 12"), text=" ")
textoVacio2.grid(row=13, column=1, columnspan=3, padx=5, pady=5)

boton_iniciar = Button(ventana, text="INICIAR", width=10, height=1, font=("Arial 18"), command = lambda: Start())
boton_iniciar.grid(row=12, column=0, columnspan=3)


deltaX = []
tamanioPoblacionInicial = 0
tamanioPoblacionMax = 0
contadorGeneracion = 0
contadorControl = 0
poblacionInicial = []  # ? poblacionInicial
listaInicial = []  # listaInicial #! ------------------------------------------------------
listaCruza = []
listaMutacion = []
listaAptitud = []
listaMejores = []
listaMejoresGeneracion = []
listaPeoresGeneraciones = []
listaPromedioGeneraciones = []
fenotipoX = []
listaFitness = []
listaGeneracion = []


def Fitness(x):
    multi = 0.50 * x
    cose = math.cos(multi)
    seno = math.sin(multi)
    sen_cos = seno * cose
    multi2 = sen_cos * 0.25
    cose2 = cose * 0.50
    y = multi2 + cose2
    return y


def Bitaje(x1, x2, precision):  # ? Calcular tamaño de los individuos (bitaje)
    # deltaX es un valor que se compara con la precision ingresada, si la precision es menor que la division entre intervalo y bitaje
    # O se trabaja con DeltaX o con Precision
    global deltaX
    intervalo = abs(x2-x1)
    valores = intervalo / precision
    bitaje = 0
    bit = 2
    bandera = True
    while bandera:
        bit2 = math.pow(bit, bitaje)
        if valores <= bit2:
            bandera = False
        else:
            bitaje = bitaje + 1

        valores2 = intervalo / bit2
    if precision >= valores2:
        deltaX.append(valores2)
    else:
        deltaX.append(precision)
    return bitaje


def BinarioDecimal(binario):
    numero_decimal = 0
    for posicion, digito_string in enumerate(binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal


def FenotipoX(genotipoX, x1, x2):  # ? Genotipo = binario a decimal
    global deltaX
    if x1 > x2:
        a = x2
    else:
        a = x1
    x = genotipoX * deltaX[0]
    xi = a + x
    return xi


def GenerarIndividuos(tamanioPoblacion, bitaje):
    cadena = ""
    listaIndividuo = []
    for i in range(int(tamanioPoblacion)):
        cadena = ""
        for x in range(bitaje):
            cadena += str(random.randint(0, 1))
        listaIndividuo.append(cadena)
    return listaIndividuo


def GenerarPoblacion(tamanioPoblacion, bitaje):
    global contadorControl, poblacionInicial
    global listaInicial, listaCruza, listaMutacion, listaAptitud

    poblacionInicial = GenerarIndividuos(tamanioPoblacion, bitaje)
    for i in range(tamanioPoblacion):
        TablaInicial = (
            {
                "ID": i,
                "Poblacion Inicial X": poblacionInicial[i],
                "Decimal": 0,
                "Fenotipo X": 0,
                "Fitness": 0,
            },
        )
        TablaCruza = (
            {
                "ID": i,
                "Auxiliar Individuo": poblacionInicial[i],
                "Punto de cruza X": 0,
                "Despues de cruza X": 0,
                "Decimal": 0,
                "Fenotipo X": 0,
                "Fitness": 0,
            },
        )
        TablaMutacion = (
            {
                "ID": i,
                "Cruzado X": 0,
                "Mutado X": 0,
                "Decimal": 0,
                "Fitness": 0,

            },
        )
        TablaFitness = (
            {
                "Padre X": 0,
                "Hijo X": 0,
                "Fitness Hijo": 0,
                "Fitness Padre": 0,
                "Mejor fitness": 0,
            },
        )
        listaInicial.extend(TablaInicial)
        listaCruza.extend(TablaCruza)
        listaMutacion.extend(TablaMutacion)
        listaAptitud.extend(TablaFitness)
        contadorControl += 1


def SeleccionarMejores(x1, x2):
    global contadorGeneracion, deltaX, listaFitness
    global listaInicial, listaCruza, listaAptitud, listaMejores

    sumaFitness = 0
    promedioFitness = 0

    mejorFitness = 0
    peorFitness = 0

    for i in range(len(listaInicial)):
        cadenaX = listaInicial[i].get("Poblacion Inicial X")
        valorX = BinarioDecimal(str(cadenaX))
        listaInicial[i].update({"Decimal": valorX})
        fenotipoX = FenotipoX(valorX, x1, x2)
        listaInicial[i].update({"Fenotipo X": fenotipoX})

        fitness = Fitness(fenotipoX)
        listaFitness.append(fitness)
        listaInicial[i].update({"Fitness": fitness})
        sumaFitness = sumaFitness + fitness
    promedioFitness = sumaFitness / len(listaInicial)

    for i in range(len(listaInicial)):
        if i == 0:
            mejorFitness = listaInicial[0].get("Fitness")
            peorFitness = listaInicial[0].get("Fitness")
        else:
            if mejorFitness > listaInicial[i].get("Fitness"):
                mejorFitness = listaInicial[i].get("Fitness")
            if peorFitness < listaInicial[i].get("Fitness"):
                peorFitness = listaInicial[i].get("Fitness")
    mejores = (
        {
            "Generacion": contadorGeneracion,
            "Mejor": mejorFitness,
            "Peor": peorFitness,
            "Promedio": promedioFitness,
            "Delta X": deltaX[0],
            "FenotipoX": fenotipoX,
        },
    )
    print(
        "Generacion: ",
        contadorGeneracion,
        "Mejor fitness: ",
        mejorFitness,
        "Peor fitness: ",
        peorFitness,
        "Promedio de fitness: ",
        promedioFitness,
    )

    listaMejores.extend(mejores)

    for i in range(len(listaInicial)):
        listaCruza[i].update(
            {
                "Auxiliar Individuo": listaInicial[i].get("Poblacion Inicial X"),
            }
        )
        listaAptitud[i].update(
            {
                "Padre X": listaInicial[i].get("Poblacion Inicial X"),
                "Fitness Padre": listaInicial[i].get("Fitness"),
            },
        )


def Cruza(bitaje, x1, x2):
    global listaCruza, listaMutacion, listaAptitud
    cadena1X = ""
    cadena2X = ""
    auxCadena1X = ""
    auxCadena2X = ""

    for i in range(0, len(listaCruza), 2):
        tamanioX = len(listaCruza[i].get("Auxiliar Individuo"))
        tamanio2X = len(listaCruza[i+1].get("Auxiliar Individuo"))
        corte = random.randint(1, bitaje)
        cadena1X = listaCruza[i].get("Auxiliar Individuo")[0:corte]
        cadena2X = listaCruza[i+1].get("Auxiliar Individuo")[0:corte]
        auxCadena1X = listaCruza[i].get("Auxiliar Individuo")[corte:tamanioX]
        auxCadena2X = listaCruza[i+1].get("Auxiliar Individuo")[corte:tamanio2X]
        cadena1X = cadena1X + auxCadena2X
        cadena2X = cadena2X + auxCadena1X

        listaCruza[i].update(
            {
                "Punto de cruza X": corte,
                "Despues de cruza X": cadena1X,
            },
        )
        listaCruza[i+1].update(
            {
                "Punto de cruza X": corte,
                "Despues de cruza X": cadena2X,
            },
        )
        listaMutacion[i].update(
            {
                "Cruzado X": cadena1X,
            },
        )
        listaMutacion[i+1].update(
            {
                "Cruzado X": cadena2X,
            },
        )

    for i in range(len(listaCruza)):
        cadenitaX = listaCruza[i].get("Despues de cruza X")
        cadenitaX = BinarioDecimal(cadenitaX)
        listaCruza[i].update(
            {
                "Decimal": cadenitaX,
            },
        )
        valorX = listaCruza[i].get("Decimal")
        fenotipoX = FenotipoX(valorX, x1, x2)
        fitness = Fitness(fenotipoX)
        listaCruza[i].update(
            {
                "Fenotipo X": fenotipoX,
                "Fitness": fitness,
            },
        )


def Mutacion(x1, x2, maxPoblacion):
    global listaMutacion, contadorGeneracion
    auxMutado = []
    originalX = ""
    mutadoX = ""
    for i in range(0, len(listaMutacion), 2):
        originalX = ""
        mutadoX = ""
        originalX = listaMutacion[i].get("Cruzado X")

        if bool(random.getrandbits(1)):
            for x in originalX:
                if bool(random.getrandbits(1)):
                    if x == "1":
                        mutadoX += "0"
                    else:
                        mutadoX += "1"
                else:
                    mutadoX += x

            listaMutacion[i].update(
                {
                    "Mutado X": mutadoX,
                },
            )
        else:
            listaMutacion[i].update(
                {
                    "Mutado X": originalX,
                },
            )
        mutadoX = ""
        originalX = listaMutacion[i+1].get("Cruzado X")

        if bool(random.getrandbits(1)):
            for x in originalX:
                if bool(random.getrandbits(1)):
                    if x == "1":
                        mutadoX += "0"
                    else:
                        mutadoX += "1"
                else:
                    mutadoX += x

            listaMutacion[i+1].update(
                {
                    "Mutado X": mutadoX,
                }
            )
        else:
            listaMutacion[i+1].update(
                {
                    "Mutado X": originalX,
                }
            )

    for i in range(len(listaMutacion)):
        cadenaX = listaMutacion[i].get("Mutado X")
        valorX = BinarioDecimal(cadenaX)

        listaMutacion[i].update(
            {
                "Decimal": valorX,
            },
        )
        fenotipoX = FenotipoX(valorX, x1, x2)

        fitness = Fitness(fenotipoX)
        listaMutacion[i].update(
            {
                "Fitness": fitness
            },
        )
        listaAptitud[i].update(
            {
                "Hijo X": cadenaX,
                "Fitness Hijo": fitness,
            },
        )
        if listaAptitud[i].get("Fitness Hijo") < listaAptitud[i].get("Fitness Padre"):
            listaAptitud[i].update(
                {
                    "Mejor fitness": listaAptitud[i].get("Fitness Hijo"),
                }
            )
        else:
            listaAptitud[i].update(
                {
                    "Mejor fitness": listaAptitud[i].get("Fitness Padre")
                }
            )
    auxMutado = listaMutacion
    auxMutado = sorted(auxMutado, key=lambda x: x["Fitness"], reverse=True)
    Actualizar(auxMutado, maxPoblacion)


def Actualizar(auxMutado, maxPoblacion):
    global listaCruza, listaMutacion, listaInicial, listaAptitud
    global contadorControl
    for i in range(2):
        if contadorControl < maxPoblacion:
            contadorControl += 1

            TablaInicial = (
                {
                    "ID": contadorControl - 1,
                    "Poblacion Inicial X": auxMutado[i].get("Mutado X"),
                    "Decimal": 0,
                    "Fenotipo X": 0,
                    "Fitness": 0,
                },
            )
            TablaCruza = (
                {
                    "ID": contadorControl-1,
                    "Auxiliar Individuo": auxMutado[i].get("Mutado X"),
                    "Punto de cruza X": 0,
                    "Despues de cruza X": 0,
                    "Decimal": 0,
                    "Fenotipo X": 0,
                    "Fitness": 0,
                },
            )
            TablaMutacion = (
                {
                    "ID": contadorControl-1,
                    "Cruzado X": 0,
                    "Mutado X": 0,
                    "Decimal": 0,
                    "Fitness": 0,

                },
            )
            TablaFitness = (
                {
                    "Padre X": 0,
                    "Hijo X": 0,
                    "Fitness Hijo": 0,
                    "Fitness Padre": 0,
                    "Mejor fitness": 0,
                },
            )
            listaInicial.extend(TablaInicial)
            listaCruza.extend(TablaCruza)
            listaMutacion.extend(TablaMutacion)
            listaAptitud.extend(TablaFitness)
        else:
            ControlPoblacion(contadorControl)


def ControlPoblacion(contadorControl):
    global listaInicial, listaAptitud
    for i in range(contadorControl):
        if listaAptitud[i].get("Fitness Hijo") < listaAptitud[i].get("Fitness Padre"):
            listaInicial[i].update(
                {
                    "Poblacion Inicial X": listaAptitud[i].get("Hijo X"),
                },
            )
        else:
            listaAptitud[i].update(
                {
                    "Poblacion Inicial X": listaAptitud[i].get("Padre X"),
                },
            )
        listaInicial[i].update(
            {
                "Decimal": 0,
                "Fenotipo X": 0,
                "Fitness": 0,
            }
        )


def Clasificar(generaciones):
    global listaMejores, listaPeoresGeneraciones, listaPromedioGeneraciones, fenotipoX, listaMejoresGeneracion
    for i in range(generaciones):
        listaMejoresGeneracion.append(listaMejores[i].get("Mejor"))
        listaPeoresGeneraciones.append(listaMejores[i].get("Peor"))
        listaPromedioGeneraciones.append(listaMejores[i].get("Promedio"))
        fenotipoX.append(listaMejores[i].get("FenotipoX"))


def GenerarGrafica(mejor, peor, promedio, fenX):
    plt.title(f'Coordenadas del mejor caso: X ={fenX}')
    plt.plot(mejor, label="Mejor", color="Blue")  # Dibuja el gráfico
    plt.xlabel("Generaciones")  # Inserta el título del eje X
    plt.ylabel("Evolucion del Fitness")  # Inserta el título del eje Y
    plt.ioff()  # Desactiva modo interactivo de dibujo
    plt.ion()  # Activa modo interactivo de dibujo
    # Dibuja datos de lista2 sin borrar datos de lista1
    plt.plot(peor, label="Peor", color="Pink")
    plt.ioff()  # Desactiva modo interactivo
    plt.ion()  # Activa modo interactivo de dibujo
    plt.plot(promedio, label="Promedio", color="Orange")
    # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()  # Desactiva modo interactivo
    # plt.plot(lista3)   # No dibuja datos de lista3
    plt.legend()
    plt.show()  # Fuerza dibujo de datos de lista3


def VerSeleccion():
    global listaInicial
    for i in range(len(listaInicial)):
        print(listaInicial[i])


def VerCruza():
    global listaCruza
    for i in range(len(listaCruza)):
        print(listaCruza[i])


def VerMutacion():
    for i in range(len(listaMutacion)):
        print(listaMutacion[i])


def VerAptitud():
    global listaAptitud
    for i in range(len(listaAptitud)):
        print(listaAptitud[i])


def VerMejores():
    global listaMejores
    for i in range(len(listaMejores)):
        print(listaMejores[i])


def Empezar(x1, x2, precision, tamanioPoblacion, maximoPoblacion, generacion):
    global contadorGeneracion, listaGeneracion
    cadenaX = Bitaje(x1, x2, precision)
    GenerarPoblacion(tamanioPoblacion, cadenaX)
    for i in range(generacion):
        contadorGeneracion += 1
        print("Generacion No.", contadorGeneracion, "\n")
        SeleccionarMejores(x1, x2)
        Cruza(cadenaX, x1, x2)
        Mutacion(x1, x2, maximoPoblacion)
        listaGeneracion.append(i)


def Start():
    global listaMejoresGeneracion, listaPeoresGeneraciones, listaPromedioGeneraciones

    x1 = int(entradaA.get())
    x2 = int(entradaB.get())
    precision = float(entradaPrecision.get())
    tamanioPoblacions = int(entradaPoblacionInicial.get())
    maximoPoblacions = int(entradaPoblacionMaxima.get())
    generacion = int(entradaGeneraciones.get())

    Empezar(x1, x2, precision, tamanioPoblacions, maximoPoblacions, generacion)
    Clasificar(generacion)
    fenx = fenotipoX[generacion-1]
    GenerarGrafica(listaMejoresGeneracion, listaPeoresGeneraciones, listaPromedioGeneraciones, fenx)

    print("\n")
    VerSeleccion()
    print("\nTERMINA SELECCION\nINICIACRUZA\n")
    VerCruza()
    print("\nTERMINA CRUZA\nINCIA MUTACION\n")
    VerMutacion()
    print("\nTERMINA MUTACION\nINICIA\n")
    VerAptitud()
    print("\nTERMINA APTITUD\nINICIA MEJORES OP")
    VerMejores()


ventana.mainloop()

#if __name__ == '__main__': 
    #Start()
