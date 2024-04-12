#3. Crear una función que tome un nombre como parámetro y retorna un mensaje
#creativo.
def mensaje(nombre):
    mensaje = f"Hola mi nombre es: {nombre}! :D."
    return mensaje

# Ejemplo de uso de la función
nombre = input("Ingrese su nombre: ")
resultado = mensaje(nombre)
print(resultado)
