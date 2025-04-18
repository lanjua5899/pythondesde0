### Users API ###
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Iniciar el servidor:

router = APIRouter()

# Entidad de usuario


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

# Crear un usuario


users_list = [User(id=1, name="Juan", surname="Perez Lang", age=33, url="https://www.linktree.com/juanmathiasperezlang"),
              User(id=2, name="Elias", surname="Varon", age=37,
                   url="https://www.instagram.com/eav"),
              User(id=3, name="Franco", surname="Costa", age=29, url="https://www.amgmadrid.com/")]


@router.get("/users")
async def usersjson():  # JSON de ejemplo
    return [{"name": "Juan", "surname": "Perez Lang", "age": 33, "url": "https://www.linktree.com/juanmathiasperezlang"},
            {"name": "Elias", "surname": "Varon", "age": 37,
                "url": "https://www.instagram.com/eav"},
            {"name": "Franco", "surname": "Costa", "age": 29, "url": "https://www.amgmadrid.com/"}]


@router.get("/users")
async def users():
    return users_list


@router.get("/user/{id}")  # Path o endpoint
async def user(id: int):
    return search_user(id)


@router.get("/user/")  # Query
async def user(id: int):
    return search_user(id)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
