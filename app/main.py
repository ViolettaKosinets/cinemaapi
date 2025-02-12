import os
from dotenv import load_dotenv
from datetime import date, time

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


load_dotenv()
engine = create_engine(os.getenv('DB_URL_POSTGRES'))


class Base(DeclarativeBase):
    pass


# film_genres = Table('film_genres', Base.metadata, )


class FilmModel(Base):
    __tablename__ = 'films'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    release_date: Mapped[date] = mapped_column(nullable=False)
    # genre: Mapped[list['GenreModel']] = relationship('GenreModel',
    #                                                 secondary=film_genres,
    #                                                 back_populates='films')
    duration: Mapped[time] = mapped_column(nullable=False)
    # actor
    description: Mapped[str]


class GenreModel(Base):
    __tablename__ = 'genres'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
