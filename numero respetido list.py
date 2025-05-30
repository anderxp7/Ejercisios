def contar_apariciones(lista, numero):
    return lista.count(numero)  
numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
num_buscar = int(input("Ingrese el número que desea contar: "))

print(f"El número {num_buscar} aparece {contar_apariciones(numeros, num_buscar)} veces.")
input("Presiona f8 para salir")