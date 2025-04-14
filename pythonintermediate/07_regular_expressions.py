### Expresiones regulares ###

# Las expresiones regulares son una herramienta poderosa para buscar y manipular texto.
# Permiten definir patrones complejos y realizar operaciones como búsqueda, reemplazo y validación de cadenas.
# En Python, el módulo 're' proporciona funciones para trabajar con expresiones regulares.

import re

# Ejemplo de uso de expresiones regulares
# Definir una cadena de texto
my_string = "Hola, mi número es 123-456-7890"
my_other_string = "Hola, mi número es 1234567890"

# match y search
# match busca una coincidencia al inicio de la cadena
# search busca una coincidencia en cualquier parte de la cadena
match = re.match("Esto es un texto", my_string)
print(match)  # None, no hay coincidencia al inicio de la cadena
# Buscar una coincidencia en la cadena
match = re.search(r"número", my_other_string)
print(match)  # <re.Match object; span=(9, 15), match='número'>
# Buscar todas las coincidencias en la cadena
matches = re.findall(r"\d+", my_string)
print(matches)  # ['123', '456', '7890']

# span
# Obtener el inicio y el final de la coincidencia
# span es una tupla que contiene el inicio y el final de la coincidencia
span = match.span()
print(span)  # (9, 15), posición de la coincidencia
start, end = span
print(start, end)  # 9 15

# split
# Dividir una cadena usando un patrón
# Dividir la cadena en partes usando el patrón "-"
# Esto es útil para separar números de teléfono o fechas
# En este caso, se divide la cadena en partes usando el patrón "-"
# El resultado es una lista de cadenas
print(re.split("-", my_string))  # ['Hola, mi número es 123-456-7890']

# sub
# Reemplazar una coincidencia en la cadena
# Reemplazar la primera coincidencia en la cadena
replaced_string = re.sub(r"\d+", "X", my_string, count=1)
print(replaced_string)  # "Hola, mi número es X-456-7890"

# Reemplazar todas las coincidencias en la cadena
replaced_string = re.sub(r"\d+", "X", my_string)
print(replaced_string)  # "Hola, mi número es X-X-X"


# Patrones de expresiones regulares
# Definir un patrón de expresión regular para buscar un número de teléfono
pattern = r"\d{3}-\d{3}-\d{4}"
# Buscar el patrón en la cadena
match = re.search(pattern, my_string)
print(match)  # <re.Match object; span=(19, 31), match='123-456-7890'>
# Validar una dirección de correo electrónico
email = "perezlangjuan@gmail.com"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# <re.Match object; span=(0, 23), match='perezlangjuan@gmail.com'>
print(re.match(email_pattern, email))
# <re.Match object; span=(0, 23), match='perezlangjuan@gmail.com'>
print(re.search(email_pattern, email))
print(re.findall(email_pattern, email))  # ['perezlangjuan@gmail.com']
