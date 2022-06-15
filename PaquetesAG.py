from tkinter import *
import random

tamanios = [7,11,9,5,7]
preciosPublicos = [100,50,50,100,60]
costosEnvios = [35,28,29,38,31]
categorias = ["A","B","C","D","E"]
cPC = [9,10,9,10,9] #? Cantidad paquetes por categoria

individuo = []

def IniciarDatos():
    pPI = 0.30 #? Probabilidad por individuo
    pPG = 0.5 #? Probabilidad por Génotipo
    generaciones = 10
    pI = 4 #? Poblacion inicial
    pM = 10 #? Poblacion máxima
    contenedor = 294
    GenerarIniciales(pI)
    #Calcular(contenedor)
    Cruzar(pM)
    Mutacion(pPI, pPG)

def GenerarIniciales(pI):
    global individuo, categorias, cPC
    aux1 = categorias[0]*cPC[0]
    aux2 = categorias[1]*cPC[1]
    aux3 = categorias[2]*cPC[2]
    aux4 = categorias[3]*cPC[3]
    aux5 = categorias[4]*cPC[4]
    auxT = aux1+aux2+aux3+aux4+aux5
    #print("Aux:",auxT)
    print("No. Paquetes por individuo:",len(auxT))

    iI = "" #? Individuo inicial
    for i in range(pI):
        iI = ""
        for j in range(len(auxT)):
            nR = random.randint(1,5) #? Número random
            if nR == 1:
                iI += categorias[0]
            if nR == 2:
                iI += categorias[1]
            if nR == 3:
                iI += categorias[2]
            if nR == 4:
                iI += categorias[3]
            if nR == 5:
                iI += categorias[4]
        individuo.append(iI)
    print("Individuos generados:",individuo)
            
def Calcular(contenedor):
    global individuo, categorias
    for i in range(len(individuo)):
        contadorPesoA = 0
        contadorPesoB = 0
        contadorPesoC = 0
        contadorPesoD = 0
        contadorPesoE = 0
        pesoGeneral = 0
        for j in range(len(individuo[i])):
            #print("----",individuo[i][j])
            if individuo[i][j] == "A":
                contadorPesoA += 7
            if individuo[i][j] == "B":
                contadorPesoB += 11
            if individuo[i][j] == "C":
                contadorPesoC += 9
            if individuo[i][j] == "D":
                contadorPesoD += 5
            if individuo[i][j] == "E":
                contadorPesoE += 7
            pesoGeneral += contadorPesoA + contadorPesoB + contadorPesoC + contadorPesoD + contadorPesoE
            if pesoGeneral > contenedor:
                print("El peso es de:",pesoGeneral,"| Rebasa por:",pesoGeneral-contenedor,"| En el indice:",j)
                break
        
def Cruzar(pM):
    global individuo, categorias
    indicesReferencia = []
    hijo1 = ""
    hijo2 = ""
    for i in range(0,len(individuo),2):
        indicesReferencia.clear()
        cantidadIntercambios = random.randint(0,47)
        print("Se intercambiaran:",cantidadIntercambios)

        for x in range(cantidadIntercambios):
            indices = random.randint(0,47)
            indicesReferencia.append(indices)
        indicesReferencia = list(set(indicesReferencia))
        print("Indices:",indicesReferencia)

        paquete1 = individuo[i]
        paquete2 = individuo[i+1]
        auxiliar = list(paquete1)
        auxiliar2 = list(paquete2)
        auxiliar3 = list(paquete1)
        auxiliar4 = list(paquete2)
        for i in range(len(individuo)):
            indx = indicesReferencia[i]
            #print("-- Esto tiene indx:",indx)
            #print("-- Esto tiene Aux:",auxiliar)
            #print("-- Esto tiene Aux2:",auxiliar4)
            auxiliar[indx] = auxiliar2[indx]
            auxiliar4[indx] = auxiliar3[indx]
            hijo1 = "".join(auxiliar)
            hijo2 = "".join(auxiliar4)
            individuo.append(hijo1)
            individuo.append(hijo2)
        #print("Asi quedo el paquete",hijo1, hijo2)
    print("-- Lista de individuos:",individuo)
    if len(individuo) > pM:
        pass #Entra poda
    

def Mutacion(pPI, pPG):
    global individuo
    mutacion = ""
    for i in range(len(individuo)):
        prob1 = random.random()
        if prob1 <= pPI:
            print("-- Vamos a mutar al del:",i)
            sujeto = individuo[i]
            auxSujeto = list(sujeto)
            for x in range(len(sujeto)):
                prob2 = random.random()

                if prob2 <= pPG:
                    #print("-- Mutamos Gen")
                    indice1 = 0
                    indice2 = 0
                    while indice1 == indice2:
                        indice1 = random.randint(0,46)
                        indice2 = random.randint(0,46)
                    #print("-- Tamaño de auxSujeto:",len(auxSujeto))
                    gen1 = auxSujeto[indice1]
                    gen2 = auxSujeto[indice2]
                    auxSujeto[indice1] = gen2
                    auxSujeto[indice2] = gen1
                    mutacion = "".join(auxSujeto)
            individuo[i] = mutacion
    print("-- Mutados",individuo)
                    
            

def Poda():
    pass

def SeleccionarMejores():
    pass

        



IniciarDatos()


