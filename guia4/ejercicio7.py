#7. Escribir una función que tome tres números como entrada y retorna el máximo.
def maximo(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3

    return max

# Ejemplo de uso de la función
num1 = 25
num2 = 1
num3 = 18
print("El máximo es:", max(num1, num2, num3))
