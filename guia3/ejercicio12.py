#12. Escribir un programa que pida un número natural N al usuario e imprima por
#pantalla la suma de los números naturales de 1 hasta N.
#Por ejemplo para N = 5, la salida debe ser:
#1 + 2 + 3 + 4 + 5 = 15

N = int(input("Ingrese un numero natural: "))
suma = 0
for i in range(1, N + 1):
    suma =suma + i
print(f"La suma de los números naturales hasta {N} es igual a: {suma}")