def suma_numeros_naturales(n):
    return n * (n + 1) // 2 
numero = int(input("Ingrese un número entero positivo: "))
if numero >= 0:
    print(f"La suma de los primeros {numero} números naturales es: {suma_numeros_naturales(numero)}")
else:
    print("Por favor, ingrese un número positivo.")
    input("Presiona f8 para salir...")