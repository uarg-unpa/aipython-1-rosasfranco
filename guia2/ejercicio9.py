
#Para pagar un determinado impuesto se debe ser mayor de 18 años y tener ingresos
#iguales o superiores a $100000 mensuales. Escribir un programa que pregunte al
#usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
#que pagar o no el impuesto.

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))

if edad > 18:
    if ingresos >= 100000:
        print("Debe pagar el impuesto")
    else:
        print("No debe pagar el impuesto porque no cumple con el requisito de ingresos.")
else:
    print("No debe pagar el impuesto porque no cumple con el requisito de edad.")

