### Users API con autenticación OAuth2 básica ###

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


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
        "password": "654321",
    }
}
