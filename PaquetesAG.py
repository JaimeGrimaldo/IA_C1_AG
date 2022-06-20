from tkinter import *
import random
from os import system
import pandas as pd
tamanios = [7,11,9,5,7]
preciosPublicos = [100,50,50,100,60]
costosEnvios = [35,28,29,38,31]
categorias = ["A","B","C","D","E"]
cPC = [9,10,9,10,9] #? Cantidad paquetes por categoria

individuo = []
listaPesos = []
listaPrecio = []

def IniciarDatos():
    pPI = 0.30 #? Probabilidad por individuo
    pPG = 0.5 #? Probabilidad por Génotipo
    generaciones = 10
    pI = 10 #? Poblacion inicial
    pM = 10 #? Poblacion máxima
    contenedor = 294
    GenerarIniciales(pI)
    Cruzar(pM)
    Mutacion(pPI, pPG)
    #Calcular(contenedor)
    VerPasados(contenedor)

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
    #print("Individuos generados:",individuo)
    entablar = pd.DataFrame(individuo, columns = ["------Individuos iniciales"])
    print(entablar)
            
def Calcular(contenedor):
    global individuo, categorias, cPC, preciosPublicos, listaPesos, listaPrecio
    recuento = []
    for i in range(len(individuo)):
        contadorPesoA = 0
        contadorPesoB = 0
        contadorPesoC = 0
        contadorPesoD = 0
        contadorPesoE = 0
        pesoGeneral = 0
        pP = 0 #? Precio publico
        contadorA = 0
        contadorB = 0
        contadorC = 0
        contadorD = 0
        contadorE = 0
        pPA, pPB, pPCc, pPD, pPE = 0,0,0,0,0
        for j in range(len(individuo[i])):
            if individuo[i][j] == "A":
                contadorPesoA += 7*cPC[0]
                contadorA += 1
            if individuo[i][j] == "B":
                contadorPesoB += 11*cPC[1]
                contadorB += 1
            if individuo[i][j] == "C":
                contadorPesoC += 9*cPC[2]
                contadorC += 1
            if individuo[i][j] == "D":
                contadorPesoD += 5*cPC[3]
                contadorD += 1
            if individuo[i][j] == "E":
                contadorPesoE += 7*cPC[4]
                contadorE += 1
            pesoGeneral += contadorPesoA + contadorPesoB + contadorPesoC + contadorPesoD + contadorPesoE
            pPA += preciosPublicos[0]*contadorA
            pPB += preciosPublicos[1]*contadorB
            pPCc += preciosPublicos[2]*contadorC
            pPD += preciosPublicos[3]*contadorD
            pPE += preciosPublicos[4]*contadorE
            pP += pPA + pPB + pPCc + pPD + pPE
            if pesoGeneral > contenedor:
               #print("El peso es de:",pesoGeneral,"| Rebasa por:",pesoGeneral-contenedor,"| En el indice:",j)
                #print("Precio publico total:",pP)
                #indicesExcedieron.append(j)
                #listaPesos.append(pesoGeneral)
                #listaPrecio.append(pP)
                prepararDato = (individuo[i])
                #print("Esto tiene linea 107:",individuo[i])
                recortado = prepararDato[0:j]
                recuento.append(recortado)
                break       
    return recuento
        
def VerPasados(contenedor):
    costosTotales = []
    ganancias = []
    ind = Calcular(contenedor)
    global individuo, listaPrecio, listaPesos, cPC, costosEnvios
    for i in range(len(ind)):
        #print("Tenemos esto:",ind[i])
        contador_peso_a, contador_peso_b, contador_peso_c, contador_peso_d, contador_peso_e = 0,0,0,0,0
        precio_publico, peso_paquete = 0,0
        contador_a, contador_b, contador_c, contador_d, contador_e = 0,0,0,0,0
        pPA, pPB, pPCc, pPD, pPE = 0,0,0,0,0
        costoEnvioA, costoEnvioB, costoEnvioC, costoEnvioD, costoEnvioE = 0,0,0,0,0
        for j in range(len(ind[i])):
            if ind[i][j] == "A":
                contador_peso_a += 7*cPC[0]
                contador_a += 1
                costoEnvioA += 1
            if ind[i][j] == "B":
                contador_peso_b += 11*cPC[1]
                contador_b += 1
                costoEnvioB += 1
            if ind[i][j] == "C":
                contador_peso_c += 9*cPC[2]
                contador_c += 1
                costoEnvioC += 1
            if ind[i][j] == "D":
                contador_peso_d += 5*cPC[3]
                contador_d += 1
                costoEnvioD += 1
            if ind[i][j] == "E":
                contador_peso_e += 7*cPC[4]
                contador_e += 1
                costoEnvioE += 1
            peso_paquete += contador_peso_a + contador_peso_b + contador_peso_c + contador_peso_d + contador_peso_e
            pPA += preciosPublicos[0]*contador_a
            pPB += preciosPublicos[1]*contador_b
            pPCc += preciosPublicos[2]*contador_c
            pPD += preciosPublicos[3]*contador_d
            pPE += preciosPublicos[4]*contador_e
            precio_publico += pPA + pPB + pPCc + pPD + pPE


        envioA = costoEnvioA*costosEnvios[0]
        envioB = costoEnvioB*costosEnvios[1]
        envioC = costoEnvioC*costosEnvios[2]
        envioD = costoEnvioD*costosEnvios[3]
        envioE = costoEnvioE*costosEnvios[4]
        costoEnvioTotal = envioA + envioB + envioC + envioD + envioE

        
        costosTotales.append(costoEnvioTotal)
        listaPesos.append(peso_paquete)
        listaPrecio.append(precio_publico)

        ganancia = listaPrecio[i]-costosTotales[i]
        ganancias.append(ganancia)

    print("Paquete:",ind)
    print("Peso de paquete:",listaPesos)
    print("Precio publico:",listaPrecio)
    print("El costo de envio es:",costosTotales)
    print("Las ganancias son:",ganancias)

            

def Cruzar(pM):
    global individuo, categorias
    indicesReferencia = []
    filtrar = []
    hijo1 = ""
    hijo2 = ""
    activarBandera = False
    for i in range(0,len(individuo),2):
        indicesReferencia.clear()
        filtrar.clear()
        cantidadIntercambios = random.randint(5,47)
        print("Se intercambiaran:",cantidadIntercambios)

        for x in range(100):
            indices = random.randint(0,46)
            indicesReferencia.append(indices)
            if len(filtrar) <= cantidadIntercambios:
                for element in indicesReferencia:
                    if element not in filtrar:
                        filtrar.append(element)
        print("Indices:",filtrar)



        paquete1 = individuo[i]
        paquete2 = individuo[i+1]
        auxiliar = list(paquete1)
        auxiliar2 = list(paquete2)
        auxiliar3 = list(paquete1)
        auxiliar4 = list(paquete2)
        for x in range(len(filtrar)):
           #print("Vuelta:",x,"\nTamaño auxiliar:",len(auxiliar),"\nTamaño de filtrar:",len(filtrar))
            indx = filtrar[x]
            #print("(Dentro) Esto tiene indx:",indx)
            auxiliar[indx] = auxiliar2[indx]
            auxiliar4[indx] = auxiliar3[indx]
            hijo1 = "".join(auxiliar)
            hijo2 = "".join(auxiliar4)
        individuo.append(hijo1)
        individuo.append(hijo2)
        #print("Asi quedo el paquete",hijo1, hijo2)

    #print("-- Lista de individuos:",individuo,"\n-- Tamaño de lista individuos:",len(individuo))
    entablar = pd.DataFrame(individuo, columns = ["-----Individuos de cruza"])
    print(entablar)
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
    entablar = pd.DataFrame(individuo, columns = ["----- Individuo mutado"])
    print(entablar)
                    
            

def Poda():
    pass

def SeleccionarMejores():
    pass

        



IniciarDatos()


