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

tuNombre = "Andres"
# Ejercicio 2: Crea una variable que contenga tu edad
edad = 30
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
print(valorpi*2) #imprime el valor de pi por 2

#declaracion de multiples variables
numeroint, numeroflot, cadenaString = 5, 3.2, "Hola"
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
print("suma:", suma, "resta:", resta, "multiplicacion:", multiplicacion, "division:", division, "exponente:", exponente, "modulo:", modulo, "division_entera:", division_entera)

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


#tipos de datos numericos
numero_entero = 10 #int
numero_decimal = 3.14 #float    
numero_complejo = 2 + 3j #complex
#para conocer el tipo de dato de una variable usamos la funcion type()
print("Tipo de dato entero:", type(numero_entero))
print("Tipo de dato decimal:", type(numero_decimal))
print("Tipo de dato complejo:", type(numero_complejo))





