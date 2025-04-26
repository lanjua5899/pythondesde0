### Users DB API ###

from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/usersdb", tags=["usersdb"], responses={
                   status.HTTP_404_NOT_FOUND: {"descripción": "No encontrado"}})
