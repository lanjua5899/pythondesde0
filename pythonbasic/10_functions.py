### Funciones ###

# Definición

def my_function():
    print("Esto es una función")

# Llamada a la función


my_function()
my_function()
my_function()


# Parámetros

def sum_two_values(first_value, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Parámetros de entrada y salida


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Perez Lang", name="Juan")

# Función con parámetros de entrada/argumentos por defecto


def print_name_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_default("Juan", "Perez Lang")
print_name_default("Juan", "Perez Lang", "Lanjua")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "Lanjua")
print_upper_texts("Adiós")
