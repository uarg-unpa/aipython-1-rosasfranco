#14.Escribir un programa que recibe como entrada desde el usuario dos números
#enteros e imprimir todos los números pares entre ellos.

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
for i in range(num1 + (num1 % 2), num2 + 1, 2):
    print(i)