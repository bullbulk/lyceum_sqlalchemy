import sqlalchemy
from sqlalchemy import orm
from sqlalchemy import Column

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(sqlalchemy.Integer,
                primary_key=True, autoincrement=True)
    team_leader = Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = Column(sqlalchemy.String)
    work_size = Column(sqlalchemy.Integer)
    collaborators = Column(sqlalchemy.String)
    start_date = Column(sqlalchemy.DateTime)
    end_date = Column(sqlalchemy.DateTime)
    is_finished = Column(sqlalchemy.BOOLEAN)

    user = orm.relation('User')
