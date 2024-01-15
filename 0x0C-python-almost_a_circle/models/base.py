#!/usr/bin/python3

""" introducing the base class blueprint """
import json
import csv
import turtle

class Base:
    """ the Base model
        this is the blueprint used for all instances and child classes
        in this project

    Private Class Attributes:
        __nb_object (int): keeps track of all instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ used to initialize new_0 instance of Base class
        Args:
            id (int): unique id for each instance of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): is a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON serialization to a file.

        Args:
            list_objs (list): inherited Base instances.
        """
        name_file = cls.__name__ + ".json"
        with open(name_file, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_of_dict = [m.to_dictionary() for m in list_objs]
                json_file.write(Base.to_json_string(list_of_dict))

    @staticmethod
    def from_json_string(json_string):
        """for deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation
        Returns:
            an empty list.
            Otherwise - the Python list
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return instantiation from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_0 = cls(1, 1)
            else:
                new_0 = cls(1)
            new_0.update(**dictionary)
            return new_0

    @classmethod
    def load_from_file(cls):
        """Return instantiation from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            empty list.
            Otherwise - list of instantiated classes.
        """
        name_file = str(cls.__name__) + ".json"
        try:
            with open(name_file, "r") as json_file:
                list_of_dict = Base.from_json_string(json_file.read())
                return [cls.create(**item_) for item_ in list_of_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization to a file.

        Args:
            list_objs (list): list of inherited Base instances.
        """
        name_file = cls.__name__ + ".csv"
        with open(name_file, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                w_var = csv.DictWriter(csv_file, field_names=field_names)
                for i in list_objs:
                    w_var.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ for a list of classes instantiated from a CSV file

        Reads from `<cls.__name__>.csv`.

        Returns:
                an empty list.
                list of instantiated classes.
        """
        name_file = cls.__name__ + ".csv"
        try:
            with open(name_file, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_of_dict = csv.DictReader(csv_file, field_names=field_names)
                list_of_dict = [dict([item_0, int(item_1)] for item_0, item_1 in item_.items())
                              for item_ in list_of_dict]
                return [cls.create(**item_) for item_ in list_of_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): objects to draw.
            list_squares (list): objects to draw.
        """
        output_ = turtle.Turtle()
        output_.screen.bgcolor("#b7312c")
        output_.pensize(3)
        output_.shape("turtle")

        output_.color("#ffffff")
        for var_ in list_rectangles:
            output_.showturtle()
            output_.up()
            output_.goto(var_.x, var_.y)
            output_.down()
            for i in range(2):
                output_.forward(var_.width)
                output_.left(90)
                output_.forward(var_.height)
                output_.left(90)
            output_.hideturtle()

        output_.color("#b5e3d8")
        for var_0 in list_squares:
            output_.showturtle()
            output_.up()
            output_.goto(var_0.x, var_0.y)
            output_.down()
            for i in range(2):
                output_.forward(var_0.width)
                output_.left(90)
                output_.forward(var_0.height)
                output_.left(90)
            output_.hideturtle()

        turtle.exitonclick()
