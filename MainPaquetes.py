import random
import pandas as pd
tamanios = [7,11,9,5,7]
preciosPublicos = [100,50,50,100,60]
costosEnvios = [35,28,29,38,31]
categorias = ["A","B","C","D","E"]
cPC = [9,10,9,10,9]

class Paquete:
    def __init__(self,id,paquete,peso,precioPublico,costoEnvio,ganancia):
        self.id = id
        self.peso = peso
        self.paquete = paquete
        self.precioPublico = precioPublico
        self.costoEnvio = costoEnvio
        self.ganancia = ganancia

    def __repr__(self):
        return f"ID: {self.id} - Paquete: {self.paquete} - Peso: {self.peso} - Ganancia: {self.ganancia}"

    def get_paquete(self):
        return self.paquete
    def set_paquete(self, x):
        self.paquete = x

    def get_ganancia(self):
        return self.ganancia
    def set_ganancia(self, x):
        self.ganancia = x
    
    def get_id(self):
        return self.id
    def get_peso(self):
        return self.peso
    def get_precioPublico(self):
        return self.precioPublico
    def get_costoEnvio(self):
        return self.costoEnvio


def datosEntrada():
    tamanioPoblacionInicial = 4
    tamanioPoblacionMaxima = 50
    cantidadGeneraciones = 5
    probMutacionIndividuo = 0.20
    probMutacionGenotipo = 0.12
    contenedor = 294
    return tamanioPoblacionInicial, tamanioPoblacionMaxima, cantidadGeneraciones, probMutacionIndividuo, probMutacionGenotipo, contenedor

idPaquetes = 0
listaPaquetes = []
listaPaquetesAlmacen = []
checkpoint = 0
def programa():
    global idPaquetes, listaPaquetes, checkpoint
    poblacionInicial, poblacionMaxima, generaciones, probMutacion, probMutacionGen, contenedor = datosEntrada()
    global categorias, cPC
    individuos = []
    aux1 = categorias[0]*cPC[0]
    aux2 = categorias[1]*cPC[1]
    aux3 = categorias[2]*cPC[2]
    aux4 = categorias[3]*cPC[3]
    aux5 = categorias[4]*cPC[4]
    auxT = aux1+aux2+aux3+aux4+aux5
    print("No. Paquetes por individuo:",len(auxT))
    #? ------ GENERAMOS INDIVIDUOS INICIALES ---------
    armarIndividuo = ""
    for i in range(poblacionInicial):
        armarIndividuo = ""
        for j in range(len(auxT)):
            selectorRandom = random.randint(1,5)
            if selectorRandom == 1:
                armarIndividuo += categorias[0]
            if selectorRandom == 2:
                armarIndividuo += categorias[1]
            if selectorRandom == 3:
                armarIndividuo += categorias[2]
            if selectorRandom == 4:
                armarIndividuo += categorias[3]
            if selectorRandom == 5:
                armarIndividuo += categorias[4]
        individuos.append(armarIndividuo)
    entablar = pd.DataFrame(individuos, columns = ["------Individuos iniciales"])
    print(entablar)

    #? ----- COMENZAMOS CRUZA -----
    for ciclar in range(generaciones):
        hijo1 = ""
        hijo2 = ""
        listaIndices = []
        filtroIndices = []
        for i in range(0,len(individuos),2):
            hijo1 = ""
            hijo2 = ""
            listaIndices.clear()
            filtroIndices.clear()
            cantidadIntercambios = random.randint(10,47)
            for j in range(1000):
                indices = random.randint(0,46)
                listaIndices.append(indices)
                if len(filtroIndices) <= cantidadIntercambios:
                    for element in listaIndices:
                        if element not in filtroIndices:
                            filtroIndices.append(element)
            #print("Indices a intercambiar por parejas:",filtroIndices, cantidadIntercambios, (len(filtroIndices))-1)
            paquete1 = individuos[i]
            paquete2 = individuos[i+1]
            auxiliar = list(paquete1)
            auxiliar2 = list(paquete2)
            auxiliar3 = list(paquete1)
            auxiliar4 = list(paquete2)

            for x in range(len(filtroIndices)):
                indice = filtroIndices[x]
                auxiliar[indice] = auxiliar2[indice]
                auxiliar4[indice] = auxiliar3[indice]
                hijo1 = "".join(auxiliar)
                hijo2 = "".join(auxiliar4)
            individuos.append(hijo1)
            individuos.append(hijo2)
        print("\n")
        entablar = pd.DataFrame(individuos, columns = ["------Individuos con cruza"])
        print(entablar)

        #? ----- COMENZAMOS MUTACION -----
        individuoMutado = ""
        for i in range(len(individuos)):
            probabilidad1 = random.random()
            if probabilidad1 <= probMutacion:
                experimento = individuos[i]
                auxExperimento = list(experimento)
                for x in range(len(experimento)):
                    probabilidad2 = random.random()
                    if probabilidad2 <= probMutacionGen:
                        indice1 = 0
                        indice2 = 0
                        while indice1 == indice2:
                            indice1 = random.randint(0,46)
                            indice2 = random.randint(0,46)
                        gen1 = auxExperimento[indice1]
                        gen2 = auxExperimento[indice2]
                        auxExperimento[indice1] = gen2
                        auxExperimento[indice2] = gen1
                        individuoMutado = "".join(auxExperimento)
                individuos.append(individuoMutado)
        print("\n")
        entablar = pd.DataFrame(individuos, columns = ["------ Individuos con mutación"])
        print(entablar)

        #? ----- CALCULOS ------

        for i in range(len(individuos)):
            recortePaquete = ""
            contadorPesoA = 0
            contadorPesoB = 0
            contadorPesoC = 0
            contadorPesoD = 0
            contadorPesoE = 0
            pesoGeneral = 0
            pP = 0 #pP = precio publico
            contadorA = 0
            contadorB = 0
            contadorC = 0
            contadorD = 0
            contadorE = 0
            pPA, pPB, pPCc, pPD, pPE = 0,0,0,0,0
            for j in range(len(individuos[i])):
                if individuos[i][j] == "A":
                    contadorPesoA += tamanios[0]
                    recortePaquete += "A"
                if individuos[i][j] == "B":
                    contadorPesoA += tamanios[1]
                    recortePaquete += "B"
                if individuos[i][j] == "C":
                    contadorPesoA += tamanios[2]
                    recortePaquete += "C"
                if individuos[i][j] == "D":
                    contadorPesoA += tamanios[3]
                    recortePaquete += "D"
                if individuos[i][j] == "E":
                    contadorPesoA += tamanios[4]
                    recortePaquete += "E"

                pesoGeneral += contadorPesoA + contadorPesoB + contadorPesoC + contadorPesoD + contadorPesoE


                if pesoGeneral > contenedor:
                    quitarExtra = recortePaquete[:-1]
                    #print(f"Asi queda el recorte de paquete: {recortePaquete} Con peso: {pesoGeneral}")
                    contadorPesoA = 0
                    contadorPesoB = 0
                    contadorPesoC = 0
                    contadorPesoD = 0
                    contadorPesoE = 0
                    pesoGeneral = 0
                    contadorA = 0
                    contadorB = 0
                    contadorC = 0
                    contadorD = 0
                    contadorE = 0
                    costoA, costoB, costoC, costoD, costoE = 0,0,0,0,0
                    pPA, pPB, pPCc, pPD, pPE = 0,0,0,0,0
                    for k in range(len(quitarExtra)):
                        if quitarExtra[k] == "A":
                            contadorPesoA += tamanios[0]
                            contadorA += 1
                        if quitarExtra[k] == "B":
                            contadorPesoA += tamanios[1]
                            contadorB += 1
                        if quitarExtra[k] == "C":
                            contadorPesoA += tamanios[2]
                            contadorC += 1
                        if quitarExtra[k] == "D":
                            contadorPesoA += tamanios[3]
                            contadorD += 1
                        if quitarExtra[k] == "E":
                            contadorPesoA += tamanios[4]
                            contadorE += 1
                        pesoGeneral += contadorPesoA + contadorPesoB + contadorPesoC + contadorPesoD + contadorPesoE
                        pPA = preciosPublicos[0]*contadorA
                        pPB = preciosPublicos[1]*contadorB
                        pPCc = preciosPublicos[2]*contadorC
                        pPD = preciosPublicos[3]*contadorD
                        pPE = preciosPublicos[4]*contadorE
                        pP = pPA + pPB + pPCc + pPD + pPE

                        costoA = costosEnvios[0] * contadorA
                        costoB = costosEnvios[1] * contadorB
                        costoC = costosEnvios[2] * contadorC
                        costoD = costosEnvios[3] * contadorD
                        costoE = costosEnvios[4] * contadorE
                        costoEnvioTotal = costoA + costoB + costoC + costoD + costoE
                        ganancia = pP - costoEnvioTotal
                    #print(f"Paquete corregido: {quitarExtra} Con peso corregido: {pesoGeneral} Con precio publico {pP} - Costo envio: {costoEnvioTotal} - Ganancia: {ganancia}")
                    #print("\n")
                    paquete = Paquete(idPaquetes,quitarExtra,pesoGeneral,pP,costoEnvioTotal,ganancia)
                    listaPaquetes.append(paquete)
                    idPaquetes += 1
                    break
        #print(repr(listaPaquetes))
    print(f"Otorgando al back")


    for ask in range(checkpoint,len(listaPaquetes),1):
        listaPaquetesAlmacen.append(listaPaquetes[ask])
    checkpoint = len(listaPaquetesAlmacen)
    listaPaquetes.clear()

    #? ---- FILTRAR MEJORES --- 
    listaPaquetesAlmacen.sort(key = lambda x:x.ganancia)
    #for abr in range(len(listaPaquetesAlmacen)):
        #print(repr(listaPaquetesAlmacen[abr]))

    #? ---- PODA ---
    print("\n--- Mejores individuos ---")
    mejores = []
    seguir = True
    contadorAuxiliar = 1
    if len(listaPaquetesAlmacen) > poblacionMaxima:
        while seguir:
            mejores.append(listaPaquetesAlmacen[-1])
            listaPaquetesAlmacen.pop()
            contadorAuxiliar += 1
            if contadorAuxiliar == poblacionMaxima:
                seguir = False
    mejores.sort(key = lambda x:x.ganancia)
    for i in range(len(mejores)):
        print(repr(mejores[i]))
programa()
