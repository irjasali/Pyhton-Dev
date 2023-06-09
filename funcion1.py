def mi_funcion(nombre):
    print(f"Hola mundo {nombre}")


def sumar(a=475, b=855) -> int:
    return a + b


resultado = sumar()
print(f"El resultado es {resultado}")
print(f"El resultado es {sumar(85,69)}")
mi_funcion("irving")
