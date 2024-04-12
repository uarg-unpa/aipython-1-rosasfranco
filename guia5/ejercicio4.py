#4. Crear una lista de tus frutas favoritas
#a. Imprimir la longitud.
#b. Eliminar el primer elemento de la lista.
#c. Agregar un elemento al final de la lista.
#d. Imprimir los resultados anteriores.

# Crear una lista de frutas favoritas
frutas_fav = ['banana', 'manzana', 'naranja']

# a. Imprimir la longitud de la lista
longitud_original = len(frutas_fav)
print(f"Lista de frutas favoritas actualizada: {frutas_fav}")
print(f"Longitud original de la lista: {longitud_original}")

# b. Eliminar el primer elemento de la lista
frutas_fav.pop(0)

# c. Agregar un elemento al final de la lista
frutas_fav.append('anana')

# d. Imprimir los resultados anteriores
longitud_final = len(frutas_fav)
print(f"Longitud final de la lista: {longitud_final}")
print(f"Lista de frutas favoritas actualizada: {frutas_fav}")
