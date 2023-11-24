#Conjuntos

#los conjuntos son colecciones no ordenados y sin elementos duplicados.
#son utiles para realizar operaciones de conjuntos como uniones, intersecciones, etc.

#ejemplo

conjunto_1 = {1, 2, 3, 4, 5, 5}

print (conjunto_1)

# crear un conjunto vacio

conjunto_vacio = set()

#conjunto_2 = {1, "juan", 3.5, True, [1,2,3], (1,2,3)}
#print (conjunto_2)
# los conjuntos no pueden contener listas, porque requieren que todo sus elementos sean inmutables.

#no tiene orden

conjunto_3 = {1, 2, 3, 4, 5}
#print(conjunto_3[0]) # error

#añadir elementos a un conjunto

conjunto_4 = {1, 2, 3, 4, 5}
conjunto_4.add(6)
print(conjunto_4)

#eliminar elementos de un conjunto

conjunto_5 = {1, 2, 3, 4, 5, 6}
conjunto_5.remove(3)
print(conjunto_5)

#operacion de conjuntos

#UNION A ∪ B

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9, 0}

conjunto_union = conjunto_a.union(conjunto_b)

print(conjunto_union)

# interseccion A ∩ B

conjunto_a = {1, 2, 3, 4, 5, 6}
conjunto_b = {4, 5, 6, 7, 8, 9}

conjunto_interseccion = conjunto_a.intersection(conjunto_b)
print(conjunto_interseccion)

# diferencia A − B

conjunto_a = {1, 2, 3, 4, 5, 6}
conjunto_b = {4, 5, 6, 7, 8, 9}

conjunto_diferencia = conjunto_a.difference(conjunto_b)
print(conjunto_diferencia)

# diferencia simetrica B ∆ A / (A ∪ B) - (A ∩ B) = (A − B) ∪ (B − A)

conjunto_diferencia_simetrica = conjunto_b.symmetric_difference(conjunto_a)
print(conjunto_diferencia_simetrica)



















