# Son inmutables

frutas = ("Platano", "Naranja", "Pera", "Manzana")

# Largo de una tupla

print(frutas)
print(len(frutas))

# acceder a un elemento en particular
print(frutas[0])
print(frutas[-1])
# acceder a un rango de valores
print(frutas[0:2])

for i in frutas:
    print(i, end=" ")

listaDeFrutas = list(frutas)
listaDeFrutas[0] = "Uva"
print(listaDeFrutas)
frutas = tuple(listaDeFrutas)
print("\n", frutas)
