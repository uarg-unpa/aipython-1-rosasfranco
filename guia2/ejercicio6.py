7#6. Escriba un programa que pida al usuario un número entero del 1 al 7 y muestre por
#pantalla a qué día de la semana corresponde. Controlar que el número se encuentre
#dentro del rango [1-7], sino es así, mostrar un mensaje. Por ejemplo, si se ingresa el
#número 2 la salida debe ser martes.
    
numero = int(input("Ingrese un número entero del 1 al 7: "))
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado","domingo"]
if 1 <= numero <= 7:
    print(f"El día correspondiente es {dias[numero - 1]}.")
else:
    print("Número fuera del rango [1-7].")