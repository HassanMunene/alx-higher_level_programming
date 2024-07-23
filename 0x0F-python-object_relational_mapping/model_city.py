#!/usr/bin/python3
"""
Define City class
"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class City(Base):
    """
    class with id and name attributes of each and every city
    and state_id which it belongs to
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

# Hassan Munene
