def eliminar_primero(lista):
    return lista[1:] if lista else lista 
numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Lista sin el primer elemento: {eliminar_primero(numeros)}")


input("Presiona f8 para salir...")