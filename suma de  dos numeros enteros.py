def suma_pares_hasta(n):
    return sum(i for i in range(2, n + 1, 2))  

numero = int(input("Ingrese un número entero positivo: "))
suma_pares = suma_pares_hasta(numero)

print(f"La suma de los números pares hasta {numero} es: {suma_pares}")
input("Presiona f8 para salir...")