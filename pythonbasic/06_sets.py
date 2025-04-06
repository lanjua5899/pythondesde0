### Sets ###

# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Juan", "Perez Lang", 33}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("Lanjua")
print(my_other_set)  # Un set es una estructura desordenada

my_other_set.add("Lanjua")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Perez Lang" in my_other_set)
print("Juani" in my_other_set)

# Eliminación

my_other_set.remove("Juan")
print(my_other_set)

my_other_set.clear()  # Limpia los elementos del set
print(my_other_set)

del my_other_set  # Elimina directamente el objeto
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Juan", "Perez Lang", 33}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))
