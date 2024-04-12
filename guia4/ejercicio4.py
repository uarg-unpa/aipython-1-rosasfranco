#4. Escribir una función que tome un número como entrada e imprima la tabla de
#multiplicar del 1 al 10, con el siguiente formato.

#4 x 1 = 4
#............
#............

def tabla_m(num):
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")

# Ejemplo de uso de la función
num = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_m(num)
