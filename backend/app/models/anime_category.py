from sqlmodel import Field, SQLModel


class AnimeCategory(SQLModel, table=True):
    __tablename__ = "anime_categories"

    series_id: int = Field(foreign_key="anime_series.id", primary_key=True)
    category_id: int = Field(foreign_key="categories.id", primary_key=True)
