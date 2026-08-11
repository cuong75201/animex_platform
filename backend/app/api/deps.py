
from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import create_engine
from app.core.config import Settings, setting

engine = create_engine(str(Settings.SQLALCHEMY_DATABASE_URL))
def get_db() -> Generator[Session]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session,Depends(get_db)]