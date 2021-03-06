import datetime
import sqlalchemy
from sqlalchemy import Column

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(sqlalchemy.Integer,
                primary_key=True, autoincrement=True)
    surname = Column(sqlalchemy.String)
    name = Column(sqlalchemy.String)
    age = Column(sqlalchemy.Integer)
    position = Column(sqlalchemy.String)
    speciality = Column(sqlalchemy.String)
    address = Column(sqlalchemy.String)
    email = Column(sqlalchemy.String,
                   index=True, unique=True)
    hashed_password = Column(sqlalchemy.String)
    modified_data = Column(sqlalchemy.DateTime,
                           default=datetime.datetime.now)
