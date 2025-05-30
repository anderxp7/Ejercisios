import random

opciones = ["piedra", "papel", "tijeras"]

def jugar():
    usuario = input("Elige piedra, papel o tijeras: ").lower()
    if usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        return
    
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        print("Ganaste")
    else:
        print("Perdiste.")

jugar()

input("Presiona f8 para salir...")