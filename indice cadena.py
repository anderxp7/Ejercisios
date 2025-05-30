def indice_primera_ocurrencia(lista, elemento):
    return lista.index(elemento) if elemento in lista else None  

numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
num_buscar = int(input("Ingrese el número que desea encontrar: "))

indice = indice_primera_ocurrencia(numeros, num_buscar)

print(f"El índice de la primera ocurrencia de {num_buscar} es: {indice}" if indice is not None else "El número no pertenece a esta lista.")