### MongoDB Client ###

# Descarga versión de MongoDB Community Server: https://www.mongodb.com/try/download/community
# Instalación: https://www.mongodb.com/docs/manual/installation/
# Módulo para conectarse a MongoDB: pip install pymongo
# Ejecutar MongoDB: mongod --dbpath "path/to/db"
# Conexión a MongoDB en local: mongodb://localhost:27017/


from pymongo import MongoClient

db_client = MongoClient()
