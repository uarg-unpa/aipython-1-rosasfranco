#Cortar las dos primeras palabras de la frase ‘’El razonamiento matemático puede
#considerarse más bien esquemáticamente como el ejercicio de una combinación de
#dos instalaciones, que podemos llamar la intuición y el ingenio”.

frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio."
palabras = frase.split()  # Divide la frase en palabras

# Selecciona todas las palabras después de las dos primeras
n_frase = ' '.join(palabras[2:])

print(n_frase)
