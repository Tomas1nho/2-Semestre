#ejercicio 1:

#escribir un programa que le pregunte al usuario su nombre, edad, dirección y telefono. y lo guarda en un diccionario.
#despues debe mostrar por pantalla "nombre persona", "edad", "direccion", "telefono".

diccionario_2 = {
    "nombre": "",
    "edad": "",
    "direccion": "",
    "telefono": "",
    }

nombre = input("Ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
direccion = input("Ingrese su direccion: ")
telefono = int(input("Ingrese su telefono: "))

diccionario_2["nombre"] = nombre

diccionario_2["edad"] = edad

diccionario_2["direccion"] = direccion

diccionario_2["telefono"] = telefono

print(diccionario_2)