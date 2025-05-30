def calcular_calorias(peso, altura, edad, sexo, actividad):
    if sexo.lower() == "hombre":
        metabolismo_basal = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
    else:
        metabolismo_basal = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)

    factores_actividad = {
        "sedentario": 1.5,
        "ligero": 1.378,
        "moderado": 1.58,
        "activo": 1.728,
        "muy activo": 2.5
    }

    return metabolismo_basal * factores_actividad.get(actividad.lower(), 1.5)

peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (cm): "))
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (hombre/mujer): ")
actividad = input("Ingrese su nivel de actividad (sedentario, ligero, moderado, activo, muy activo): ")

calorias_diarias = calcular_calorias(peso, altura, edad, sexo, actividad)

print(f"Su consumo diario recomendado es: {calorias_diarias:.2f} kcal.")

input("Presiona f8 para salir...")