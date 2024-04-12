#5. Implementar una función que determine si dado un número este es par o impar.
def par_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

# Ejemplo de uso de la función
num = int(input("Ingrese un número: "))
resultado = par_impar(num)
print(f"El número {num} es {resultado}.")
