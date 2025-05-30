import math

def calcular_mcd(a, b, c):
    return math.gcd(math.gcd(a, b), c) 

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

print(f"El mcd de {num1}, {num2} y {num3} es: {calcular_mcd(num1, num2, num3)}")

input("Presiona f8 para salir...")