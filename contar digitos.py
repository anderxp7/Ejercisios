def contar_digitos(n):
    return len(str(abs(n))) 

numero = int(input("Ingrese un número entero: "))
cantidad_digitos = contar_digitos(numero)

print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
input("Presiona f8 para salir")