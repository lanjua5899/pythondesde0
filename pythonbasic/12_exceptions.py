### Excepciones Handling ###

numberOne = 5
numberTwo = 1
# numberTwo = "1"

# Excepción base: try, except

try:
    print(numberOne + numberTwo)
    print("No hay error")
except:
    print("Error: No se puede sumar un número y una cadena")

# Flujo completo de una excepción: try, except, else, finally

try:
    print(numberOne + numberTwo)
    print("No hay error")
except:  # Se ejecuta si hay error
    print("Error: No se puede sumar un número y una cadena")
else:  # Se ejecuta si no hay error
    print("No ha habido error")
finally:  # Se ejecuta siempre
    print("Fin del flujo de excepciones")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No hay error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No hay error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
