#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from sqlalchemy import *
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manage the data in the database
    Attributes:
        __engine: Engine
        __session: Session
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Init method
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'),
            os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_HOST'),
            os.environ.get('HBNB_MYSQL_DB'),
            pool_pre_ping=True)
        )
        self.reload()
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query in the curent DB session dependng of the  clss name
        """
        my_dict = {}

        if cls is not None:
            data = self.__session.query(cls).all()
            for x in data:
                key = (type(x).__name__ + '.' + x.id)
                my_dict[key] = x
        else:
            '''classes = [BaseModel, User, State,
            City, Amenity, Place, Review]'''
            classes = [State, City, User, Place, Review, Amenity]
            for clas in classes:
                data = self.__session.query(clas).all()
                if data is not None:
                    for x in data:
                        key = (type(x).__name__ + '.' + x.id)
                        my_dict[key] = x
        return my_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        DBsession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(DBsession)
