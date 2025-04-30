### MongoDB Client ###

# Descarga versión de MongoDB Community Server: https://www.mongodb.com/try/download/community
# Instalación: https://www.mongodb.com/docs/manual/installation/
# Módulo para conectarse a MongoDB: pip install pymongo
# Ejecutar MongoDB: mongod --dbpath "path/to/db"
# Conexión a MongoDB en local: mongodb://localhost:27017/


from pymongo import MongoClient

# Descomenta la línea de conexión a MongoDB que no se necesite

# Base de datos local MongoDB
db_client = MongoClient().local

# Base de datos en MongoDB Atlas
# db_client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/test?retryWrites=true&w=majority")

# Despliegue MongoDB en Docker:
# docker run --name mongodb -d -p 27017:27017 -v /path/to/db:/data/db mongo
