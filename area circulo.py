import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)

print(f"El área del círculo con radio {radio} es: {area:.2f}")
input("Presiona f8 para salir")