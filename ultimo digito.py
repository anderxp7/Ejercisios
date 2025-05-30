def ultimo_digito(numero):
    return abs(numero) % 10  

numero = int(input("Ingrese un número: "))
print(f"El último dígito es: {ultimo_digito(numero)}")

input("Presiona f8 para salir...")