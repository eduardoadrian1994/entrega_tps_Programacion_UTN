"""
Práctico 4: Estructuras repetitivas
Objetivo:
Implementar ciclos para resolver problemas que requieran repetición de
acciones
"""
"""
Resultados de aprendizaje:
1. Diseño y Desarrollo de Algoritmos Eficientes: El estudiante será capaz de diseñar y
desarrollar algoritmos utilizando estructuras de control repetitivas (FOR, WHILE) para
resolver problemas matemáticos y de lógica, aplicando
correctamente operaciones matemáticas y cálculos.
2. Escritura Eficaz de Pseudocódigo y Documentación: El estudiante podrá escribir
pseudocódigo de manera estructurada y clara, utilizando comentarios para explicar el
funcionamiento de cada parte del algoritmo.
3. Interacción con el Usuario y Validación de Datos: El estudiante será capaz de
diseñar programas que interactúen con el usuario, solicitando datos de entrada y
proporcionando resultados claros y concisos.
"""
"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
# for i in range(101):
#     print(i)

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

# num = int(input("Ingrese un número entero: "))
# #Convertir de int a sting cadena y remover el signo negativo en caso de que lo tenga
# cantidad_digitos = len(str(abs(num)))
# #Con str() convertimos el número en una cadena y luego usamos len() para obtener la cantidad de caracteres (dígitos).
# #La función abs() se aplica para asegurarnos de contar solo los dígitos sin importar el signo.
# print("el número tiene", cantidad_digitos, "digitos.") 

# numero = int(input("Ingresa un número entero: "))
# # Se considera el número absoluto para evitar contar el signo negativo.
# n = abs(numero)
# contador = 0

# # Si el número es 0, consideramos que tiene 1 dígito.
# if n == 0:
#     contador = 1
# else:
#     while n > 0:
#         n //= 10  # División entera para eliminar el último dígito.
#         contador += 1

# print("El número tiene", contador, "dígitos.")


"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# # Inicializar la suma
# suma = 0

# # Iterar sobre el rango entre a y b, sin incluirlos
# for numero in range(num1+ 1, num2):
#     suma += numero

# print("La suma de los números entre", num1, "y", num2, "es:", suma)

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# # Inicializar la suma
# suma = 0
# numero = num1 + 1

# while numero < num2 :
#     suma += numero  # Sumar el número actual a la suma total
#     numero += 1  # Incrementar el número actual

# print("La suma de los números entre", num1, "y", num2, "es:", suma)

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
# CORTE = "0"
# suma_total = 0

# suma = int(input("Ingrese un número entero ("+ CORTE + " para terminar): "))
# while suma != 0:
#     if suma < 0:
#         print("El número no puede ser negativo.")
#     else:
#      suma_total += suma
#     suma = int(input("Ingrese un número entero ("+ CORTE + " para terminar): "))
# print("La suma total es:", suma_total)

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
# import random
# numero_aleatorio = random.randint(0, 9)
# intentos = 0
# numero_usuario = -1

# while numero_usuario != numero_aleatorio:
#     numero_usuario = int(input("Adivina el número entre 0 y 9: "))
#     intentos += 1
#     if numero_usuario < numero_aleatorio:
#         print("El número es mayor.")
#     elif numero_usuario > numero_aleatorio:
#         print("El número es menor.")
#     else:
#         print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
""""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
# for i in range(100, -1, -1):
#     print(i)

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
# num = int(input("Ingrese un número entero positivo: "))
# suma = 0
# for i in range(num + 1):
#     suma += i
# print("La suma de los números entre 0 y", num, "es:", suma)

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
# num_pares = 0
# num_impares = 0
# num_positivos = 0
# num_negativos = 0
# for i in range(100): # Cambia 100 o por la cantidad que desees probar
#     numero = int(input("Ingrese un número entero: "))
#     if numero % 2 == 0:
#         num_pares += 1
#     else:
#         num_impares += 1
#     if numero > 0:
#         num_positivos += 1
#     elif numero < 0:
#         num_negativos += 1
# print("Cantidad de números pares:", num_pares)
# print("Cantidad de números impares:", num_impares)
# print("Cantidad de números positivos:", num_positivos)
# print("Cantidad de números negativos:", num_negativos)

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

# suma = 0
# num = int(input("Ingrese la cantidad de números a promediar: "))
# for i in range(num): # Cambia 100 o por la cantidad que desees probar
#     numero = int(input("Ingrese un número entero: "))
#     suma += numero
#     media = suma / num
# print("La media de los números ingresados es:", media)
# print("La suma es:", suma)

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
# inverso = 0
# num = int(input("Ingrese un número entero: "))	
# for i in range(len(str(num))):
#     digito = num % 10
#     inverso = (inverso * 10) + digito
#     num = num // 10  # Eliminar el último dígito del número original
# print("El número invertido es:", inverso)
