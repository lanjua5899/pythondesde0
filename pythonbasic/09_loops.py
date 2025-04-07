### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es igual o mayor que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (33, 1.73, "Juan", "Perez Lang", "Juan")

for element in my_tuple:
    print(element)

my_set = {"Juan", "Perez Lang", 33}

for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Juan",
    "Apellido": "Perez Lang",
    "Edad": 33,
    "Lenguajes": {"Python", "Java", "C#"},
    1: 1.73}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El loop for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El loop for para diccionario ha finalizado")
