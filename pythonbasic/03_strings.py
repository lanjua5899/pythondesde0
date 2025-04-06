### Strings ###
my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de string"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_escape_string = "\\tEste es un String \\n espaciado"
print(my_escape_string)

print('Espero que estes disfrutando del Python Challenge. \nLo estás?')
print('Dias\tTemas\tEjercicios')
print('Dia 1\t5\t5')
print('Dia 2\t6\t20')
print('Dia 3\t5\t23')
print('Dia 4\t1\t35')
print('Esto es una barra inversa (\\)')
print('En todo lenguaje de programación se empieza con \"Helo, World!"')

# Formateo

name, surname, age = "Juan", "Perez Lang", 33

print("Mi nombre es {} {} y mi edad es {}".format(
    name, surname, age))  # Se usa {} para objetos
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py"))
print("Py" == "py")  # No es lo mismo
