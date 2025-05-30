def maximo(lista):
    return max(lista) if lista else None 
numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"El número más grande es: {maximo(numeros)}")


input("Presiona f8 para salir...")