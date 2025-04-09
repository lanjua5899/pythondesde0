### Clases ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):  # Constructor
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.__name} está caminando")


my_person = Person("Juan", "Perez Lang")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Juan", "Perez Lang", "Lanjua")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Juanito"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
