#21. Escribir un programa que pida una palabra al usuario y reemplace todas las letras
#"a" por 😃 y muestre el resultado por pantalla.

palabra = input("Ingrese una palabra: ")

p_reemplazada = palabra.replace('a', '😃')

# Mostrar el resultado por pantalla
print("Palabra original:", palabra)
print("Palabra reemplazada:", p_reemplazada)
