from collections import Counter

def numero_mas_repetido(lista):
    contador = Counter(lista)
    return max(contador, key=contador.get)  

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"El número más repetido es: {numero_mas_repetido(numeros)}")
input("Presiona f8 para salir")