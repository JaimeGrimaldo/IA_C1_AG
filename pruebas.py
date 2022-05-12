# Archivo para probar algoritmos de internet

def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal


def ver():
    dato = binario_a_decimal("1000101")
    print(dato)

#ver()

def probarLista():
    dato = 0
    lista = []
    for i in range(10):
        dato += 1
        lista.append(dato)

    lista.remove(5)
    print(lista)
probarLista()