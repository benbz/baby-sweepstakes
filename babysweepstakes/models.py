from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Enum,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Guess(Base):
    __tablename__ = 'guess'
    id = Column(Integer, primary_key=True)
    your_name = Column(String)
    baby_sex = Column(Enum('Boy', 'Girl'))
    days_late = Column(Integer)

Index('days_late', Guess.days_late, unique=True, mysql_length=255)
