#sentencia if
edad= int(input("Ingrese su edad "))
#if edad >= 18:
 #   print("es mayor de edad")
#print("fuera del bloque if, independiente")    

if edad >= 18:
   print("usted debe votar")
else:
   print("usted es menor de 18 años")
print("fuera del bloque if, independiente")

#
calificacion=int(input("Ingrese su calficacion: "))
if calificacion >=90:
   print("Excelente")
else:
   if calificacion>=80:
      print("Muy Bien")
   else:  
     if calificacion>=70:
        print("bien")
     else:
        print("Insfuficiente")   

