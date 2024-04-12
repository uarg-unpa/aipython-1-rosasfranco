#6. Crear una función que calcule el factorial de un número.

def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

# Ejemplo de uso de la función
numero = int(input("Ingrese un número para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}.")
