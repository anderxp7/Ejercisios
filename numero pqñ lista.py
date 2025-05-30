def minimo(lista):
    return min(lista) if lista else None 
numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"El número más pequeño es: {minimo(numeros)}")


input("Presiona f8 para salir...")