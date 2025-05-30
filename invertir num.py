def invertir_numero(n):
    return int(str(n)[::-1])

numero = int(input("Ingrese un número entero: "))
numero_invertido = invertir_numero(numero)

print(f"El número invertido es: {numero_invertido}")
input("Presiona f8 para salir")