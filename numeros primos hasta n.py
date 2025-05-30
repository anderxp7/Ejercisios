def numeros_primos_hasta(n):
    primos = []
    for num in range(2, n + 1):
        es_primo = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if es_primo:
            primos.append(num)
    return primos

limite = int(input("Ingrese el valor límite: "))
print(f"Números primos hasta {limite}: {numeros_primos_hasta(limite)}")

input("Presiona Enter para salir...")