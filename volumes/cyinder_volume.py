import math
radio = float(input("El radio del círculo: "))
altura = float(input("Altura del cilindro: "))
area_circ = math.pi * (radio**2)
volumen = area_circ * altura

print( round(volumen,6))
