from re import S

from click import UsageError
from sqlmodel import Session

from app.CRUD.userCRUD import UserCRUD
from app.core.security import verify_password
from app.dto.userDTO import UserUpdate
from app.models.user import User


class UserService:
    def __init__(self):
        self.userCRUD:UserCRUD = UserCRUD()
        self.DUMMY_HASH = "$argon2id$v=19$m=65536,t=3,p=4$MjQyZWE1MzBjYjJlZTI0Yw$YTU4NGM5ZTZmYjE2NzZlZjY0ZWY3ZGRkY2U2OWFjNjk"
    
    def authenticate(self,*,session:Session,email:str,password:str) -> User|None:
        userSession= self.userCRUD.findByEmail(session=session,email=email)
        if not userSession:
            verify_password(password,self.DUMMY_HASH)
            return None
        verified,update_password=verify_password(password,userSession.password_hash)
        if not verified:
            return None
        if update_password:
            userUpdate = self.userCRUD.updateUser(Session=session,db_user=userSession,user_in=UserUpdate(password=update_password))
            return userUpdate
        return userSession