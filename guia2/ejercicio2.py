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
