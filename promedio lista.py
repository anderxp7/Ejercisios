def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else 0  


numeros = list(map(float, input("Ingrese números separados por espacios: ").split()))

promedio = calcular_promedio(numeros)

print(f"El promedio de los números ingresados es: {promedio:.2f}")
input("Presiona f8 para salir...")
