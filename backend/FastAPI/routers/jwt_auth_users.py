### Users API con autenticación JWT ###

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext


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
