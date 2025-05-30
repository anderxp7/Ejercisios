def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # 
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entero: "))
resultado = "es primo" if es_primo(numero) else "no pertenece a los primos"

print(f"El número {numero} {resultado}.")
input("Presiona f8 para salir...")