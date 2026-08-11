from ctypes.wintypes import HHOOK
import token
from app.response.loginRes import Token
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import SessionDep


router = APIRouter(tags=["login"])

@router.post("/login/access-token")
def login_access_toker(session:SessionDep, form_data: Annotated[OAuth2PasswordRequestForm,Depends()]) -> Token:
    