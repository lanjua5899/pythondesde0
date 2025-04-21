### Users API con autenticación OAuth2 básica ###

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "lanjua": {
        "username": "lanjua",
        "full_name": "Juan Perez Lang",
        "email": "lanjua@lanjua.com",
        "disabled": False,
        "password": "123456"
    },
    "lanjua2": {
        "username": "lanjua2",
        "full_name": "Juan Perez Lang 2",
        "email": "lanjua2@lanjua.com",
        "disabled": True,
        "password": "654321"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def current_user(token: str = Depends(oauth2)):
    """
    Función para obtener el usuario actual a partir del token.
    """
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas", headers={"www-Authenticate": "Bearer"}
        )


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para iniciar sesión y obtener un token de acceso."""
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto"
        )
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=400, detail="La contraseña no es correcta"
        )
    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    """
    Endpoint para obtener información del usuario autenticado.
    """
    return user
