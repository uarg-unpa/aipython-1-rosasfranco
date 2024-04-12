#Implementar una función que convierte temperaturas de fahrenheit a celsius.
def f_a_c(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

# Ejemplo de uso de la función
temperatura_fahrenheit = 75
temperatura_celsius = f_a_c(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit} grados Fahrenheit equivalen a {temperatura_celsius:.2f} grados Celsius.")
