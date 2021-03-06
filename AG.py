from cProfile import label
from code import interact
from tkinter import *
from tkinter import font
import random
from tkinter import messagebox
import math
import matplotlib.pyplot as plt

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

e_indice1 = Entry(ventana, font=("Arial 12"))
e_mutacion = Entry(ventana, font=("Arial 12"))
e_generaciones = Entry(ventana, font=("Arial 12"))
#e_indice.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
e_mutacion.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
e_indice1.grid(row=6, column=1, columnspan=1, padx=5, pady=5)
e_generaciones.grid(row=7, column=1, columnspan=1, padx=5, pady=5)



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

texto_indice1 = Label(ventana, font=("Arial 12"), text="IE:")
texto_indice1.grid(row=6, column=0, padx=5, pady=5)

texto_generaciones = Label(ventana, font=("Arial 12"), text="Generaciones:")
texto_generaciones.grid(row=7, column=0, padx=5, pady=5)

texto_vacio = Label(ventana, font=("Arial 8"), text=" ")
texto_vacio.grid(row=8, column=0, padx=5, pady=1)

#Boton 
boton_iniciar = Button(ventana, text="INICIAR", width=10, height=1, font=("Arial 18"), command = lambda: extraerDatos())
boton_iniciar.grid(row=9, column=0, columnspan=2)

#Variables globales
correr_programa = False
parejas = []
bitaje = 0
hijosMutados = []
hijosAB1 = []
hijosAB2 = []
individuos = []
mejor = []
peor = []
def extraerDatos():
    generaciones = e_generaciones.get()
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
        for i in range(int(generaciones)):
            proceso(poblacion_inicial, poblacion_maxima, precision, intervalo, indice)
        graficar()
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
    global individuos
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
    individuos = list(set(individuos))
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
    global parejas, bitaje, hijosMutados, hijosAB1, hijosAB2
    pm = e_mutacion.get()

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
    for i in range(len(hijosAB2)):
        prob_mutacion = random.uniform(0,1)
        if prob_mutacion <= float(pm):
            #print("+",hijosAB1[i],"MUTA")
            #print("+ Probabilidad de mutacion:",prob_mutacion)
            mutar_individuo = hijosAB2[i]
            mutacion(mutar_individuo)
    print("Estos son todos los mutados:",hijosMutados)
    hijosAB1 = list(set(hijosAB1))
    hijosAB2 = list(set(hijosAB2))
    limpieza()
    calcular()

def mutacion(mutar):
    global hijosMutados
    guardar = ""
    bandera = False
    print("+ Hola acá vamos a mutar a:",mutar)
    
    for i in range(len(mutar)):
        prob_mutacion = random.uniform(0,1)
        prob_mutaconG = random.uniform(0,1)
        if prob_mutaconG <= prob_mutacion:
            if mutar[i] == "1":
                muatarString = "".join(mutar[i])
                muatarString = muatarString.replace("1","0")
                guardar = guardar + muatarString
            else:
                if mutar[i] == "0":
                    muatarString = "".join(mutar[i])
                    muatarString = muatarString.replace("0","1")
                    guardar = guardar + muatarString
        else:
            if mutar[i] == "1":
                muatarString = "".join(mutar[i])
                muatarString = muatarString.replace("1","1")
                guardar = guardar + muatarString
            else:
                if mutar[i] == "0":
                    muatarString = "".join(mutar[i])
                    muatarString = muatarString.replace("0","0")
                    guardar = guardar + muatarString
    print("+ Se ha transformado en:",guardar)
    hijosMutados.append(guardar)
    hijosMutados = list(set(hijosMutados))

def limpieza():
    global hijosMutados, hijosAB1, hijosAB2, individuos
    
    iE = e_indice1.get()

    diferenciar_indice = iE.split(",")
    iE1 = int(diferenciar_indice[0])
    iE2 = int(diferenciar_indice[1])
    print("De estos tipos son",type(iE2),type(iE1))
    print("Esto vale iE1:",iE1,"\nEsto vale IE2",iE2)

    print("\n")
    print("+ Individuos iniciales:",individuos)
    print("+ Hijos AB1:",hijosAB1)
    print("+ Hijos AB2:",hijosAB2)
    print("+ Mutados:",hijosMutados)

    for i in range(len(hijosMutados)-1,-1,-1):
        numDecimal = binario_a_decimal(hijosMutados[i])
        if numDecimal < iE1:
            print("- El numero",hijosMutados[i],"excede el limite con decimal",numDecimal)
            hijosMutados.pop(i)
        if numDecimal > iE2:
            print("- El numero",hijosMutados[i],"excede el limite con decimal",numDecimal)
            hijosMutados.pop(i)

    for i in range(len(individuos)-1,-1,-1):
        numDecimal = binario_a_decimal(individuos[i])
        if numDecimal < iE1:
            print("- El numero",individuos[i],"excede el limite con decimal",numDecimal)
            individuos.pop(i)
        if numDecimal > iE2:
            print("- El numero",individuos[i],"excede el limite con decimal",numDecimal)
            individuos.pop(i)
    

    for i in range(len(hijosAB1)-1,-1,-1):
        numDecimal = binario_a_decimal(hijosAB1[i])
        if numDecimal < iE1:
            print("- El numero",hijosAB1[i],"excede el limite con decimal",numDecimal)
            hijosAB1.pop(i)
        if numDecimal > iE2:
            print("- El numero",hijosAB1[i],"excede el limite con decimal",numDecimal)
            hijosAB1.pop(i)

    for i in range(len(hijosAB2)-1,-1,-1):
        numDecimal = binario_a_decimal(hijosAB2[i])
        if numDecimal < iE1:
            print("- El numero",hijosAB2[i],"excede el limite con decimal",numDecimal)
            hijosAB2.pop(i)
        if numDecimal > iE2:
            print("- El numero",hijosAB2[i],"excede el limite con decimal",numDecimal)
            hijosAB2.pop(i)

    print("\n")
    print("+ Hijos limpios AB1:",hijosAB1)
    print("+ Hijos limpios AB2:",hijosAB2)
    print("+ Mutados limpios:",hijosMutados)


def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal



def formula(valor):
    precision = e_precision.get()
    intervalo = e_intervalo.get()
    separarInervalo = intervalo.split(",")
    x1 = int(separarInervalo[0])
    x2 = int(separarInervalo[1])
    minimo = 0
    if x1 < x2:
        minimo = x1
    else:
        minimo = x2
    x = (valor * float(precision))
    xi = minimo + x
    return xi

def funcion(xs, xHijosAB1, xHijosAB2, xMutados):
    global individuos, hijosAB1, hijosAB2, hijosMutados
    cantidadIndividuos = len(xs)
    cantidadHijosAB1 = len(hijosAB1)
    cantidadHijosAB2 = len(hijosAB2)
    cantidadMutaddos = len(hijosMutados)
    poblacionTotal = cantidadIndividuos + cantidadHijosAB1 + cantidadHijosAB2 + cantidadMutaddos
    pMaxima = e_poblacionMaxima.get()
    pMaxima = int(pMaxima)
    global mejor, peor
    ap = []
    apAB1 = []
    apAB2 = []
    apMutados = []
    #0.25Cos(0.50x)Sen(0.50x) + 0.50Cos(0.50x)
    for i in range(len(xs)):
        x = xs[i]
        multi = 0.50 * x
        cose = math.cos(multi)
        seno = math.sin(multi)
        sen_cos = seno * cose
        multi2 = sen_cos * 0.25
        cose2 = cose * 0.50
        y = multi2 + cose2
        #print("+ Ap individuos:",y)
        ap.append(y)

    for i in range(len(xHijosAB1)):
        x = xHijosAB1[i]
        multi = 0.50 * x
        cose = math.cos(multi)
        seno = math.sin(multi)
        sen_cos = seno * cose
        multi2 = sen_cos * 0.25
        cose2 = cose * 0.50
        y = multi2 + cose2
        #print("+ Ap individuos:",y)
        apAB1.append(y)

    for i in range(len(xHijosAB2)):
        x = xHijosAB2[i]
        multi = 0.50 * x
        cose = math.cos(multi)
        seno = math.sin(multi)
        sen_cos = seno * cose
        multi2 = sen_cos * 0.25
        cose2 = cose * 0.50
        y = multi2 + cose2
        #print("+ Ap individuos:",y)
        apAB2.append(y)
        
    for i in range(len(xMutados)):
        x = xMutados[i]
        multi = 0.50 * x
        cose = math.cos(multi)
        seno = math.sin(multi)
        sen_cos = seno * cose
        multi2 = sen_cos * 0.25
        cose2 = cose * 0.50
        y = multi2 + cose2
        #print("+ Ap individuos:",y)
        apMutados.append(y)

    minimoAptitud = 0
    peorA = 0
    for i in range(len(ap)):
        if i == 0:
            peorA = ap[i]
            minimoAptitud = ap[i]
        else:
            if peorA < ap[i]:
                peor.append(peorA)
                mejor.append(ap[i])
            else: 
                mejor.append(peorA)
                peor.append(ap[i])

            if minimoAptitud > ap[i]:
                minimoAptitud = ap[i]
    
    if poblacionTotal > pMaxima:
        poda()
            
    mejor.sort()
    peor.sort()
    print("+ Mejores:",mejor,"\n\n+ Peores:",peor)
    print("+ Individuos actualizados:",individuos,"\n+ Hijos AB1 actualizados:",hijosAB1, "\n+ Hijos AB2",hijosAB2, "\n+ Mutados: ",hijosMutados)





def calcular(): #Sacar aptitudes/Fitness de cada individuo
    global individuos, hijosAB1, hijosAB2, hijosMutados
    xs = []
    xHijosAB1 = []
    xHijosAB2 = []
    xMutados = []

    for i in range(len(individuos)):
        convertirDecimal = binario_a_decimal(individuos[i])
        aptitud = formula(convertirDecimal)
        xs.append(aptitud)
    print("\n+ Aptitudes de individuos:",xs)

    for i in range(len(hijosAB1)):
        convertirDecimal = binario_a_decimal(hijosAB1[i])
        aptitud = formula(convertirDecimal)
        xHijosAB1.append(aptitud)
    print("+ Aptitudes de hijos AB1:",xHijosAB1)

    for i in range(len(hijosAB2)):
        convertirDecimal = binario_a_decimal(hijosAB2[i])
        aptitud = formula(convertirDecimal)
        xHijosAB2.append(aptitud)
    print("+ Aptitudes de hijos AB2:",xHijosAB2)

    for i in range(len(hijosMutados)):
        convertirDecimal = binario_a_decimal(hijosMutados[i])
        aptitud = formula(convertirDecimal)
        xMutados.append(aptitud)
    print("+ Aptitudes de hijos mutados:",xMutados)

    funcion(xs, xHijosAB1, xHijosAB2, xMutados) 

def calculoDescriptivo(individuo): #Recalcular para buscar individuos no adecuados
    convertirDecimal = binario_a_decimal(individuo)
    aptitud = formula(convertirDecimal)
    #print("\n+ Aptitud:",aptitud)
    return aptitud

def funcionIndividual(x):
    multi = 0.50 * x
    cose = math.cos(multi)
    seno = math.sin(multi)
    sen_cos = seno * cose
    multi2 = sen_cos * 0.25
    cose2 = cose * 0.50
    y = multi2 + cose2
    print("+ Resultado Y:",y)
    return y


def poda():
    for i in range(len(individuos)-1,-1,-1):
        aptitudIndividuos = calculoDescriptivo(individuos[i])
        fitnessIndividuos = funcionIndividual(aptitudIndividuos)
        for j in range(len(peor)):
            if fitnessIndividuos == peor[j]:
                print("Se sacara al individuo:",individuos[i])
                individuos.pop(i)
                break

    for i in range(len(hijosAB1)-1,-1,-1):
        aptitudIndividuos = calculoDescriptivo(hijosAB1[i])
        fitnessIndividuos = funcionIndividual(aptitudIndividuos)
        for j in range(len(peor)):
            if fitnessIndividuos == peor[j]:
                print("Se sacara al individuo:",hijosAB1[i])
                hijosAB1.pop(i)
                break

    for i in range(len(hijosAB2)-1,-1,-1):
        aptitudIndividuos = calculoDescriptivo(hijosAB2[i])
        fitnessIndividuos = funcionIndividual(aptitudIndividuos)
        for j in range(len(peor)):
            if fitnessIndividuos == peor[j]:
                print("Se sacara al individuo:",hijosAB2[i])
                hijosAB2.pop(i)
                break

    for i in range(len(hijosMutados)-1,-1,-1):
        aptitudIndividuos = calculoDescriptivo(hijosMutados[i])
        fitnessIndividuos = funcionIndividual(aptitudIndividuos)
        for j in range(len(peor)):
            if fitnessIndividuos == peor[j]:
                print("Se sacara al individuo:",hijosMutados[i])
                hijosMutados.pop(i)
                break
    


mejoresGen = []
peoresGen = []

  
def graficar():
    global mejor, peor
    plt.title("Grafica individuos")
    plt.plot(mejor,label="Mejor",color="green")
    plt.xlabel("Generaciones")
    plt.ylabel("Evolución de aptitudes")
    plt.ioff()
    plt.ion()
    plt.plot(peor,label="Peor",color="red")
    plt.ioff()
    plt.legend()
    plt.show()





    

ventana.mainloop()