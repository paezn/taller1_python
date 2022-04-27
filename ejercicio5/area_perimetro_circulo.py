"""Ejercicio5:
Calcular el área y el perímetro de un circulo dado su radio"""

import math

print("-------------------------------")
print("----AREA PERIMITRO CIRCULO-----")
print("-------------------------------")

# input
radio = int(input("Digite el valor del radio: "))

# processing
area = math.pi * radio * radio
perimetro = 2 * radio * math.pi

# output
print("\n\nRESULTADOS:\n")
print("Radio: " + str(radio))
print("Area: " +  str(area))
print("Perimetro: " + str(perimetro))