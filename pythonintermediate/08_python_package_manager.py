### Python Package Manager ###

# Python Package Manager (pip)
# PIP https://pypi.org/project/pip/

# import pandas  # pip install pandas
from mypackage import arithmetics
import requests  # pip install requests
import numpy  # pip install numpy
# import matplotlib  # pip install matplotlib


# pip es el gestor de paquetes de Python, que permite instalar y gestionar librerías y dependencias de Python.
# pip install <package_name>  # Instalar un paquete
# pip uninstall <package_name>  # Desinstalar un paquete
# pip list  # Listar todos los paquetes instalados
# pip show <package_name>  # Mostrar información sobre un paquete
# pip freeze  # Listar todos los paquetes instalados y sus versiones
# pip freeze > requirements.txt  # Guardar la lista de paquetes instalados en un archivo
# pip install -r requirements.txt  # Instalar los paquetes listados en un archivo requirements.txt
# pip search <package_name>  # Buscar un paquete en el índice de paquetes de Python
# pip check  # Verificar si hay dependencias rotas
# pip install --upgrade <package_name>  # Actualizar un paquete
# pip install --upgrade pip  # Actualizar pip
# pipenv install <package_name>  # Instalar un paquete en un entorno virtual
# pipenv uninstall <package_name>  # Desinstalar un paquete en un entorno virtual
# pipenv shell  # Activar el entorno virtual
# pipenv install --dev <package_name>  # Instalar un paquete de desarrollo
# pipenv install --dev  # Instalar todos los paquetes de desarrollo
# pipenv graph  # Mostrar el grafo de dependencias
# pipenv lock  # Bloquear las dependencias en un archivo Pipfile.lock
# pipenv update  # Actualizar las dependencias
# pipenv run <command>  # Ejecutar un comando en el entorno virtual
# pipenv check  # Verificar si hay dependencias rotas
# pipenv --venv  # Mostrar la ruta del entorno virtual
# pipenv --rm  # Eliminar el entorno virtual
# pipenv --where  # Mostrar la ruta del proyecto
# pipenv --version  # Mostrar la versión de pipenv
# pipenv --help  # Mostrar la ayuda de pipenv

# pip install pandas  # Instalar pandas
# pip install numpy  # Instalar numpy
# pip install matplotlib  # Instalar matplotlib

print(numpy.__version__)

numpy_array = numpy.array([33, 44, 25, 12, 11, 56, 78])
print(numpy_array)

# Modulo de aritmética

print(arithmetics.sum_two_values(1, 4))
