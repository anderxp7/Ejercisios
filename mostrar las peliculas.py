46
cine = {
     "Avengers: Endgame": [False] * 10, 
    "El Padrino": [False] * 10,
    "Interestelar": [False] * 10
    
}

def mostrar_peliculas():
    print("/nPeliculas disponibles:")
    for i, pelicula in enumerate(cine.keys(), 1):

     def reservar_asientos():
      mostrar_peliculas()
    
    try:
        opcion ;int(input("/nSeleccionar una pelicula(numero):")) - 1
        pelicula = list(cine.keys())[opcion]
    except (ValueError, indexError):
        print("seleccion invalida.")
        return
    
        mostrar_asientos(pelicula)
    try:
        asiento = int(input("Selecciona el número de asiento a reservar (1-10): ")) - 1
        if asiento < 0 or asiento >= len(cine[pelicula]):
            print("Número de asiento inválido.")
            return
        if cine[pelicula][asiento]:
            print("Asiento ya reservado.")
        else:
            cine[pelicula][asiento] = True
            print(f"Reserva exitosa en '{pelicula}', asiento {asiento + 1}.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n--- Menú de Reservas ---")
        print("1. Ver películas")
        print("2. Reservar asiento")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_peliculas()
        elif opcion == "2":
            reservar_asientos ()
        elif opcion == "3":
            print("Gracias por usar el sistema de reservas.")
            break
        else:
            print("Opción no válida.")