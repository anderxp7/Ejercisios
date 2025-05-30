def imprimir_triangulo_derecha(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)  

altura = int(input("Ingrese la altura del triángulo: "))
imprimir_triangulo_derecha(altura)


input("Presiona Enter para salir...")