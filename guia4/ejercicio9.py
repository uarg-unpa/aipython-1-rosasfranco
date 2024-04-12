#Crear una función que tome un string como parámetro y verifique si es un
#palíndromo. Ejemplo: Arenera, Narran. etc.
def palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar espacios en blanco
    cadena = cadena.lower().replace(" ", "")
    
    # Verificar si la cadena es igual a su reverso
    return cadena == cadena[::-1]

# Ejemplo de uso de la función
cadena1 = "Hola mundo"
cadena2 = "reconocer"


print(cadena1, "es palíndromo:", palindromo(cadena1))
print(cadena2, "es palíndromo:", palindromo(cadena2))

