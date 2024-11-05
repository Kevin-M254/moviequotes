#!/usr/bin/python3
"""review module"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """class for managing review objects"""
    __tablename__ = 'reviews'
    if storage_type == 'db':
        movie = Column(String(128), ForeignKey('movies.movie'), nullable=False)
        review = Column(String(1024), nullable=False)
    else:
        movie = ''
        review = ''
