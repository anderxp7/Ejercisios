def imprimir_triangulo(n):
    for i in range(1, n + 1):
        print("*" * i) 

altura = int(input("Ingrese la altura del triángulo: "))
imprimir_triangulo(altura)


input("Presiona f8 para salir...")