#7. Escribir un programa que pregunte el nombre de usuari|o y un número entero
#e imprima en diferentes líneas el nombre de usuario tantas veces como el
#número introducido.


nomb = input("Ingrese su nombre: ")
num = int(input("Ingrese un número entero: "))

for i in range(num):
    print(nomb)