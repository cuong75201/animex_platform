import sqlmodel


class Token(sqlmodel):
    access_token:str
    token_type:str = "bearer"

