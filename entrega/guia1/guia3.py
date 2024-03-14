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
#8. Escribir un programa que pida un número entero positivo mayor a 3 y muestre
#por pantalla todos los números impares desde 1 hasta ese número.
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