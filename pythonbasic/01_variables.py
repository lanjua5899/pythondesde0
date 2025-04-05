# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_variable_to_str = str(my_int_variable)
print(my_int_variable_to_str)
print(type(my_int_variable_to_str))

my_float_variable = 5.5
print(my_float_variable)

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable,
      my_float_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))  # Longitud de la cadena

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Juan", "Perez Lang", "Lanjua", 33
print("Me llamo:", name, surname, ". Mi edad es:", age, "y mi apodo es", alias)

# Inputs
name = input("¿Cuál es tu nombre? ")
age = input("¿Cuántos años tienes? ")
print(name)
print(age)

# Cambiar el tipo de dato de una variable
name = 33
age = "Juan"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
address = True
address = 1.2
print(type(address))
