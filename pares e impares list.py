def contar_pares_impares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = len(lista) - pares
    return pares, impares


numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))

pares, impares = contar_pares_impares(numeros)

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
input("Presiona f8 para salir")