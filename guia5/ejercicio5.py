#5. Dada una lista mostrar el primer elemento, el del medio y el último.
frutas_favoritas = ['banana', 'manzana', 'naranja','uva', 'pera', 'mandarina']

# Calcular el índice del elemento del medio
indice_medio = len(frutas_favoritas) // 2

# Mostrar el primer elemento, el del medio y el último
primer_elemento = frutas_favoritas[0]
elemento_medio = frutas_favoritas[indice_medio]
ultimo_elemento = frutas_favoritas[-1]

# Imprimir los resultados
print(f"Primer elemento: {primer_elemento}")
print(f"Elemento del medio: {elemento_medio}")
print(f"Último elemento: {ultimo_elemento}")
