47
estudiantes = {}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in estudiantes:
        print("El estudiante ya existe.")
    else:
        estudiantes[nombre] = {}
        print(f"Estudiante '{nombre}' agregado.")

def agregar_nota():
    nombre = input("Nombre del estudiante: ")
    if nombre not in estudiantes:
        print("Estudiante no encontrado.")
        return

    materia = input("Nombre de la materia: ")
    try:
        nota = float(input("Nota obtenida (0-10): "))
        if 0 <= nota <= 10:
            estudiantes[nombre][materia] = nota
            print(f"Nota registrada para {nombre} en {materia}.")
        else:
            print("La nota debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada inválida para la nota.")

def mostrar_notas():
    for nombre, materias in estudiantes.items():
        print(f"\nEstudiante: {nombre}")
        if materias:
            for materia, nota in materias.items():
                print(f"  {materia}: {nota}")
        else:
            print("  No hay notas registradas.")

def calcular_promedio():
    nombre = input("Nombre del estudiante: ")
    if nombre not in estudiantes:
        print("Estudiante no encontrado.")
        return

    notas = list(estudiantes[nombre].values())
    if notas:
        promedio = sum(notas) / len(notas)
        print(f"Promedio de {nombre}: {promedio:.2f}")
    else:
        print("No hay notas registradas para este estudiante.")

def menu():
    while True:
        print("\n--- Sistema de Notas ---")
        print("1. Agregar estudiante")
        print("2. Agregar nota")
        print("3. Mostrar notas")
        print("4. Calcular promedio")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_nota()
        elif opcion == "3":
            mostrar_notas()
        elif opcion == "4":
            calcular_promedio()
        elif opcion == "5":
            print("Gracias por usar el sistema de notas.")
            break
        else:
            print("Opción no válida.")


menu()