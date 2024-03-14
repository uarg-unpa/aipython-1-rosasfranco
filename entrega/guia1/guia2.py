# 1 Solicite información del usuario mediante el uso de input(“Ingrese su edad: ”). Si el
#usuario tiene 18 años o más, informar: tiene edad suficiente para conducir. Si tiene
#menos de 18 años,informe la cantidad de años que faltan.
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Tiene edad suficiente para conducir.")
else:
    print(f"Faltan {18 - edad} años para que pueda conducir.")

#2. Compare su edad y mi edad usando if..else. ¿Quién es mayor (vos o yo)?,
#para el ingreso de la edad use input(“Ingrese su edad: ”)
#Use un condición anidada para:
#Imprimir año si la diferencia es de 1, sino años para diferencias
#mayores.
#Cuando las edades son iguales imprimir un mensaje personalizado,
#ser creativo!!

mi_edad = 25  
su_edad = int(input("Ingrese su edad: "))
if su_edad > mi_edad:
    diferencia = su_edad - mi_edad
    print(f"Usted es mayor que yo por {diferencia} {'año' if diferencia == 1 else 'años'}")
elif su_edad < mi_edad:
    diferencia = mi_edad - su_edad
    print(f"Yo soy mayor que usted por {diferencia} {'año' if diferencia == 1 else 'años'}")
else:
  print("¡Increíble! Parece que fuimos separados al nacer :D")



#3. Solicite al usuario una contraseña, utilizando input(“Ingrese su contraseña”),
#almacene esta contraseña en una variable. Luego informar si la contraseña
#introducida coincide con la guardada sin tener en cuenta mayúsculas y
#minúsculas .

contraseña_guardada = "Contraseña1"
contraseña_usuario = input("Ingrese su contraseña: ")
if contraseña_guardada.lower() == contraseña_usuario.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

#4. Obtenga dos números del usuario mediante input. Si a es mayor que b, devuelve a
#es mayor que b, si a es menor que b, devuelve a es menor que b de lo contrario, a
#es igual a b.

a = int(input("Ingrese el primer número a: "))
b = int(input("Ingrese el segundo número b: "))
if a > b:
    print("a es mayor que b.")
elif a < b:
    print("a es menor que b.")
else:
    print("a es igual a b.")

#5. Escriba un programa que pida al usuario un número entero e indique si es par o
#impar.

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

#6. Escriba un programa que pida al usuario un número entero del 1 al 7 y muestre por
#pantalla a qué día de la semana corresponde. Controlar que el número se encuentre
#dentro del rango [1-7], sino es así, mostrar un mensaje. Por ejemplo, si se ingresa el
#número 2 la salida debe ser martes.
    
numero = int(input("Ingrese un número entero del 1 al 7: "))
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado","domingo",]
if 1 <= numero <= 7:
    print(f"El día correspondiente es {dias[numero - 1]}.")
else:
    print("Número fuera del rango [1-7].")

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

#8. Escriba un programa para una empresa que tiene salas de juegos para todas las
#edades y quiere calcular de forma automática el precio que debe cobrar a sus
#clientes por entrar. El programa debe preguntar al usuario la edad del cliente y
#mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
#si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10.

edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10
print(f"El precio de la entrada es: ${precio}")

#Para pagar un determinado impuesto se debe ser mayor de 18 años y tener ingresos
#iguales o superiores a $100000 mensuales. Escribir un programa que pregunte al
#usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
#que pagar o no el impuesto.

edad = int(input("Ingrese su edad: ."))
ingresos = float(input("Ingrese sus ingresos mensuales: ."))

if edad > 18:
    if ingresos >= 100000:
        print("Debe pagar el impuesto")
    else:
        print("No debe pagar el impuesto porque no cumple con el requisito de ingresos.")
else:
    print("No debe pagar el impuesto porque no cumple con el requisito de edad.")

