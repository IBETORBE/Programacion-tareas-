# Programa para calcular el área de un círculo
import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float or int): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    area = math.pi * radio ** 2
    return area

def main():
    # Solicitar al usuario que ingrese el radio del círculo
    radio_str = input("Ingrese el radio del círculo: ")
    radio = float(radio_str)  # Convertir la entrada a float

    # Calcular el área del círculo utilizando la función definida
    area_circulo = calcular_area_circulo(radio)

    # Mostrar el resultado al usuario
    print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")

if __name__ == "__main__":
    main()
