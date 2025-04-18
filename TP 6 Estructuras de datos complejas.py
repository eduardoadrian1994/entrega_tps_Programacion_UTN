"""
Práctico 6: Estructuras de datos complejas
Objetivo:
Dominar el uso de estructuras de datos complejas en Python para
almacenar, organizar y manipular datos de manera eficiente, aplicando
buenas prácticas y optimizando el rendimiento de las aplicaciones.
Resultados de aprendizaje:
1. Comprensión y aplicación de iterables: listas, tuplas y sets.
2. Introducción a estructuras de datos complejas: diccionarios y objetos.
"""


"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""
# Programa principal
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300
# print(precios_frutas)
"""
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
# #Programa principal
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300
# print(precios_frutas)
# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800
# print("Lista de precios de frutas actualizado : ", precios_frutas)


"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300
# #print(precios_frutas)
# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800
# #print("Lista de precios de frutas actualizado : ", precios_frutas)
# print("Lista de frutas : ", list(precios_frutas.keys()))

"""
4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
años."
"""
# # Definición de la clase Persona
# class Persona:
#     def __init__(self, nombre, pais,edad):
#         self.nombre = nombre
#         self.pais = pais
#         self.edad = edad
#     # en java lo conozco como to string     
#     def saludar(self):
#         print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
# #Programa principal
# persona = Persona("Eduardo", "Argentina", 31)
# persona.saludar()

"""
5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.
"""
# import math
# # Definición de la clase Circulo
# class Circulo:
#     def __init__(self, radio):
#         self.radio = radio

#     def calcular_area(self):
#         return math.pi * (self.radio ** 2)

#     def calcular_perimetro(self):
#         return 2 * math.pi * self.radio
    
#     def resultados(self):
#         print(f"El área del círculo es: {self.calcular_area()}")
#         print(f"El perímetro del círculo es: {self.calcular_perimetro()}")

# # Programa principal
# circulo = Circulo(3)
# circulo.resultados()

"""
Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
balanceados usando una pila.
"""
# #Definición de  función
# def verificar_balanceado(cadena):
#     pila = []
#     pares = {')': '(', '}': '{', ']': '['}
    
#     for char in cadena:
#         if char in pares.values():
#             pila.append(char)
#         elif char in pares.keys():
#             if not pila or pila[-1] != pares[char]:
#                 return False
#             pila.pop()
    
#     return len(pila) == 0

# #Programa principal
# cadena = "{[()]}"
# print(f"La cadena '{cadena}' está balanceada: {verificar_balanceado(cadena)}")
# cadena = "{[(])}"
# print(f"La cadena '{cadena}' está balanceada: {verificar_balanceado(cadena)}")

"""
7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
● Agregar clientes (encolar).
● Atender clientes (desencolar).
● Mostrar el siguiente cliente en la fila.
"""
# #Definición de  funciónes
# def agregar_cliente(cola, cliente):
#     cola.append(cliente)

# def atender_cliente(cola):
#     if cola:
#         return cola.pop(0)
#     else:
#         return "No hay clientes en la fila."
    
# def  mostrar_siguiente_cliente(cola):
#     if cola:
#         return cola[0]
#     else:
#         return "No hay clientes en la fila."
    
# #programa principal
# cola = []
# agregar_cliente(cola, "Cliente 1")
# agregar_cliente(cola, "Cliente 2")
# agregar_cliente(cola, "Cliente 3")
# atender_cliente(cola)
# print("Siguiente cliente en la fila:", mostrar_siguiente_cliente(cola))


"""
8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
los valores almacenados.
"""
# # Definición de la clase Nodo 
# class Nodo:
#     def __init__(self, dato):
#         self.dato = dato  
#         self.siguiente = None  

# class ListaEnlazada:
#     def __init__(self):
#         self.cabeza = None  

#     def insertar(self, dato):
#         nuevo_nodo = Nodo(dato)
#         nuevo_nodo.siguiente = self.cabeza
#         self.cabeza = nuevo_nodo

#     def mostrar(self):
#         actual = self.cabeza
#         while actual:
#             print(actual.dato, end=' ➡️ ')
#             actual = actual.siguiente
#         print("None")

# # Programa principal
# lista = ListaEnlazada()
# lista.insertar(3)
# lista.insertar(2)
# lista.insertar(1)
# lista.mostrar()  

"""
9) Dada una lista enlazada, implementa una función para invertirla.
Ejemplo de entrada y salida:
Lista original: 1 ➡️ 2 ➡️ 3 ➡️ None
Lista invertida: 3 ➡️ 2 ➡️ 1 ➡️ None
"""
# # Definición de la clase Nodo
# class Nodo:
#     def __init__(self, dato):
#         self.dato = dato 
#         self.siguiente = None  

# class ListaEnlazada:
#     def __init__(self):
#         self.cabeza = None  

#     def insertar(self, dato):
#         nuevo_nodo = Nodo(dato)
#         nuevo_nodo.siguiente = self.cabeza
#         self.cabeza = nuevo_nodo

#     def mostrar(self, mensaje):
#         print(mensaje)
#         actual = self.cabeza
#         while actual:
#             print(actual.dato, end='  ➡️  ')
#             actual = actual.siguiente
#         print("None")

#     # Definición de la función para invertir la lista
#     def invertir(self):
#         anterior = None
#         actual = self.cabeza
#         while actual:
#             siguiente = actual.siguiente
#             actual.siguiente = anterior
#             anterior = actual
#             actual = siguiente
#         self.cabeza = anterior    

# # 🚀 Probemos nuestra lista enlazada
# lista = ListaEnlazada()
# lista.insertar(3)
# lista.insertar(2)
# lista.insertar(1)
# lista.mostrar("Lista original: ")
# lista.invertir()
# lista.mostrar("Lista invertida: ")
