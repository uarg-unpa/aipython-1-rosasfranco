#15.Escribir un programa que pida un número entero e informe si dicho número es
#primo o no primo

numero = int(input("Ingrese un numero entero: "))

if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    primo = True
    # si el número es divisible por el valor actual de i significa 
    # que el número no es primo y actualizamos la variable es_primo a False. 

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")