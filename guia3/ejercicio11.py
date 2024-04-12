#11. Escribir un programa que pida al usuario un número entero y muestre por
#pantalla un triángulo rectángulo como el que se muestra
#Si se ingresa el número 9, el resultado será
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

numero = int(input("Ingrese un número entero: "))

# Bucle para imprimir el triángulo rectángulo
for i in range(numero, 0, -2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print()  # Salto de línea después de cada fila
