#No pueden empezar ni contener carácteres especiales
#No pueden empezar por números
#No pueden ser llamadas igual que las palabras claves reservadas en Python
#No pueden contener espacios
#No pueden contener símbolos especiales como @, #, $, etc.
#No pueden ser iguales a los nombres de las funciones integradas de Python
#'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
#'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#tipos de variables
# str: Cadenas de texto
# int: Números enteros
# float: Números decimales
# bool: Valores booleanos (True o False)

# Ejercicio 1: Crea una variable que contenga tu nombre

tuNombre = "Andres" #declaracion de variable tipo string

# Ejercicio 2: Crea una variable que contenga tu edad
edad = 30 #declaracion de variable tipo int
# Ejercicio 3: Crea una variable que contenga tu altura en metros
altura = 1.63
# Ejercicio 4: Crea una variable que contenga si eres estudiante (True o False)
estudiante = True

#funcion import 
import math as mt #as es un alias para math

mt.tan #función tangente
mt.pi #número pi
from math import pi #importar solo pi de math
from math import pi as valorpi #importar pi y renombrarlo como valorpi

valorpi = mt.pi
print(valorpi) #imprime el valor de pi

#declaracion de multiples variables
numeroint, numeroflot, cadenaString = 5, 3.2, "Hola Mundo"
print(numeroint, numeroflot, cadenaString)

#intercambio de valores entre variables
numeroint = 20
numeroflot = 10.5
print("despues del cambio de valor: a =", numeroint, ", b =", numeroflot)


#operaciones con variables
suma = numeroint + numeroflot
resta = numeroint - numeroflot
multiplicacion = numeroint * numeroflot
division = numeroint / numeroflot
exponente = numeroint ** 2
modulo = numeroint % 3
division_entera = numeroint // 3
print('suma:', suma, "resta:", resta, "multiplicacion:", multiplicacion, "division:", division, "exponente:", exponente, "modulo:", modulo, "division_entera:", division_entera)

#variable de tipo string
string1 = "esto es un string" #comillas dobles
string2 = 'esto es otro string' #comillas simples
#nota evitar usar acentos en las cadenas de texto pueden generar errores

#strings literales, el hecho de que el contenido de las variables del tipo string vaya entre comillas conlleva a que algunos caracteres deban ser tratados de forma especial aqui algunos ejemplos
#\\ para insertar una barra invertida
#\' para insertar una comilla simple
#\" para insertar una comilla doble
#\n para insertar un salto de linea
#\t para insertar una tabulacion

#operaciones con cadenas de texto 
cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2 #que sucede si no colocamos " "?
print("Cadena concatenada:", cadena_concatenada)
print("Cadena repetida: ", cadena1*3)

#tambien podemos usar suma 
Nombre="pepe"
print("Hola " + Nombre)

#funcion str() convierte a string variables de otros tipos
edad = 25
print("Tengo " + str(edad) + " años")

#metodo format() para formatear cadenas de texto
nombre = "Ana"  
edad = 28
altura = 1.70
print("Me llamo {}, tengo {} años y mido {} metros.".format(nombre, edad, altura))
#funcion len() para conocer la longitud de una cadena de texto
longitud_cadena = len(cadena_concatenada)
print("Longitud de la cadena concatenada:", longitud_cadena)

#acceder a caracteres individuales de una cadena
primer_caracter = cadena1[0] #indexacion empieza en 0
print("Primer caracter de cadena1:", primer_caracter)   
ultimo_caracter = cadena1[-1] #indexacion negativa empieza en -1 empezando desde el final
print("Ultimo caracter de cadena1:", ultimo_caracter)

#metodos para trabajar con cadenas de texto
cadena_mayusculas = cadena1.upper() #convierte a mayusculas
print("Cadena en mayusculas:", cadena_mayusculas)
cadena_minusculas = cadena2.lower() #convierte a minusculas
print("Cadena en minusculas:", cadena_minusculas)   
cadena_capitalizada = cadena1.capitalize() #primera letra en mayuscula
print("Cadena capitalizada:", cadena_capitalizada)
cadena_titulo = cadena2.title() #primera letra de cada palabra en mayuscula
print("Cadena en formato titulo:", cadena_titulo)
cadena_reemplazada = cadena_concatenada.replace("Hola", "Adios") #reemplaza una subcadena por otra
print("Cadena con reemplazo:", cadena_reemplazada)


#tipos de datos numericos
numero_entero = 10 #int
numero_decimal = 3.14 #float    
numero_complejo = 2 + 3j #complex
#para conocer el tipo de dato de una variable usamos la funcion type()
print("Tipo de dato entero:", type(numero_entero))
print("Tipo de dato decimal:", type(numero_decimal))
print("Tipo de dato complejo:", type(numero_complejo))

#variables booleanas y operaciones logicas

#booleanos pueden ser True o False
es_mayor = numero_entero > 5 #True
es_menor = numero_entero < 5 #False
#operadores logicos: and, or, not
A=True
B=False
print(not A) #False
#operador and
print(A and B) #False
#operador or
print(A or B) #True
#operadores de comparacion: ==, !=, >, <, >=, <=
#multiples comparaciones simultaneas
edad = 20
print(edad>=16) and (edad <=40)

#SEGUNDA CLASE 

#listas, tuplas y diccionarios

#listas son colecciones ordenadas y mutables
lista_frutas = ["manzana", "banana", "naranja"]  # Lista de frutas
print("Lista de frutas:", lista_frutas)

# Acceder a elementos de la lista
print("Primera fruta:", lista_frutas[0])  # Accede al primer elemento
print("Ultima fruta:", lista_frutas[-1])  # Accede al último elemento
#consulta todos los elementos de la lista
for fruta in lista_frutas:
    print("Fruta:", fruta)  # Imprime cada fruta en la lista

# Modificar un elemento de la lista
lista_frutas[1] = "kiwi"  # Cambia "banana" por "kiwi"
print("Lista de frutas modificada:", lista_frutas)

# Añadir un elemento a la lista
lista_frutas.append("uva")  # Añade "uva" al final de la lista
print("Lista de frutas después de añadir uva:", lista_frutas)

# Eliminar un elemento de la lista
lista_frutas.remove("naranja")  # Elimina "naranja" de la lista
print("Lista de frutas después de eliminar naranja:", lista_frutas)
del lista_frutas[1]  # Elimina un elemento por indice
print("Lista de frutas después de eliminar el segundo elemento:", lista_frutas)
lista_frutas.insert(1, "pera")  # Inserta "pera" en la posición 1
print("Lista de frutas después de insertar pera:", lista_frutas)
lista_frutas.pop()  # Elimina el último elemento de la lista
print("Lista de frutas después de eliminar el último elemento:", lista_frutas)
lista_frutas.clear()  # Elimina todos los elementos de la lista
print("Lista de frutas después de limpiar:", lista_frutas)



#tuplas son colecciones ordenadas e inmutables
tupla_frutas = ("manzana", "banana", "naranja")  # Tupla de frutas
print("Tupla de frutas:", tupla_frutas)

#consulta todos los elementos de la tupla
for fruta in tupla_frutas:
    print("Fruta:", fruta)  # Imprime cada fruta en la tupla


# Acceder a elementos de la tupla
print("Primera fruta de la tupla:", tupla_frutas[0])  # Accede al primer elemento
# No se pueden modificar elementos de la tupla, pero se pueden acceder a ellos

#diccionarios son colecciones desordenadas de pares clave-valor
diccionario_frutas = {
    "manzana": 1.5,
    "banana": 0.8,
    "naranja": 1.2
}  # Diccionario de frutas con precios
print("Diccionario de frutas:", diccionario_frutas)

# Acceder a un valor por su clave
print("Precio de la manzana:", diccionario_frutas["manzana"])  # Accede al valor de la clave "manzana"
# Consulta todos los pares clave-valor del diccionario
for fruta, precio in diccionario_frutas.items():
    print("Fruta:", fruta, "Precio:", precio)  # Imprime cada par clave-valor en el diccionario


# Añadir un nuevo par clave-valor al diccionario
diccionario_frutas["kiwi"] = 2.0  # Añade "kiwi" con su precio
print("Diccionario de frutas después de añadir kiwi:", diccionario_frutas)

# Eliminar un par clave-valor del diccionario
del diccionario_frutas["naranja"]  # Elimina "naranja" del diccionario
print("Diccionario de frutas después de eliminar naranja:", diccionario_frutas)


#solicitar datos al usuario
nombre = input("Como te llamas?:  ")  # Solicita al usuario que ingrese su nombre
print("Hola, " + nombre + "!")  # Saluda al usuario por su nombre
edad = int(input("Cual es tu edad?: "))  # Solicita al usuario que ingrese su edad y la convierte a entero


#operadores de decision 

#condicionales if, elif, else
if edad < 18:
    print("Eres menor de edad") 
elif edad >= 18 and edad < 65:
    print("Eres mayor de edad")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Edad no válida")

#operadores anidados
name="andres"
if edad < 18:
    print("Eres menor de edad") 
    if name.startswith("A") or name.startswith("a"):
        print( "eres mauor de edad pues tienes {} años y tu nombre, que es {}, empieza por A".format(edad, name))
    else:
        print("eres mayor de edad pues tienes {} años".format(edad))
else:
    print("eres muy joven")

#operadores de iteracion 
#bucle while mientras la condicion sea verdadera el bucle se ejecuta
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementa el contador en 1
#debemos tener cuidado con los bucles infinitos, si la condicion nunca se vuelve falsa el bucle se ejecutara indefinidamente
#comando break para salir del bucle
contador = 0
while True:  # Bucle infinito
    print("Contador:", contador)
    contador += 1
    if contador >= 5:
        break  # Sale del bucle cuando contador es mayor o igual a 5
#combinacion de bucle while...else
i = 10
print("preparados para la cuenta regresiva")
while i > 0:
    print(i)
    i -= 1
else:
    print("¡Despegue!")
#bucle for para iterar sobre una secuencia (lista, tupla, cadena de texto, etc.)
for i in range(5):  # Itera desde 0 hasta 4 
    print("Iteración:", i)



#funciones
#definicion de funciones con def

#funcion sin valor de retorno
def saludar(nombre):
    print("Hola, " + nombre + "!") #cuerpo de la funcion

saludar("Andres") #llamada a la funcion


#funcion con valor de retorno
def sumar(a, b):
    return a + b  # Devuelve la suma de a y b

resultado = sumar(3, 5)  # Llama a la función y almacena el resultado
print("Resultado de la suma:", resultado)







