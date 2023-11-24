'''escribir un programa que pregunte al usuario los numeros ganadores de la loteria, los almacene en una lista y los muestre por pantalla ordenados.
'''

numeros_ganadores = []
for i in range(6):
    numeros_ganadores.append(int(input("Ingrese un numero de los ganadores: ")))

print("los numero de los ganadores son, "+ str(numeros_ganadores))



#ejercicio 2:
#escribir un programa que almacene en una lista los siguientes valores y 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los valores.


lista_2 = [50, 75, 46, 22, 80, 65, 8]

menor = lista_2[0]
mayor = lista_2[0]

for i in lista_2:
    if i < menor:
        menor = i
    if i > mayor:
        mayor = i

print(f"El menor numero es {menor}")
print(f"El mayor numero es {mayor}")


#ejercicio 3:
#escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.

tupla_3 = (1,2,3)
tupla_4 = (-1,0,2)

#producto_escalar = (tupla_3[0]*tupla_4[0] + tupla_3[1]*tupla_4[1] + tupla_3[2]*tupla_4[2])
producto_escalar = 0

for i in range(len(tupla_3)):
    producto_escalar = producto_escalar + (tupla_3[i]*tupla_4[i])    
    


print(f"El producto escalar es: {producto_escalar}")


#ejercicio 4:
#escribir un programa que almacene las matrices A y B en una tupla y muestre por pantalla su producto

A = [
    [1,2,3],
    [4,5,6]
]

B = [
    [1,2],
    [4,5],
    [7,8]
]

producto = [[0,0],
            [0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            producto [i][j] += (A[i][k] * B[k][j])
        
print(producto)

#ejercicio extra (hard mode)
#escribir un diccionario con nombres de estudiantes, el valor de cada llave debe ser otrodiccionario con la informacion de los estudiantes: edad, peso y altura.

estudiantes = {
    "Juan": {
        "edad": 25,
        "peso": 70,
        "altura": 1.75
    },
    "Pedro": {
        "edad": 22,
        "peso": 65,
        "altura": 1.65
    },
    "Maria": {
        "edad": 20,
        "peso": 60,
        "altura": 1.70
    }
}

for i in estudiantes:
    print(estudiantes[i])
