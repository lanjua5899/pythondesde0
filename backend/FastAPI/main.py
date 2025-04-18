### FastAPI app ###

# FastAPI es un framework para construir APIs con Python 3.6+ basado en tipos de datos estándar de Python.
# FastAPI es rápido (alto rendimiento), fácil de usar, y tiene una gran documentación.
# FastAPI es ideal para construir APIs RESTful y microservicios.

# Instalación de FastAPI: pip install "fastapi[standard]"

from typing import Union

from fastapi import FastAPI
from routers import users, products

app = FastAPI()

# Routers
app.include_router(users.router)  # Incluye el router de usuarios
app.include_router(products.router)

# Url local: http://127.0.0.1:8000


@app.get("/")
async def read_root():
    return {"mensaje": "Hola FastAPI!"}

# Url local: http://127.0.0.1:8000/items/5?q=somequery


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Url local: http://127.0.0.1:8000/url


@app.get("/url")
async def read_url():
    return {"url": "http://linktree.com/juanmathiasperezlang"}

# Iniciar el servidor: fastapi dev main.py --reload
# Detener el servidor: Ctrl + C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
