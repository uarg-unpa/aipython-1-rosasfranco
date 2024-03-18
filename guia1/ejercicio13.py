# Escribir un programa que calcule el promedio de precios de 10 productos.

suma_precios = 0

for i in range(1, 11):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    suma_precios =suma_precios + precio  
promedio_precios = suma_precios / 10
print(f"El promedio de precios de los 10 productos es: ${promedio_precios}")
