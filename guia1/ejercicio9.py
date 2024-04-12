#9 
 # Solicitar peso y estatura al usuario
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el resultado por pantalla
print("Tu índice de masa corporal es:", imc)