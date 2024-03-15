#creacion de listas usando el metodo
#nombres=list()
#crear una lista con valores iniciales
nombres=list(['Gaston','eva','Lautaro'])
#print(nombres)
#metodos, apped, permite agregar un elemento al final de la lista
nombres.append('Sandra')
#print(nombres)
#vamos a utilizar la funcion id
print(id(nombres))
#insert
nombres.insert(0,'victoria')
#print(nombres)
#utilizar el operador in
for nombre in nombres:
    print(nombre)
#mutabilidad
print()
nombres[4]='Lorenza'
for nombre in nombres:
    print(nombre)
print(id(nombres))