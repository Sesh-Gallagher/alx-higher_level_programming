#!/usr/bin/python3
"""
Module contains State class and Base, an instance of declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
Represents class with id and name attributes of each state
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
