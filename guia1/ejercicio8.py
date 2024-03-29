#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable. Luego debe
#mostrar por pantalla la frase: "Tu índice de masa corporal es: <imc>". Donde <imc>
#es el índice de masa corporal calculado. Tip. buscar en google cómo calcular el IMC.

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura ** 2)
print(f"Tu índice de masa corporal es: {imc}")
