#!/usr/bin/python3
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Integer
from sqlalchemy.orm import Relationship

class Quote(BaseModel, Base):
    """representation of quotes"""
    if models.storage_t == 'db':
        __tablename__ = 'quotes'
        movie = Column(String(60), ForeignKey('movies.name'), nullable=False)
        review = Column(String(1024), ForeignKey('movies.review'), nullable=False)
        quote = Column(String(1024), nullable=False)
        year = Column(Integer, nullable=False, default=0)
    else:
        movie = ""
        review = ""
        quote = ""
        year = 0
