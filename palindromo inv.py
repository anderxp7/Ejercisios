def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  
    return palabra == palabra[::-1]  

texto = input("Ingrese una palabra o frase: ")
resultado = "es un palíndromo" if es_palindromo(texto) else "no es un palíndromo"

print(f'"{texto}" {resultado}.')
input("Presiona Enter para salir...")