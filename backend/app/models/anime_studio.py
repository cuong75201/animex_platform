from sqlmodel import Field, SQLModel


class AnimeStudio(SQLModel, table=True):
    __tablename__ = "anime_studios"

    anime_release_id: int = Field(foreign_key="anime_releases.id", primary_key=True)
    studio_id: int = Field(foreign_key="studios.id", primary_key=True)
