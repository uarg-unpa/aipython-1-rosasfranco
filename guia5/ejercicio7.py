#7. Almacenar los nombres de tus compañías favoritas en una lista.
#a. Recorrer la lista del ejercicio 7 y mostrar los datos con print.
#b. Recorrer la lista del ejercicio 7 y mostrar el índice más el nombre de la
#compañía.
#c. Modificar alguna/as de las compañía/s de la lista del ejercicio 7 y luego
#mostrar la lista.

# Crear una lista de compañías favoritas
companias_fav = ['lg', 'Samsung', 'Nokkia', 'Apple']

# a. Recorrer la lista y mostrar los datos con print
print("Lista de compañías favoritas:")
for compania in companias_fav:
    print(compania)

# b. Recorrer la lista y mostrar el índice más el nombre de la compañía
print("\nÍndice y nombre de la compañía:")
for indice, compania in enumerate(companias_fav):
    print(f"{indice}: {compania}")

# c. Modificar alguna/s de las compañía/s de la lista y luego mostrar la lista
# Supongamos que queremos cambiar 'Samsung' por 'Xionami'
indice_samsung = companias_fav.index('Samsung')
companias_fav[indice_samsung] = 'Xionami'

# Mostrar la lista actualizada
print("\nLista de compañías favoritas actualizada:")
for compania in companias_fav:
    print(compania)
