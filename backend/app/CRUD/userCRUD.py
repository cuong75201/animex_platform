import datetime
from time import timezone

from sqlmodel import Session, select

from app.core.security import get_password_hash
from app.models.user import User
from app.dto.userDTO import UserUpdate

class UserCRUD:
    def __init__(self):
        pass

    @staticmethod
    def findByEmail(*,session:Session,email:str) -> User|None:
        statement = select(User).where(User.email==email)
        session_user=exec(statement).first()
        return session_user
    
    @staticmethod
    def updateUser(*,session:Session,db_user:User,user_in:UserUpdate) -> User:
        user_data=user_in.model_dump(exclude_unset=True)
        extra_data={}
        if "password" in user_data:
            password=user_data['password']
            password_hash=get_password_hash(password)
            extra_data['password_hash']=password_hash
        extra_data['updated_at']=datetime.now(timezone.utc)
        db_user.sqlmodel_update(user_data,extra_data)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

