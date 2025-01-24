# Ejemplo básico de uso de pint

mensaje = "Hola, mundo"
print (mensaje)

# Formateo de cadenas

nombre = "Jheyson"
edad = 32
print(f"Mi nombre es {nombre} y tengo {edad} años")

# Cambiando el carácter al final de la salida

print ("Hola", end= " ")
print ("mundo!")

# Especificando un separador diferente

nombre = "Jheyson"
edad = 32
print(nombre, edad, sep="-")

# Ejemplo de declaración y asignación de variables

nombre = "Jheyson"
edad = 32
altura = 1.69
es_estudiante = False 

print (f"Mi nombre es {nombre}, tengo {edad} años, mido {altura} m y soy estudiante: {es_estudiante}")

# Asignación de valores de la declaración

ciudad = "Fresno Tolima"
población = 32165

# Reasignación de valores

ciudad = "Manizales"
población = 457022

# convenciones de nombres

nombre_completo = "Jheyson Galvis"
dias_vivido = 12.004
print(f"Mi nombre es {nombre_completo} y tengo {dias_vivido} días vividos")

# Tipos de variables dinámicos

variable_dinamica = 10
print(variable_dinamica) # salida: 10

variable_dinamica = "Hola"
print(variable_dinamica) # salida: Hola

print(type(variable_dinamica))

# Enteros

entero_positivo = 10
entero_negativo = -5

print(entero_positivo)
print(entero_negativo)

# Flotantes

flotante_1 = 3.14
flotante_2 = -0.5

print(flotante_1)
print(flotante_2)

# operaciones con enteros y flotantes

resultado_suma = entero_positivo + flotante_1 
resultado_multiplicacion = entero_negativo * flotante_2

print(resultado_suma)
print(resultado_multiplicacion)

# cadenas

cadena_simple = 'Hola, mundo!'
cadena_doble = "Python es divertido"

# Concatenación de cadenas
saludo_completo = cadena_simple + '  ' + cadena_doble

print(saludo_completo)

# Ejercicio Operaciones con Cadenas:

# 1. Crea dos variables de cadenas llamadas cadena1 y cadena 2

cadena1 = "Jheyson"
cadena2 = "Galvis"  
print(cadena1 + " " + cadena2)

# 2. Concatena las dos cadenas y guarda el resultado de una nueva variable  

nueva_cadena = cadena1 + " " + cadena2
print(nueva_cadena)

# 3. Imprime la longitud de la cadena resultante 

print(len(nueva_cadena))

# Ejercicio Formato de Cadenas: 

# 1. Crea una variable con tu nombre

mi_nombre = "Jheyson"
print (mi_nombre)

# 2. Utiliza el formato de cadena para imprimir un mensaje de bienvenida personalizado

mi_nombre = "Jheyson"
print (f"Bienvenido, {mi_nombre} a mi programa de Python")  

# Ejercicio Subcadenas y métodos 

# 1. Crea una cadena larga y utiliza el método split() para dividirla en una lista de palabras

cadena_larga = "Estoy aprendiendo a programar en Python"
palabras = cadena_larga.split()
print(palabras)

# 2. Encuentra e imprime la posición de una subcadena especifica

cadena_larga = "Estoy aprendiendo a programar en Python"
posicion_subcadena = cadena_larga.find("programar")
print(posicion_subcadena)

# Ejercicios Métodos de Mayúsculas y Minúsculas

# 1. Crea una cadena en minúsculas y conviertelas a mayúsculas usando los métodos upper () y lower ().

cadena = "Hola, mundo!"
cadena_minusculas = cadena.lower()
cadena_mayusculas = cadena.upper()
print(cadena_minusculas)
print(cadena_mayusculas)

# Ejercicios Operaciones Aritméticas:

# 1. Crea dos variables, a y b, con valores numéricos.

a = 10
b = 5
print(a + b)    

# 2. Realiza operaciones aritméticas básicas (suma, resta, multiplicación, división, exponente) con estas variables e imprime los resultados.

a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

# Ejercición de División y Módulo

# 1. Divide dos números enteros y guarda el resultado en una variable llamada resultado. 

a = 10
b = 3
resultado = a / b
print("El resultado de la divisió es:", resultado)

# 2. Utiliza el operador módulo (%) para obtener el residuo de la división e imprímelo.

a = 10
b = 3
residuo = a % b
print("El residuo de la divisió es:", residuo)

# Ejercicios de Precisión de Flotantes:

# 1. Crea una variable c con un valor flotante

c = 3.14159
print(f"El valor de c es: {c}")

# 2. Realiza operaciones aritméticas que involucren flotantes y enteros.

a = 10
b = 3.14
resultado = a * b
print(f"El resultado de la multiplicación es: {resultado}")

# 3. ¿Cómo se manejan las operaciones mixtas?

a = 10
b = 3.14
resultado = a * b
print(f"El resultado de la multiplicación es: {resultado}")

print(type(resultado))
# Python convierte automáticamente el entero en un flotante para realizar la operación.
# El tipo de resultado será el tipo más general involucrado (en este caso, float)