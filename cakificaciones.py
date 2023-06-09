calificacion = int(input("Proporciona la calificación entre 0 y 10:"))
mensaje = None

if 0 <= calificacion < 6:
    mensaje = "F"
elif 6 <= calificacion < 7:
    mensaje = "D"
elif 7 <= calificacion < 8:
    mensaje = "C"
elif 8 <= calificacion < 9:
    mensaje = "B"
elif 9 <= calificacion < 10:
    mensaje = "A"
else:
    mensaje = "Valor incorrecto"


print(f"La notal final es {mensaje}")
