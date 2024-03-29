#15. Implementar una función que tome una lista de números y retorna el promedio de
#sus elementos.
def calc_promedio(lista):
    suma = sum(lista)
    cantidad_elementos = len(lista)
    if cantidad_elementos == 0:
        return 0  # Si la lista está vacía, el promedio es 0 para evitar divisiones por cero
    else:
        promedio = suma / cantidad_elementos
        return promedio

# Ejemplo de uso de la función
num = [2, 4, 6, 8, 10]
promedio = calc_promedio(num)
print(f"El promedio de los números en la lista es: {promedio}")
