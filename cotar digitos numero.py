def contar_digitos(numero):
    return len(str(abs(numero))) 

numero = int(input("Ingrese un número: "))
print(f"El número tiene {contar_digitos(numero)} dígitos.")

input("Presiona f8 para salir")