#!/usr/bin/python3
"""
Module that contains the class definition of a City
"""

from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
"""
Represents class that defines each city
"""

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
