#ejercicio 1: crear un conjunto y añadir elementos al conjunto
#crear un conjunto vacio y añadele elementos tres elementos de diferente tipo.

conjunto_1 = set()
print (conjunto_1)
conjunto_1.add(1)
conjunto_1.add("colo colo")
conjunto_1.add(3.5)

print (conjunto_1)

#ejercicio 2: crear un conjunto a partir de un conjunto A = {1, 2, 3, 4, 5} cuyos valores sean el cuadrado de los elementos del conjunto A.

conjunto_a = {1, 2, 3, 4, 5}

conjunto_b = set()

for i in conjunto_a:
    conjunto_b.add(i**2)
    
print(conjunto_b)

#ejercicio 3: estudiantes en diferentes clases
# en la universidad, hay dos cursos: matematicas y literatura.
#tienes estudiantes que estan inscritos en ambos cursos.
#matematicas: ana, luis, pedro, maria
#literatura: juan, maria, ana, sofia

conjunto_m = {"ana", "luis", "pedro", "maria"}
conjunto_l = {"juan", "maria", "ana", "sofia"}

conjunto_diferencia_curso = conjunto_m.intersection(conjunto_l)
print(conjunto_diferencia_curso)