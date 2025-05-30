def encontrar_min_max(lista):
    return min(lista), max(lista) 


numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))

minimo, maximo = encontrar_min_max(numeros)

print(f"El mínimo es: {minimo}")
print(f"El máximo es: {maximo}")
input("Presiona f8 para salir...")