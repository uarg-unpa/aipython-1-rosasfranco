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
