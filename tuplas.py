# Tuplas

#las tuplas son lista inmutables, es decir no se pueden modificar
#las tuplas se definen con () y cada elemento separado por una ,

#ejemplo

tupla = (1,2,3,4,5)

tupla_2 = (1, "hola", 3.5, True, [1,2,3], (1,2,3))

print(tupla[3])

#tupla[3] = 0 #genera un error

#largo de una tupla
print(len(tupla))

#cuantos elementos repetidos hay
tupla_3 = (1,2,3,4,4,4,4,4,4,5)

print(tupla_3.count(4))

# concatenar dos tuplas
tupla_4 = (1,2,3)
tupla_5 = (4,5,6)
print(tupla_4 + tupla_5)