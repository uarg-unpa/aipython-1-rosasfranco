import random

def lanzar_dado(num_caras):
    return random.randint(1, num_caras)

def lanzamientos_multiples(cant_dados, num_caras, cant_lanzamientos):
    resultados = []
    for _ in range(cant_lanzamientos):
        lanzamientos = [lanzar_dado(num_caras) for _ in range(cant_dados)]
        resultados.append(sum(lanzamientos))
    return resultados

def main():
    cant_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
    num_caras = int(input("Ingrese el número de caras de cada dado: "))
    cant_lanzamientos = int(input("Ingrese la cantidad de lanzamientos deseados: "))

    aux = lanzamientos_multiples(cant_dados, num_caras, cant_lanzamientos)

    print(f"Resultados individuales: {aux}")
    print(f"Total de los resultados: {sum(aux)}")
    print(f"Promedio de los resultados: {sum(aux) / cant_lanzamientos}")
    print(f"Valor mínimo: {min(aux)}")
    print(f"Valor máximo: {max(aux)}")

if __name__ == "__main__":
    main()
