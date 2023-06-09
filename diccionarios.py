diccionario = {
    "IDE": "iNTEGRATED dEVELOMENT eNVIROMENET",
    "OOP": "oBJECT Oriented Programming",
    "dbms": "Database Management System",
}


print(diccionario)
print(len(diccionario))
print(diccionario["IDE"])
print(diccionario.get("OOP"))
diccionario["dbms"] = "SDFLSDFLSKF"
print(diccionario)

# RECORRER LOS ELEMENTOS DE UN DICCIONARIO

for elemento, valor in diccionario.items():
    print(elemento, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# comprobar existencia de un elemento

print("IDE" in diccionario)

# agregar un elemento
diccionario["PK"] = "Primary KEy"
print(diccionario)

# remover elemento
diccionario.pop("dbms")
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

# borrar
del diccionario
print(diccionario)
