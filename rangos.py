# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

for rango in range(10):
    if rango % 3 == 0:
        print(rango)

print("**************************")
# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos
rango2 = range(2, 7)
for i in rango2:
    print(i)

print("**************************")

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

rango3 = range(3, 11, 2)
for i in rango3:
    print(i)

print("**************************")
