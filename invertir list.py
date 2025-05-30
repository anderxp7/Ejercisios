def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista)):  
        lista_invertida.append(lista[len(lista) - 1 - i])
    return lista_invertida

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print(f"Lista invertida: {invertir_lista(numeros)}")
input("Presiona f8 para salir...")