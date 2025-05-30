def decimal_a_binario(n):
    return bin(n)[2:] 

numero = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero)

print(f"El número {numero} en binario es: {binario}")
input("Presiona f8 para salir...")