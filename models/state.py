#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.base_model import BaseModel, Base
import models

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City')
    else:
        @property
        def cities(self):
            data = models.storage.all()
            print(data)
