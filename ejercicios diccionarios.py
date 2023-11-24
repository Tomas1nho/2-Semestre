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

#ejercicio 2:

#escribir un programa que guarde en un diccionario los precios de la fruta de la tabla.
#pregunta al usuario por una fruta, numero de kilos y muestre por pantalla el precio de kilo por la fruta.
#si la fruta no se encuentra debe avisarle al usuario.


Tabla = { 
    "Fruta"   : "Precio",
    "Platano" : "1.35",
    "Manzana" : "0.80",
    "Pera"    : "0.85",
    "Naranja" : "0.75",
}

frutas = { 
    "Platano" : 1.35,
    "Manzana" : 0.80,
    "Pera"    : 0.85,
    "Naranja" : 0.75,
}

fruta = input("¿Que fruta quiere?: ")
kg = float(input("¿Cuantos kilos quiere?: "))

if fruta in frutas:
    print(f"{kg} kilos de {fruta} vale ${kg * frutas[fruta]}")
else:
    print(f"La fruta [{fruta}] no se encuentra disponible")