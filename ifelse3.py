aNacimiento = int(input("Año de Nacimiento:"))
aActual = int(input("Año Actual:"))

edad = aActual - aNacimiento

mensaje = None
if 0 <= edad < 10:
    mensaje = "La infancia es increíble..."
elif 10 <= edad < 20:
    mensaje = "Muchos cambios y Estudio"
elif 20 <= edad < 50:
    mensaje = "Amor y comienza el trabajo..."
else:
    mensaje = "Estapa no reconicida..."


print(f"0-10; Tú edad es {edad} y {mensaje}")
