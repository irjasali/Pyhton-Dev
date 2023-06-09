print("Datos del libro")
nombreLibro = input("Nombre del libro:")
idLibro = int(input("ID del Libro"))
precioLibro = float(input("Precio del libro:"))
envio = input("Envio gratis True/False")

if envio == "True":
    envio = True
elif envio == False:
    envio = False
else:
    envio = "Valor incorrecto, debe escribir True/False"


print("Los datos del libro a enviar son los siguientes")

print(
    f"""
        Nombre: {nombreLibro}
        ID: {idLibro} 
        Precio: {precioLibro}
        envio: {envio}
        
        """
)
