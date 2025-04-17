"""
Práctico 2: Funciones en Python
Objetivo:
Comprender y aplicar el uso de funciones en la programación, desarrollando algoritmos que implementen modularidad, reutilización de código y
una organización estructurada para resolver problemas.
Resultados de aprendizaje:
Fundamentos de las Funciones: A través de explicaciones teóricas y
ejercicios prácticos, el estudiante desarrollará habilidades para definir, llamar y reutilizar funciones en Python.
Modularidad y Reutilización: El estudiante será capaz de descomponer
problemas complejos en pequeñas unidades funcionales, mejorando la claridad, mantenimiento y reutilización del código.
Resolución de Problemas con Funciones: El estudiante aplicará funciones para resolver problemas computacionales que involucren cálculos matemáticos, manipulación de datos y flujos de control más complejos.
Buenas Prácticas: El estudiante aprenderá a estructurar el código usando funciones y a documentar adecuadamente cada una para facilitar su
comprensión.
Actividades:
"""

"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""

# # Definicion de funciones

# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# #programa principal
# imprimir_hola_mundo()

"""
2.Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
# # Definicion de funciones

# def  saludar_usuario(nombre) :
#     print(f"Hola {nombre}!")

# #programa principal
# saludar_usuario("Marcos")

"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
Pedir los datos al usuario y llamar a esta función con los valores ingresados
"""
# # Definicion de funciones
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# # programa principal
# nombre = input("Ingrese sus nombres: ")
# apellido = input("Ingrese sus apellidos: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su residencia: ")
# informacion_personal(nombre, apellido, edad, residencia)
"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como 
parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas 
funciones para mostrar los resultados.
"""
# import math
# #Deficion de fucinones
# def leer_entero_validado(mensaje, min=float("-inf"), max=float("inf")): 
#     n = int(input(f"{mensaje} "))
#     while n < min or n > max:
#         n = int(input(f"ERROR. {mensaje} "))
#     return n
# def calcular_area_circulo(radio):
#     return math.pi * radio ** 2
# def calcular_perimetro_circulo(radio):
#     return 2 * math.pi * radio
# #programa principal
# radio = leer_entero_validado("Ingrese el radio del círculo: ", 0, 100)
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)
# print(f"El área del círculo es: {area}")
# print(f"El perímetro del círculo es: {perimetro}")

"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos 
y mostrar el resultado usando esta función.
"""
# # Definicion de funciones
# def segundos_a_horas(segundos):
#     horas = segundos // 3600
#     print(f"{segundos} segundos son {horas} horas.")

# #programa principal
# segundos = int(input("Ingrese la cantidad de segundos: "))
# segundos_a_horas(segundos)

"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
# # Definicion de funciones
# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")

# # programa principal
# numero = int(input("Ingrese un número: "))
# tabla_multiplicar(numero)

"""
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""
# # Definicion de funciones
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b if b != 0 else "Error: División por cero"
#     print (f"el resultado de la suma es: {suma}, la resta es: {resta}, la multiplicacion es: {multiplicacion} y la division es: {division}") 

# # programa principal
# a = float(input("Ingrese el primer número: "))
# b = float(input("Ingrese el segundo número: "))
# operaciones_basicas(a, b)

"""
Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
función para mostrar el resultado con dos decimales
"""
# # Definicion de funciones
# def calcular_imc(peso, altura):
#     imc = round(peso / altura**2, 2)
#     print(f"Su IMC es de: {imc}.")

# # programa principal
# peso = float(input("Por favor, ingrese su peso en kilogramos: "))
# altura = float(input("Por favor, ingrese su altura en metros: "))
# calcular_imc(peso, altura)
"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
# # Defincion de funciones
# def celsius_a_fahrenheit(celsius):
#     fahrenheit = round((9/5)*celsius+32, 2)
#     print(f"{celsius} °C equivalen a {fahrenheit} °F.")

# # Programa principar
# celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# celsius_a_fahrenheit(celsius)

"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
# # Definicion de funciones
# def calcular_promedio(a, b, c):
#     suma_a_b_c = a + b + c
#     promedio_a_b_c = round(suma_a_b_c / 3, 2)
#     print(f"El promedio de los números ingresados es {promedio_a_b_c}.")

# # Programa principal
# a = float(input("Por favor, ingrese el primer número: "))
# b = float(input("Por favor, ingrese el primer número: "))
# c = float(input("Por favor, ingrese el primer número: "))
# calcular_promedio(a, b, c)
