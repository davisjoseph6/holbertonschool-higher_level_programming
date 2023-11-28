#!/usr/bin/python3
"""class states
"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import Sequence
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """states class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
