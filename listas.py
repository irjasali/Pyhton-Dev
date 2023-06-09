# Definición de una lista
nombres = ["juan", "Karla", "Ricardo", "Pedro", "Roberto"]

# Imprimiento la Lista

print(nombres)

print(nombres[0])
print(nombres[3])
print(nombres[2])
print(nombres[4])

# De forma inversa
print(nombres[-2])
print(nombres[-1])

# por medio de rangos sin incljuir el indice 2
print(nombres[0:2])
print(nombres[2:4])
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:4])
print(nombres[1:])

nombres[4] = "Wallace"
print(nombres)


for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista")
