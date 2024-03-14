#1. Iterar de 0 a 100 usando un bucle while y mostrar dichos números.

i = 0
while i <= 100:
    print(i, end=" ")
    i =i + 1

#2. Tomar el ejercicio 1 y realizarlo con un bucle for, tip usar range. los números deben
#salir uno al lado del otro.
    
    for i in range(101):
     print(i, end=" ")

#3. Iterar de 10 a 0 usando un bucle while y un bucle for.
    i = 10
    while i >= 0:
     print(i, end=" ")
     i =i - 1

    for i in range(10, -1, -1):
     print(i, end=" ")

#4. Escribir un programa que pida al usuario dos números enteros e imprima todos los
#números entre ellos.
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    for i in range(n1, n2 + 1):
      print(i, end=" ")


#5. Escribe un bucle que haga siete llamadas a print(), de modo que obtengamos
#en la salida el siguiente triángulo:

#
##
###
####
#####
######
#######

for i in range(1, 8):
    print("#" * i)

#6. Usar bucles anidados para mostrar la siguiente figura

########
########
########
########
########
########
########
########

for i in range(8):
    for j in range(8):
        print("#", end="")
    print()

#7. Escribir un programa que pregunte el nombre de usuari|o y un número entero
#e imprima en diferentes líneas el nombre de usuario tantas veces como el
#número introducido.


nomb = input("Ingrese su nombre: ")
num = int(input("Ingrese un número entero: "))

for i in range(num):
    print(nomb)

#8. Escribir un programa que pida un número entero positivo mayor a 3 y muestre
#por pantalla todos los números impares desde 1 hasta ese número.

num = int(input("Ingrese un número entero positivo mayor a 3: "))

for i in range(1, num + 1, 2):
    print(i)

#9. Escribir un programa que permita mostrar el siguiente patrón:

#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

for i in range(11):
    print(f"{i} x {i} = {i*i}")

#10. Escribir un programa que imprima todas las fichas del domino, una por línea,
#sin repetir. Como se muestra a continuación
#0 0
#0 1
#0 2
#0 3
#0 4
#0 5
#0 6
#...

for i in range(7):
    for j in range(i, 7):
        print(f"{i} {j}")

#11. Escribir un programa que pida al usuario un número entero y muestre por
#pantalla un triángulo rectángulo como el que se muestra
#Si se ingresa el número 9, el resultado será
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1


#12. Escribir un programa que pida un número natural N al usuario e imprima por
#pantalla la suma de los números naturales de 1 hasta N.
#Por ejemplo para N = 5, la salida debe ser:
#1 + 2 + 3 + 4 + 5 = 15

N = int(input("Ingrese un numero natural: "))
suma = 0
for i in range(1, N + 1):
    suma =suma + i
print(f"La suma de los números naturales hasta {N} es igual a: {suma}")



#13.Construir un programa que lea un número natural N y calcule la suma de los
#primeros N números pares.

N = int(input("Ingrese un numero natural: "))
suma = 0
for i in range(2, 2 * N + 1, 2):
    suma =suma + i
print(f"La suma de los primeros {N} números pares es: {suma}")

#14.Escribir un programa que recibe como entrada desde el usuario dos números
#enteros e imprimir todos los números pares entre ellos.

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
for i in range(num1 + (num1 % 2), num2 + 1, 2):
    print(i)

#15.Escribir un programa que pida un número entero e informe si dicho número es
#primo o no primo

numero = int(input("Ingrese un numero entero: "))

if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    primo = True
    # si el número es divisible por el valor actual de i significa 
    # que el número no es primo y actualizamos la variable es_primo a False. 

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
