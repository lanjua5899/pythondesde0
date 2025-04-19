### Users API ###
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Iniciar el servidor:

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"message": "No encontrado"}})

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


@router.get("/")
async def usersjson():  # JSON de ejemplo
    return [{"name": "Juan", "surname": "Perez Lang", "age": 33, "url": "https://www.linktree.com/juanmathiasperezlang"},
            {"name": "Elias", "surname": "Varon", "age": 37,
                "url": "https://www.instagram.com/eav.ok"},
            {"name": "Franco", "surname": "Costa", "age": 29, "url": "https://www.amgmadrid.com/"}]


@router.get("/")
async def users():
    return users_list


@router.get("/user/{id}")  # Path o endpoint
async def user(id: int):
    return search_user(id)


@router.get("/user/")  # Query
async def user(id: int):
    # Si no se pasa el id lanzamos una excepción
    if id is None:
        raise HTTPException(status_code=400)
    return search_user(id)


@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if isinstance(search_user(user.id), User):
        # Si el usuario ya existe lanzamos una excepción
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)
    return user


@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha encontrado el usuario"}
    return user


@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "No se ha encontrado el usuario"}
