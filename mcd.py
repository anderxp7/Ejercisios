def mcd(a, b):
    while b:
        a, b = b, a % b  
    return a

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(f"El mcd de {num1} y {num2} es: {mcd(num1, num2)}")
input("Presiona Enter para salir...")