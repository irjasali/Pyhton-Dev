# Función que calcula la Hipotenusa

import math


def Hipo(co, ca):
    return math.sqrt((co**2) + (ca**2))


co = float(input("Dame el valor del cateto Opuesto:"))
ca = float(input("Dame el valor del cateto Adyacente:"))
print(f"La hipotenusa es {Hipo(ca,co)}")
