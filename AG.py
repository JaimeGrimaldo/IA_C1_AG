from code import interact
from tkinter import *
from tkinter import font
import random
from tkinter import messagebox


ventana = Tk()
ventana.title("191214 - Grimaldo Moreno - IA - IDS")


#Datos de entrada
e_poblacionInicial = Entry(ventana, font=("Arial 18"))
e_poblacionInicial.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

e_poblacionMaxima = Entry(ventana, font=("Arial 18"))
e_poblacionMaxima.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

e_intervalo = Entry(ventana, font=("Arial 18"))
e_intervalo.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

e_precision = Entry(ventana, font=("Arial 18"))
e_precision.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

e_indice = Entry(ventana, font=("Arial 18"))
e_indice.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

#Etiquetas
texto_1 = Label(ventana, font=("Bebas 20"), text="Algoritmo Genetico - Max Min")
texto_1.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

texto_PO = Label(ventana, font=("Arial 18"), text="Población inicial:")
texto_PO.grid(row=1, column=0, padx=5, pady=5)

texto_PMaxima = Label(ventana, font=("Arial 18"), text="Población máxima:")
texto_PMaxima.grid(row=2, column=0, padx=5, pady=5)

texto_PMaxima = Label(ventana, font=("Arial 18"), text="Intérvalo:")
texto_PMaxima.grid(row=3, column=0, padx=5, pady=5)

texto_precision = Label(ventana, font=("Arial 18"), text="Precisión:")
texto_precision.grid(row=4, column=0, padx=5, pady=5)

texto_indice = Label(ventana, font=("Arial 18"), text="Indice:")
texto_indice.grid(row=5, column=0, padx=5, pady=5)

texto_vacio = Label(ventana, font=("Arial 8"), text=" ")
texto_vacio.grid(row=6, column=0, padx=5, pady=1)

#Boton 
boton_iniciar = Button(ventana, text="INICIAR", width=10, height=1, font=("Arial 18"), command = lambda: extraerDatos())
boton_iniciar.grid(row=7, column=0, columnspan=2)

#Banderas
correr_programa = False

def extraerDatos():
    poblacion_inicial = e_poblacionInicial.get()
    poblacion_maxima = e_poblacionMaxima.get()
    precision = e_precision.get()
    intervalo = e_intervalo.get()
    indice = e_indice.get()

    if poblacion_inicial == "" and poblacion_maxima == "" and precision =="" and intervalo == "" and indice =="":
        print("> ERROR: No se han ingresado datos.")
    else:
        validarDatos(poblacion_maxima, poblacion_inicial)

    if correr_programa:
        proceso(poblacion_inicial, poblacion_maxima, precision, intervalo, indice)
    else:
        print("> ERROR: Hay problemas con los datos de entrada, no es posible avanzar con el AG.")

    '''''
    print("Esto tiene Población inicial:",poblacion_inicial)
    print("Esto tiene Población maxima:",poblacion_maxima)
    print("Esto tiene intervalo:",intervalo)
    print("Esto tiene precision:",precision)
    '''''

def validarDatos(poblacion_maxima, poblacion_inicial):
    poblacion1_correcta = False
    poblacion2_correcta = False
    global correr_programa

    if int(poblacion_inicial) <= 0:
        print("> ERROR: El tamaño de la poblacion inicial es incorrecto.")
    else:
        poblacion1_correcta = True
    
    if int(poblacion_maxima) <= 0:
        print("> ERROR: El tamaño de la poblacion maxima es incorrecto.")
    else:
        poblacion2_correcta = True

    if poblacion1_correcta and poblacion2_correcta:
        correr_programa = True


def proceso(poblacion_inicial, poblacion_maxima, precision, intervalo, indice):
    separar_intervalo = intervalo.split(",")
    rango = int(separar_intervalo[1]) - int(separar_intervalo[0])
    
    num_puntos = (rango/float(precision)) + 1
    if num_puntos < 0:
        print(">ERROR: El rango no es válido.")
        messagebox.showinfo(message="La cantidad de puntos es negativa, verificar el intervalo", title="VENTANA DE ERROR")
    else:
        int(num_puntos)
        print("+ Numero de puntos",num_puntos)
        #calcularBits(num_puntos, poblacion_inicial,indice)
        transformarIndividuos(num_puntos, poblacion_inicial, indice, intervalo)

def decimal_a_binario(num_puntos):
    a = num_puntos
    if num_puntos <= 0:
        return "0"
    binario = ""
    while num_puntos > 0:
        residuo = int(num_puntos % 2)
        num_puntos = int(num_puntos / 2)
        binario = str(residuo) + binario
    print("+ Esto es",a,"en binario:",binario)
    return len(binario)

def calcularBits(num_puntos, poblacion_inicial, indice, intervalo):
    individuos = []
    numBits = decimal_a_binario(num_puntos)
    print("+ Se ocuparán:",numBits,"bits")

    if indice == "":
        print("- No se detecto Indice, se usará el intervalo")
        splitIntervalo = intervalo.split(",")
        indiceMin = int(splitIntervalo[0])
        indiceMax = int(splitIntervalo[1])
    else:
        splitIndice = indice.split(",")
        indiceMin = int(splitIndice[0])
        indiceMax = int(splitIndice[1])

    print("+ Indice de:",indiceMin,"a:",indiceMax)
    for i in range(int(poblacion_inicial)):
        randiNum = random.randrange(indiceMin, indiceMax, 1)
        individuos.append(randiNum)
    return individuos, numBits

def transformarIndividuos(num_puntos, poblacion_inicial, indice, intervalo):
    lista_individuos, numBits = calcularBits(num_puntos, poblacion_inicial, indice, intervalo)
    convertidos = []
    print("+ Lista de individuos:",lista_individuos)

    for i in range(len(lista_individuos)):
        if lista_individuos[i] <= 0:
            return "0"
        binario = ""
        while lista_individuos[i] > 0:
            residuo = int(lista_individuos[i] % 2)
            lista_individuos[i] = int(lista_individuos[i] / 2)
            binario = str(residuo) + binario
        convertidos.append(binario)
    print("+ Individuos convertidos:",convertidos)
    print("+ Numero de bits:",numBits)

    #Rellenar bitaje
    for i in range(len(convertidos)):
        if len(convertidos[i]) < numBits:
            print("- Este requiere relleno:",convertidos[i])
            rellenar = convertidos[i]
            relleno = "0"
            diferencia = numBits - len(rellenar)
            for i in range(diferencia):
                if diferencia == 1:
                    arreglado = relleno + rellenar
                    print("+ Numero corregido:",arreglado)
                else:
                    relleno += relleno
                    arreglado = relleno + rellenar
                    print("+ Numero corregido:",arreglado)

    
    


    

    

ventana.mainloop()