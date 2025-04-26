"""
Práctico 5: Listas
Objetivo:
Desarrollar la comprensión y la capacidad de manipular listas en Python
mediante la aplicación de conceptos fundamentales como la indexación, la
modificación de elementos, el uso de métodos integrados y el manejo de
listas anidadas.
Resultados de aprendizaje:
1. Reconocer y aplicar correctamente la indexación y el slicing para acceder a elementos
individuales o subconjuntos dentro de una lista.
2. Utilizar los métodos básicos de listas para crear, modificar y gestionar estructuras de
datos simples.
3. Modificar listas mediante la actualización de valores y el manejo de listas anidadas,
comprendiendo cómo acceder a datos en estructuras más complejas.
"""

"""
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.
"""

# numeros_multiplo_4 = list(range(4, 101, 4))
# print(numeros_multiplo_4)


"""
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!
"""
# lista =[ "manzana", "pera", "uva", "naranja", "kiwi"]
# print(lista[-2])

"""
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []
"""
# lista_vacia = []

# lista_vacia.append("manzana")
# lista_vacia.append("avion")
# lista_vacia.append("uva")
# lista_vacia.append("perro")

# print(lista_vacia)


"""
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
"""
# #posicion segun lista:
# #              0        1        2       3
# #             -4       -3       -2      -1
# animales = ["perro", "gato", "conejo", "pez"]

# animales[-2] = "loro"
# animales[-1] = "oso"
# print(animales)

# #posicion segun como esta armada al lista;

# #posicion segun lista:
# #              1        2        3       4
# #             -4       -3       -2      -1
# animales = ["perro", "gato", "conejo", "pez"]

# animales[-3] = "loro"
# animales[-1] = "oso"
# print(animales)

"""
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
"""
# # contiene una lista de numeros enteros.
# numeros = [8, 15, 3, 22, 7]
# # se le pasa la lista y se llama ala funcion remove, dentro de la funcion se llama a la funcion max, 
# # que devuelve el mayor valor de la lista, en este caso 22.
# # la funcion remove elimina el valor 22 de la lista numeros.
# numeros.remove(max(numeros))
# # se imprime la lista de numeros, que ahora no contiene el valor 22.
# print(numeros)
# # dejando la lista [8, 15, 3, 7]

"""
6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
"""

# numeros_en_5_5 = list(range(10, 101, 5))
# print(numeros_en_5_5[:2])

"""
7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
"""

# autos = ["sedan", "polo", "suran", "gol"]

# autos[1] = "toyotaTruenoAE86"
# autos[2] = "Corsa classic"

# print(autos)

"""
8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
"""
# dobles = []

# dobles.append(5*2)
# dobles.append(10*2)
# dobles.append(15*2)

# print(dobles)

"""
9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
"""
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]

# #a)Agregar "jugo" a la lista del tercer cliente usando append.

# compras[2].append("jugo")

# #b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# compras[1][1] = "tallarines"

# #c) Eliminar "pan" de la lista del primer cliente.
# compras[0].remove("pan")

# #d) Imprimir la lista resultante por pantalla
# print(compras)

"""
10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
"""
# lista_anidada = [[15, True], [25.5, 57.9, 30.6
# ],[False]]
# print(lista_anidada)

