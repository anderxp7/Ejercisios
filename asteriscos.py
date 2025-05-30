def imprimir_y(n):
    for i in range(n):
        if i == 0 or i == n - 1:  
            print("*" * n)
        else: 
            print(" " * (n - i - 1) + "*")

tamaño = int(input("Ingrese el tamaño de la 'y': "))
imprimir_y(tamaño)


input("Presiona f8 para salir...")