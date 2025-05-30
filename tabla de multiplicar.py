numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    input("Presiona Enter para salir...")