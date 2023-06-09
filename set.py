# definición de tipo set

planetas = {"Marte", "Jupiter", "Venus"}

print(planetas)
print(len(planetas))

# revisar si un elemento esta presente

print("Marte" in planetas)

# Agregar más elementos

planetas.add("Tierra")
print(planetas)

# No se pueden duplicar elementos
planetas.add("Tierra")

# Eliminar elementos
planetas.remove("Tierra")

print(planetas)

planetas.discard("Jupiter")
print(planetas)

# Limpiar el set
planetas.clear()
print(planetas)

# Eliminar el set
del planetas
print(planetas)
