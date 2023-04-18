#!/usr/bin/python3
""" Base Class"""
import json


class Base:
    """ Base Classs"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class constructor
        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list of objects"""
        filename = cls.__name__+".json"
        with open(filename, 'w') as jfile:
            if list_objs is None:
                jfile.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns string from JSON string"""
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns class instantiated from a dictionary """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new 

    @classmethod
    def load_from_file(cls):
        """Returns lis of classes instantiated from a JSON file"""
        filename = str(cls.__name__)+".json"
        try:
            with open(filename, 'r') as jfile:
                list_dicts = Base.from_json_string(jfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        pass

    @classmethod
    def laod_from_file_csv(cls):
        pass

    @classmethod
    def draw(list_rectangles, list_squares):
        pass
