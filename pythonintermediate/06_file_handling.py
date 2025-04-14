### Manejo de ficheros ###

import csv
import json
import os

# .txt file

# Sintaxis: open("ruta del fichero", "modo de apertura", encoding='utf-8')
# Modos de apertura:
# r: read (leer)
# w: write (escribir)
# a: append (añadir)
# r+: read and write (leer y escribir)
# w+: write and read (escribir y leer)
# x: exclusive creation (creación exclusiva)
# x+: exclusive creation and read (creación exclusiva y lectura)
# Crear un fichero. Si el fichero ya existe, se sobrescribirá

# Leer, escribir y sobreescribir un fichero
txt_file = open("pythonintermediate/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Juan\nMi apellido es Perez Lang\n33 años\nY mi lenguaje preferido es Python")

# Posiciona el cursor al inicio del fichero
txt_file.seek(0)

# Lee e imprime el contenido del fichero
print(txt_file.read())

# Lee e imprime 10 caracteres desde el inicio del fichero
txt_file.seek(0)
print(txt_file.read(10))

# Lee e imprime el resto de la línea actual desde la posición 11
print(txt_file.readline())

# Lee e imprime las lineas restantes del fichero
for line in txt_file.readlines():
    print(line)

# Escribe una nueva línea en el fichero
txt_file.write("\nSoy Cloud Engineer autodidacta\n")

# Posiciona el cursor al inicio del fichero, lee e imprime todo su contenido
txt_file.seek(0)
print(txt_file.read())

# Cierra el fichero
txt_file.close()

# Agrega una nueva línea en el fichero
with open("pythonintermediate/my_other_file.txt", "w") as my_other_file:
    my_other_file.write("Hola, soy otro fichero\n")

# Elimina el fichero si existe
# if os.path.exists("my_file.txt"):
#    os.remove("my_file.txt")

# .json file
# Crear un fichero JSON
json_file = open("pythonintermediate/person.json", "w+")

# Escribir en el fichero JSON

json_test = {
    "name": "Juan",
    "surname": "Perez Lang",
    "age": 33,
    "languages": ["Python", "JavaScript"],
    "occupation": "Cloud Engineer",
    "is_autodidact": "True"
}


# El método dump() convierte un objeto Python en una cadena JSON y lo escribe en un fichero
# El método loads() convierte una cadena JSON en un objeto Python
# El método dumps() convierte un objeto Python en una cadena JSON
# El método load() convierte un fichero JSON en un objeto Python


# Convertir la cadena JSON en un objeto Python
json.dump(json_test, json_file, indent=4)

# Cerrar el fichero JSON
json_file.close()

with open("pythonintermediate/person.json", "r") as json_file:
    # Cargar el fichero JSON en un objeto Python
    json_test = json.load(json_file)

# .csv file
# Crear un fichero CSV

csv_file = open("pythonintermediate/person.csv", "w+", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languages",
                    "occupation", "is_autodidact"])
csv_writer.writerow(
    ["Juan", "Perez Lang", 33, ["Python", "JavaScript"], "Cloud Engineer", True])

# Cerrar el fichero CSV
csv_file.close()

# Leer el fichero CSV
with open("pythonintermediate/person.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
