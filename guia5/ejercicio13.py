#13. Escribir una función que dada una lista de caracteres cuente la cantidad de vocales
#y retorne esa información.
def c_vocales(l_caracteres):
    vocales = 'aeiou'  # Lista de vocales en mayúsculas y minúsculas
    cantidad_vocales = 0
    for caracter in l_caracteres:
        if caracter in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

# Ejemplo de uso de la función
caracteres = ['a', 'b', 'c', 'd', 'e']
cantidad = c_vocales(caracteres)
print(f"La lista contiene {cantidad} vocales.")
