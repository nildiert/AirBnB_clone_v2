#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import *

import json
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


        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(tables)

    def all(self, cls=None):
        """ query in the curent DB session dependng of the  clss name
        """
        data = self.__session.query(State).all()
        keys = []
        my_dict = {}
        for x in data:
            key = (str(type(x).__name__ + '.' + x.id))
            value = x
            my_dict[key] = value
            #setattr(my_dict, key, value)
        '''if cls is not None:
            new_dict = {}
            for key, values in FileStorage.__objects.items():
                if(cls.__name__ in key):
                    new_dict.update({key: values})
            return new_dict
        else:
            return self.__objects'''

        if cls is not None:
            '''data =self.__session.query(cls).all()'''
            print("Recibi class {}".format(cls))
        else:
            print("No recibi cls {}".format(cls))
            #classes = [BaseModel, User, State, City, Amenity, Place, Review]
            #for i in classes:
            '''data = self.__session.query(State).all()'''
            '''return data'''
        #print(my_dict)
        return my_dict

    #all_classes = {"BaseModel", "User", "State", "City","Amenity", "Place", "Review"}

    def new(self, obj):
        if obj is not None:
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
