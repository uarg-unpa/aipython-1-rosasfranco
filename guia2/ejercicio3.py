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
