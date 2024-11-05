#!/usr/bin/python3
"""movie module for moviequotes"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import relationship

class Movie(BaseModel, Base):
    """handle Movie attributes"""
    __tablename__ = 'movies'
    if storage_type == 'db':
        movie = Column(String(128), nullable=False, primary_key=True)
        script = Column(String(2048), nullable=False)
        stars = Column(String(128), nullable=False)
        year = Column(String(60), nullable=False)
        review = relationship('Review',
                              backref='movie',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''
        script = ''
        stars = ''
        years = 0

        @property
        def reviews(self):
            """returns review for movie"""
            from models import storage
            related_review = []
            reviews = storage.all(Review)
            for review in reviews.values():
                if review.movie == self.id:
                    related_review.append(review)
            return related_review
