from sqlalchemy import Index
from sqlmodel import Field, SQLModel

from app.models.enums import Category_type


class Categories(SQLModel, table=True):
    __tablename__ = "categories"
    __table_args__ = (
        Index("ix_categories_slug", "slug"),
        Index("ix_categories_type", "type"),
    )

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False, max_length=100)
    slug: str = Field(unique=True, nullable=False, max_length=100)
    type: Category_type = Field(nullable=False)
