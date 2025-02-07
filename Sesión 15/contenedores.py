# ------------------------------Página 3-----------------------------
# Contenedores
#Listas
# las listas van en corchetes []
pokemones_ash = ["pikachu", "charmander", "squirtle", "bulbasaur"]
# Los elementos de una lista se enumeran del 0 al adelante
print(pokemones_ash[0])
# índices y acceso a elementos: los elementos de una lista se enumeran desde 
# el 0 en adelante. Puedes acceder a un elemento mediante su índice:
primer_pokemon = pokemones_ash[0]
print(primer_pokemon)
segundo_pokemon = pokemones_ash[2]
print(segundo_pokemon)

# ------------------------------Página 4-----------------------------
# Longitud de una lista: Puedes obtener la longitud de una lista con la función len():
# la longitud es el número de elementos que contiene la lista
longitud = len(pokemones_ash)
print(longitud)
# Moficación de elementos: Las listas son mutables, lo que significa que puedes modificar
# sus elementos. Por ejemplo, puedes cambiar el tercer elemento de la lista:
pokemones_ash[2] = "Pidgey"
print(pokemones_ash)

# ------------------------------Página 5-----------------------------
# Operaciones comunes:
# Puedes realizar diversas operaciones con listas como agregar elementos, eliminar 
# elementos, extender una lista con otra, etc.

# Agregar elementos al final de la lista: 
print(pokemones_ash)
pokemones_ash.append("squirtle")
print(pokemones_ash)

# También podrías eliminar elementos por valor:
pokemones_ash.remove("squirtle")
print(pokemones_ash)

# Puedes extender una lista con otra:
pokemones_misty = ["starmie", "staryu", "psyduck"]
pokemones_ash.extend(pokemones_misty)
print(pokemones_ash)

# ------------------------------Página 6-----------------------------
# Slicing (recortando o rebanando)
# Puedes obtener una porción de una lista mediante el slicing:

print(pokemones_ash)
batalla = pokemones_ash[1:4]
print(batalla)

# Inclusión de elementos: Puedes verificar si un elemento se encuentra presente
# en una lista con el operador in:

print(pokemones_ash)
print("squirtle" in pokemones_ash)

# Las listas son herramientas versátiles en Python y se utilizan comúnmente para almacenar
# y manipular colecciones de datos.

# ------------------------------Página 7-----------------------------
# Tuplas

# Las tuplas son inmutables, lo que significa que no puedes modificar sus elementos.
# Puedes crear una tupla con la palabra clave tuple:

herramientas_de_goku = ("Báculo sagrado", "Nube voladora", "semillas del Ermitaño")
# índices y acceso a elementos: 
# Los elementos de una tupla también se enumeran desde 0 en adelante.
# Puedes acceder a un elemento mediante su índice:
herramienta_1_de_goku = herramientas_de_goku[0]
print(herramienta_1_de_goku)
herramienta_2_de_goku = herramientas_de_goku[1]
print(herramienta_2_de_goku)

# ------------------------------Página 8-----------------------------
# Longitud de una tupla: Puedes obtener la longitud de una tupla con la función len():
# la longitud es el número de elementos que contiene la tupla
longitud = len(herramientas_de_goku)
print(longitud)

# inmutabilidad
# Las tuplas son inmutables, lo que significa que no puedes modificar sus elementos. 
# herramientas_de_goku[0] = "Radar del dragon"
# print(herramientas_de_goku) # esto generará un error por lo tanto comenta la linea de arriba

# Empaquetado y desempaquetado
# Puedes empaquetar varios valores en una tupla y luego desempaquetar esos valores en 
# variables individuales:

print (herramientas_de_goku)
# Asignemos cada herramienta a una variable individual
herramienta_1_de_goku, herramienta_2_de_goku, herramienta_3_de_goku = herramientas_de_goku
# Ahora cada variable contiene un elmento de la tupla
print(herramienta_1_de_goku)
print(herramienta_2_de_goku)
print(herramienta_3_de_goku)

# Nota importante: El número de variables debe ser igual al número de elementos en la tupla.
# Si la tupla tiene 3 elementos, entonces debes asignar 3 variables.

# Solución con '*': Si no sabes cuántos elementos tiene la tupla, puedes usar '*':
herramienta_1_de_goku, *resto_de_herrramientas = herramientas_de_goku
print(herramienta_1_de_goku)
print(resto_de_herrramientas)


# ------------------------------Página 9-----------------------------
# Uso de Iteraciones: Las tuplas se utilizan comunmente en situaciones donde se necesita una
# estructura de datos inmutables, como claves de un diccionario o elementos de un conjunto.

# Tuplas anidadas: Puedes tener tuplas dentro de tuplas, creando así estructuras de datos 
# más complejas.

# Vamos a crear una tupla anidada que contenga sub-tuplas con información básica de las herramientas de Goku.

tupla_anidada = (("Báculo sagrado", "Nube voladora", "semillas del Ermitaño"), ("radar del dragón", "esfera de cuatro estrellas", "colita de mono"))

print(tupla_anidada)

# Las tuplas son útiles cuando necesitas asegurarte de que los datos no cambien durante la 
# ejecución del programa y se utilizan comúnmente donde la inmutabilidad es importante.


    
