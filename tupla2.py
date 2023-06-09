# A patir de una tupla crear una lisya que solo incluya los números menores a 5

tupla = (12, 1, 8, 3, 2, 5, 8)
lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)


print(lista)
