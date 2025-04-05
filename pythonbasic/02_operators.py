### Operadores Aritméticos ###

# Operaciones con enteros

print(3 + 4)  # Suma
print(3 - 4)  # Resta
print(3 * 4)  # Multiplicación
print(3 / 4)  # División
print(10 % 3)  # Módulo (resto de la división)
print(10 // 3)  # División entera
print(2 ** 3)  # Exponente
print(2 ** 3 + 3 - 7 / 1 // 4)  # Operaciones combinadas

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")  # Concatenación
print("Hola" + str(5))  # Concatenación con conversión de tipo

# Operaciones mixtas
my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" >= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores lógicos ###

# Basado en el Álgebra de Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
