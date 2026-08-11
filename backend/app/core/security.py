from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib.hashers.bcrypt import BcryptHasher

from app.core.config import Settings

password_hash = PasswordHash(
    (
        Argon2Hasher(),
        BcryptHasher()
    )
)

ALGORITHMS="HS256"

def create_access_token(subject:str | Any,expire_delta:timedelta) -> str:
    expire=datetime.now(UTC)+expire_delta
    to_encode={"sub":str(subject),"exp":expire}
    jwt_encode=jwt.encode(to_encode,Settings.SECRET_KEY,ALGORITHMS)
    return jwt_encode

def verify_password(plain_password:str,hash_password:str) -> tuple[bool,str | None]:
    return password_hash.verify_and_update(plain_password,hash_password)

def get_password_hash(password:str) ->str:
    return password_hash.hash(password)