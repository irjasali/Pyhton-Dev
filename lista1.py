# Definición de Listas

nombres = ["Hugo", "Paco", "Luis", "Tribilin"]
# Imprimir la lista de nombres
print(nombres)

print(nombres[0])
print(nombres[1])
print(nombres[3])

nombres[3] = "Pedro"
print(nombres)
# acediendo de forma inversa

print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[-4])

# Accediendo a Rangos en el último estrablecido
print(nombres[0:2])
# ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
# desde el indice indicado hasta el final
print(nombres[1:])

nombres[3] = "Fernanda"
print(nombres)

for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista")

# Largo de una lista
print(len(nombres))
# Agregar un elemento
nombres.append("Alba")
print(nombres)
# insertar un elemento en un indice en especifico
nombres.insert(0, "Octavio")
print(nombres)
# remover un elmemento
nombres.remove("Octavio")
print(nombres)
# remover el último valor agregado
nombres.pop()
print(nombres)
# Eliminar en un indice indicado
del nombres[0]
print(nombres)
# Limpiar todos los elementos de nuestra lista
nombres.clear()
print(nombres)
# Borrar las lista por completo
del nombres
print(nombres)
