#14. Escribir una función que tome dos listas como parámetros y las intercale en una
#nueva, retornar la nueva lista resultante.
def intercalar_listas(lista1, lista2):
    nueva_lista = []
    # Determinar la longitud de la lista más corta para iterar hasta ese punto
    longitud_minima = min(len(lista1), len(lista2))
    for i in range(longitud_minima):
        nueva_lista.append(lista1[i])
        nueva_lista.append(lista2[i])

    return nueva_lista

lista1 = [1, 3]
lista2 = [2, 4]
nueva_lista = intercalar_listas(lista1, lista2)
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista intercalada:", nueva_lista)
