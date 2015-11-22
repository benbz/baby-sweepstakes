from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Enum,
    )

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

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
    your_name = Column(String(255), nullable=False)
    baby_sex = Column(Enum('Boy', 'Girl'), nullable=False)
    days_late = Column(Integer, nullable=False)
    ounces = Column(Integer, nullable=False)

    @hybrid_property
    def pounds_and_ounces(self):
        pounds = self.ounces / 16
        remaining_ounces = self.ounces % 16
        return '%dlb %doz' % (pounds, remaining_ounces)

    @hybrid_property
    def kilos_and_grams(self):
        all_grams = int(self.ounces * 28.3495)
        return '%d.%dkg' % (all_grams / 1000, all_grams % 1000)


Index('days_late', Guess.days_late, unique=False)
Index('ounces', Guess.ounces, unique=False)
