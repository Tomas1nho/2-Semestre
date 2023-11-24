#diccionarios

#un diccionario es una coleccion que utiliza para almacenar valores que tienen una relacion entre si.
#se diferencian de los conjuntos porque tiene una clave y valor.
#se define con {} y separan los elementos por ,

#ejemplo

diccionario_1 = {
    "nombre": "juan",
    "edad": 25,
    "peso": 80,
    }

print(diccionario_1["nombre"])
print(diccionario_1["edad"])
print(diccionario_1["peso"])

#largo de un diccionari

print(len(diccionario_1))

#modificar un elemento de un diccionario

diccionario_1["peso"] = 90
print(diccionario_1)

#agregar un elemento a un diccionario

diccionario_1["edad"] = 26
print(diccionario_1)

#eliminar un elemento de un diccionario

diccionario_1.pop("nombre")
print(diccionario_1)

#retornar claves/keys de un diccionario

print(diccionario_1.keys())

#retornar valores de un diccionario

print(diccionario_1.values())
