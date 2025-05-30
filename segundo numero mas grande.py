def segundo_maximo(lista):
    lista_unica = list(set(lista))  
    lista_unica.sort(reverse=True) 
    return lista_unica[1] if len(lista_unica) > 1 else None  
    
numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))

segundo_mayor = segundo_maximo(numeros)

if segundo_mayor is not None:
    print(f"El segundo número más grande es: {segundo_mayor}")
else:
    print("No hay suficiente variedad de números para encontrar el segundo mayor.")
    input("Presiona f8 para salir...")