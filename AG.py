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
e_mutacion = Entry(ventana, font=("Arial 12"))
#e_indice.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
e_mutacion.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

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

texto_indice = Label(ventana, font=("Arial 12"), text="Prob. Mutar:")
texto_indice.grid(row=5, column=0, padx=5, pady=5)

texto_vacio = Label(ventana, font=("Arial 8"), text=" ")
texto_vacio.grid(row=6, column=0, padx=5, pady=1)

#Boton 
boton_iniciar = Button(ventana, text="INICIAR", width=10, height=1, font=("Arial 18"), command = lambda: extraerDatos())
boton_iniciar.grid(row=7, column=0, columnspan=2)

#Variables
correr_programa = False
parejas = []
bitaje = 0
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
        print("> ERROR: El rango no es válido.")
        messagebox.showinfo(message="La cantidad de puntos es negativa, verificar el intervalo", title="VENTANA DE ERROR")
    else:
        int(num_puntos)
        print("+ Numero de puntos",num_puntos)
        #calcularBits(num_puntos, poblacion_inicial, indice, intervalo)
        seleccion(num_puntos, poblacion_inicial, indice, intervalo)
        cruzar()
        #cruzar(num_puntos, poblacion_inicial, indice, intervalo)

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
    individuo = ""
    numBits = decimal_a_binario(num_puntos)
    print("+ Se ocuparán:",numBits,"bits")
    if indice == "":
        #print("- No se detecto Indice, se usará el intervalo")
        splitIntervalo = intervalo.split(",")
        indiceMin = int(splitIntervalo[0])
        indiceMax = int(splitIntervalo[1])
    else:
        splitIndice = indice.split(",")
        indiceMin = int(splitIndice[0])
        indiceMax = int(splitIndice[1])
    print("+ Indice de:",indiceMin,"a:",indiceMax)
    for i in range(int(poblacion_inicial)):
        for i in range(int(numBits)):
            bandera_random = bool(random.randint(0,1))
            if bandera_random:
                individuo += "1"
            else:
                individuo += "0"
        #print("+ Individuo generado:",individuo)
        int(individuo)
        individuos.append(individuo)
        individuo = ""
    return individuos, numBits

def seleccion(num_puntos, poblacion_inicial, indice, intervalo):
    lista_individuos, numBits = calcularBits(num_puntos, poblacion_inicial, indice, intervalo)
    global parejas, bitaje
    bitaje = numBits
    contador_coincidencias = 0
    print("+ Lista de individuos generados:",lista_individuos)

    #Generar turnos
    tamaño_individuos = len(lista_individuos)
    for i in range(tamaño_individuos):
        indice1 = random.randint(0,tamaño_individuos-1)
        indice2 = random.randint(0,tamaño_individuos-1)
        if indice1 == indice2:
            contador_coincidencias +=1
            print("- Coincidieron indices",contador_coincidencias,"veces")
        else:
           # print("+ Individuo",lista_individuos[indice1], "con individuo",lista_individuos[indice2])
            unir = lista_individuos[indice1] + "-" + lista_individuos[indice2]
            parejas.append(unir)

def cruzar():
    global parejas, bitaje
    pm = e_mutacion.get()
    hijosAB1 = []
    hijosAB2 = []
    print("+ Lista de parejas:",parejas)
    print("+ El bitaje es:",bitaje)
    separador = random.randint(1,bitaje)
    #Fragmentar individuos
    while separador == bitaje:
        separador = random.randint(1,bitaje)
    #Cruzar
    print("+ Se separará en el bit:",separador)
    for i in range(len(parejas)):
        prepararParejas = parejas[i].split("-")
        print("+ Preparar parejas:",prepararParejas)
        a = prepararParejas[0]
        b = prepararParejas[1]
        print("+ Cruza AB1:",a[0:separador],"-",b[separador:bitaje])
        ab1 = a[0:separador] + b[separador:bitaje]
        ab2 = b[0:separador] + a[separador:bitaje]
        hijosAB1.append(ab1) #Capturar hijos AB1
        hijosAB2.append(ab2) #Capturar hijos AB2
        print("+ Cruza AB2:",b[0:separador],"-",a[separador:bitaje])
    print("+ Cruzas AB1", hijosAB1)
    print("+ Cruzas AB2", hijosAB2)
    for i in range(len(hijosAB1)):
        prob_mutacion = random.uniform(0,1)
        if prob_mutacion <= float(pm):
            #print("+",hijosAB1[i],"MUTA")
            #print("+ Probabilidad de mutacion:",prob_mutacion)
            mutar_individuo = hijosAB1[i]
            mutacion(mutar_individuo)

def mutacion(mutar):
    guardar = ""
    print("+ Hola acá vamos a mutar a:",mutar)
    for i in range(len(mutar)):
        if mutar[i] == "1":
          muatarString = "".join(mutar[i])
          muatarString = muatarString.replace("1","0")
          guardar = guardar + muatarString

        else:
            if mutar[i] == "0":
                muatarString = "".join(mutar[i])
                muatarString = muatarString.replace("0","1")
                guardar = guardar + muatarString
    print("+ Se ha transformado en:",guardar)

def limpieza():
    pass

def poda():
    pass
        



        









    

ventana.mainloop()