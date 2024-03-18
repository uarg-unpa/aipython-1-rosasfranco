#8. Escribir un programa que pida un número entero positivo mayor a 3 y muestre
#por pantalla todos los números impares desde 1 hasta ese número.

num = int(input("Ingrese un número entero positivo mayor a 3: "))

for i in range(1, num + 1, 2):
    print(i)