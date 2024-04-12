#7. Genere un programa que clasifique a los estudiantes según sus puntuaciones:
#● 80-100, A
#● 70-89, B
#● 60-69, C
#● 50-59, D
#● 0-49, F

punt = int(input("Ingrese la puntuación del estudiante: "))
if 80 <= punt <= 100:
    print("A")
elif 70 <= punt <= 79:
    print("B")
elif 60 <= punt <= 69:
    print("C")
elif 50 <= punt <= 59:
    print("D")
else:
    print("F")