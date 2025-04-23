### Users API con autenticación JWT ###

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION_MINUTES = 1

router = APIRouter(prefix="/jwtauth", tags=["jwtauth"], responses={
                   status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


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
        "password": "$2a$12$GKsb8qx47Hf6zMXGLXlA9ODgcMCee.sDFZDoCCw0gr/Fj27tRMSmq"
    },
    "lanjua2": {
        "username": "lanjua2",
        "full_name": "Juan Perez Lang 2",
        "email": "lanjua2@lanjua.com",
        "disabled": True,
        "password": "$2a$12$/8CmHstBj8R8jjMG4EM21ehnLUC2kmfT.q06zl7B/fRTZ7HPWG3wu"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


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

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="La contraseña no es correcta"
        )

    access_token = {"sub": user.username, "exp": datetime.now(
    ) + timedelta(minutes=ACCESS_TOKEN_DURATION_MINUTES)}

    return {"access_token": access_token, "token_type": "bearer"}
