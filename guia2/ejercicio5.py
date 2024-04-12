#5. Escriba un programa que pida al usuario un número entero e indique si es par o
#impar.

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
