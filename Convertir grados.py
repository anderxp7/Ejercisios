def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"La temperatura en Fahrenheit es: {fahrenheit}°F")
input("Presiona Enter para salir...")