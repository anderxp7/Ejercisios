def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))
print(f"El factorial de {numero} es: {factorial(numero)}")
input("Presiona f8 para salir")