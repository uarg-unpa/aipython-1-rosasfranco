#23. Remover los espacios en blanco del principio y final de la siguiente frase, “ La
#ciencia es una ecuación diferencial. La religión es una condición de frontera. “

frase = " La ciencia es una ecuación diferencial. La religión es una condición de frontera. "
f_limpia = frase.rstrip().lstrip()#metodo para limpiar la frase

print(f_limpia)
