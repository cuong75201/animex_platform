from dataclasses import dataclass
from pwdlib import PasswordHash
from sqlalchemy import create_engine, select
from sqlmodel import Session
from app.models.enums import User_Role, User_gender,User_status
from app.models  import User
from app.core.config import setting
from pwdlib.hashers.argon2 import Argon2Hasher

engine = create_engine(setting.DATABASE_URL)
password_hash=PasswordHash((Argon2Hasher(),))

@dataclass(frozen=True)
class UserSeed:
    username:str
    email:str
    password:str
    gender:User_gender| None = None
    role:User_Role = User_Role.user
    status:User_status = User_status.active

USER_SEEDS = [
    UserSeed("admin", "admin@example.com", "Admin@123", User_Role.admin),
    UserSeed("moderator", "moderator@example.com", "Moderator@123", User_Role.moderator),
    UserSeed("user01", "user01@example.com", "User@123"),
]


def main():
    with Session(engine) as session:
        for item in USER_SEEDS:
            exists = session.exec(
                select(User).where(User.email == item.email)
            ).first()

            if exists:
                continue

            session.add(
                User(
                    username=item.username,
                    email=item.email,
                    password_hash=password_hash.hash(item.password),
                    role=item.role,
                    status=item.status,
                )
            )

        session.commit()


if __name__ == "__main__":
    main()