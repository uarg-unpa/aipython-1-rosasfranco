#num=2
#def multiplicacion(x):
#    num=3
#    return x*num
#print(multiplicacion(4))

#def mensaje():
#    alternativo='mas sobre programacion'
#    print("Alumnos de AIPython")
#    return alternativo
#dato=mensaje()
#print(dato)

def mutables(lista):
    lista[2]=35
    return lista

mis_numeros=[1,2,3]
print(f"Antes de invocar a la funcion")
print(mis_numeros)
mutables(mis_numeros)
print("Despues de llamar a la funcion mutables")
print(mis_numeros)