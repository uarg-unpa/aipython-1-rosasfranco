#4. Escribir un programa que pida al usuario dos números enteros e imprima todos los
#números entre ellos.
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
for i in range(n1, n2 + 1):
  print(i, end=" ")