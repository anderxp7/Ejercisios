import random

def lanzar_dado():
    return random.randint(1, 6)  # Generamos un número aleatorio entre 1 y 6

resultado = lanzar_dado()
print(f"El dado ha salido {resultado}.")
input("Presiona Enter para salir...")