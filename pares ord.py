from itertools import combinations

def generar_pares(lista):
    return list(combinations(lista, 2))  

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Todos los pares posibles: {generar_pares(numeros)}")

input("Presiona f8 para salir...")