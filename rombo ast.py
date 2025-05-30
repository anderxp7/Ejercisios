def imprimir_rombo(n):
    for i in range(1, n + 1, 2):  
        print(" " * ((n - i) // 2) + "*" * i)

    for i in range(n - 2, 0, -2):  
        print(" " * ((n - i) // 2) + "*" * i)

tamaño = int(input("Ingrese un número impar para el tamaño del rombo: "))
imprimir_rombo(tamaño)


input("Presiona f8 para salir...")