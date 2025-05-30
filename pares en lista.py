def contar_pares(lista):
    return sum(1 for num in lista if num % 2 == 0) 
numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Cantidad de números pares en la lista: {contar_pares(numeros)}")

input("Presiona f8 para salir...")