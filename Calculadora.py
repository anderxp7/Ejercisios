def calculadora(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2 if num2 != 0 else "Error: División por cero"
    else:
        return "Operador no válido"

num1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))

resultado = calculadora(num1, num2, operador)
print(f"Resultado: {resultado}")

input("Presiona f8 para salir")