print("Taller de AIPython P1 E2")
print("el","taller","es")
print("hola alumnos                     ","es viernes",sep='-')
print("probando argumentos","soy el segundo argumento", end='*')
print("soy otra linea")

print("soy seis")
print("Las maquinas me sorprenden con mucha frecuencia")
print("")
print("23",23) 
print("Una computadora puede ser llamada ''intelig|ente'' si logra engañar a una persona haciéndole creer que es un humano.")
print("Franco ","rosas","25")
# print("Franco ","rosas","25",sep='-')
print("calle \t","numero \t"," codigo postal \t")
print("calle")
print("numero")
print("codigo postal")
print("--------------")
# Imprimir en forma de escalera
print("Feliz\n","\tPrimavera\n","\t\t\t2024")

# Imprimir la primera parte terminando con una coma
print("Solo podemos ver poco del futuro", end=', ')
# Continuar la impresión en la misma línea
print("pero lo suficiente para darnos cuenta de que hay mucho que hacer.")
#i
print("       *       ")
print("      ***      ")
print("     *****     ")
print("    *******    ")
print("   *********   ")
print("  ***********  ")
print(" ************* ")
print("***************")
print("--")
#3
nombre = "Franco"
apellido = "Rosas"
edad = 25
altura = 1.70
numero_de_vuelo = "FRA999"
temperatura_ambiente = 8.0
salario_mensual = 100000.00
juego_terminado = False

#  determinA si un número es par

# Mostrar por pantalla
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Edad:", edad)
print("Altura:", altura)
print("Número de vuelo:", numero_de_vuelo)
print("Temperatura ambiente:", temperatura_ambiente, "°C")
print("Salario mensual:", salario_mensual)
print("El juego terminó:", juego_terminado)

# Uso de la función es_numero_par sin funciones

print("--")

#4
#a. nombre: Literal de cadena
#b. apellido: Literal de caden
#c. edad: Literal numérico entero 
#d. altura: Literal numérico de punto flotante 
#e. numero_vuelo: Literal numérico entero 
#f. temperatura_ambiente: Literal numérico de punto flotante 
#g. salario_mensual: Literal numérico de punto flotante
#h. juego_terminado: Literal booleano (True o False).
#i. es_par: Literal booleano 

#5
# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")

# Imprimir mensaje creativo con los datos ingresados
print(f"{nombre} {apellido}, ser creativo con {edad} años.")

# Solicitar datos al usuario y mostrar mensaje creativo en una sola línea
mensaje_creativo = input("Ingresa tu nombre, apellido y edad separados por espacios: ")
print(f"{mensaje_creativo}, ser creativo.")

# 6 Solicitar dos números enteros al usuario
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))


print("La suma es:", num1 + num2)
print("La resta es:", num1 - num2)
print("El producto es:", num1 * num2)
print("La potencia es:", num1 ** num2)
print("El resto es:", num1 % num2)

#7 # Solicitar un número entero y un número de punto flotante al usuario
num_entero = int(input("Ingresa un número entero: "))
num_float = float(input("Ingresa un número de punto flotante: "))

# Realizar operaciones y mostrar resultados
print("La suma es:", num_entero + num_float)
print("La resta es:", num_entero - num_float)
print("El producto es:", num_entero * num_float)
print("La potencia es:", num_entero ** num_float)
print("El resto es:", num_entero % num_float)

frase=input("Ingrese una frase")
caracter=input("Ingrese un caracter")
#buscar la primera aparicion del caracter
posicion=frase.find(caracter)

if posicion !=-1:
    print(f"El caracter{caracter} se encuentra en la posicion {posicion+1}")
    subcadena=frase[posicion:]
    print(f"Subcadena a partir de la posicion {posicion+1}: {subcadena}")
else:
    print(f"el caracter {caracter} no se encuntra en la frase")

#9 
 # Solicitar peso y estatura al usuario
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el resultado por pantalla
print("Tu índice de masa corporal es:", imc)

#10 # Solicitar temperatura en grados Celsius al usuario
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Realizar la transformación a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado por pantalla
print("La temperatura en grados Fahrenheit es:", fahrenheit)

#11
# Solicitar al usuario el número de horas trabajadas y el costo por hora
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
costo_por_hora = float(input("Ingrese el costo por hora: "))

# Calcular el sueldo
sueldo = horas_trabajadas * costo_por_hora

# Mostrar el sueldo por pantalla
print("El sueldo correspondiente es:", sueldo)

#---RANGE
for num in range[11]:
    print(num)

for _ in range(10):
    print("AIPYTHON")
#12
# Solicitar al usuario la cantidad a invertir, el interés anual y el número de años
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (en porcentaje): "))
num_anios = int(input("Ingrese el número de años: "))

# Calcular el capital obtenido en la inversión
interes_decimal = interes_anual / 100  # Convertir el interés a formato decimal
capital_obtenido = cantidad_invertir * (1 + interes_decimal) ** num_anios

# Mostrar el capital obtenido por pantalla
print("El capital obtenido en la inversión es:", capital_obtenido)

# 14  Concatenar los strings
resultado = 'Una ambiciosa' + ' ' + 'Introducción' + ' ' + 'a Python' + ' ' + 'Parte 1'

# Mostrar el resultado por pantalla
print(resultado)

#15 ----------------# Inicializar la variable sociedad
sociedad = 'aiPython P1'

# a. Imprimir la variable utilizando print()
print("a. Valor de la variable sociedad:", sociedad)

# b. Imprimir la longitud de la variable sociedad usando len() y print()
longitud_sociedad = len(sociedad)
print("b. Longitud de la variable sociedad:", longitud_sociedad)

# c. Cambiar todos los caracteres a mayúsculas usando el método upper()
sociedad_mayusculas = sociedad.upper()
print("c. Variable sociedad en mayúsculas:", sociedad_mayusculas)

# d. Cambiar todos los caracteres a minúsculas usando el método lower()
sociedad_minusculas = sociedad.lower()
print("d. Variable sociedad en minúsculas:", sociedad_minusculas)

#16 
# String proporcionado
frase = "sometimes it is the people no one imagines anything of who do the things that no one can imagine."

# Aplicar los métodos y mostrar los resultados
resultado_capitalize = frase.capitalize()
resultado_title = frase.title()
resultado_swapcase = frase.swapcase()

# Mostrar los resultados por pantalla
print("Original:", frase)
print("capitalize():", resultado_capitalize)
print("title():", resultado_title)
print("swapcase():", resultado_swapcase)

  
