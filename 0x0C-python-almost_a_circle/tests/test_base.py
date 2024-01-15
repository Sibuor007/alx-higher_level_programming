#!/usr/bin/python3
""" introducing unittests for base.py.

Unittest classes:
    TestBase_variables
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_variables(unittest.TestCase):
    """ for testing instantiation of the Base class"""

    def test_0_arg(self):
        var_0 = Base()
        var_1 = Base()
        self.assertEqual(var_0.id, var_1.id - 1)

    def test_3_bases(self):
        var_0 = Base()
        var_1 = Base()
        var_2 = Base()
        self.assertEqual(var_0.id, var_2.id - 2)

    def test_for_None_id(self):
        var_0 = Base(None)
        var_1 = Base(None)
        self.assertEqual(var_0.id, var_1.id - 1)

    def test_uniq_id(self):
        self.assertEqual(11, Base(11).id)

    def test_nb_instances_uniq_id(self):
        var_0 = Base()
        var_1 = Base(11)
        var_2 = Base()
        self.assertEqual(var_0.id, var_2.id - 1)

    def test_public_id(self):
        b = Base(11)
        b.id = 16
        self.assertEqual(16, b.id)

    def test_private_instances_num(self):
        with self.assertRaises(AttributeError):
            print(Base(11).__nb_instances)

    def test_id_str(self):
        self.assertEqual("world", Base("world").id)

    def test_id_float(self):
        self.assertEqual(7.4, Base(7.4).id)

    def test_id_complex(self):
        self.assertEqual(complex(9), Base(complex(9)).id)

    def test_id_dict(self):
        self.assertEqual({"a": 4, "b": 9}, Base({"a": 4, "b": 9}).id)

    def test_id_bool(self):
        self.assertEqual(False, Base(False).id)

    def test_id_list(self):
        self.assertEqual([4, 5, 6], Base([4, 5, 6]).id)

    def test_id_tuple(self):
        self.assertEqual((8, 9), Base((8, 9)).id)

    def test_id_set(self):
        self.assertEqual({4, 5, 6}, Base({4, 5, 6}).id)

    def test_id_frozenset(self):
        self.assertEqual(frozenset({4, 5, 6}), Base(frozenset({4, 5, 6})).id)

    def test_id_range(self):
        self.assertEqual(range(9), Base(range(9)).id)

    def test_id_bytes(self):
        self.assertEqual(b'program', Base(b'program').id)

    def test_id_bytearray(self):
        self.assertEqual(bytearray(b'mnopqr'), Base(bytearray(b'mnopqr')).id)

    def test_id_memoryview(self):
        self.assertEqual(memoryview(b'mnopqr'), Base(memoryview(b'mnopqr')).id)

    def test_id_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_id_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_2_args(self):
        with self.assertRaises(TypeError):
            Base(3, 4)


class TestBase_to_json(unittest.TestCase):
    """ for testing to_json_string method of Base class """

    def test_to_json_rect(self):
        rect_ = Rectangle(13, 10, 6, 9, 4)
        self.assertEqual(str, type(Base.to_json_string([rect_.to_dictionary()])))

    def test_to_json_string_dict(self):
        rect_ = Rectangle(13, 10, 6, 9, 4)
        self.assertTrue(len(Base.to_json_string([rect_.to_dictionary()])) == 52)

    def test_to_json_two_dicts(self):
        rect_0 = Rectangle(4, 5, 7, 19, 2)
        rect_1 = Rectangle(5, 3, 6, 2, 12)
        list_dicts_0 = [rect_0.to_dictionary(), rect_1.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts_0)) == 98)

    def test_to_json_square(self):
        sq_ = Square(11, 3, 5, 4)
        self.assertEqual(str, type(Base.to_json_string([sq_.to_dictionary()])))

    def test_to_json_one_dict(self):
        sq_ = Square(11, 3, 5, 4)
        self.assertTrue(len(Base.to_json_string([sq_.to_dictionary()])) == 38)

    def test_to_json_string_square_two_dicts(self):
        sq_0 = Square(11, 3, 5, 4)
        sq_1 = Square(6, 9, 18, 4)
        list_dicts_0 = [sq_0.to_dictionary(), sq_1.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts_0)) == 76)

    def test_to_json_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 4)


class TestBase_save_2_file(unittest.TestCase):
    """ for testing save_to_file method of Base class """

    @classmethod
    def tearDown(self):
        """ bring down created files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_one_rectangle(self):
        rect_ = Rectangle(12, 9, 4, 10, 7)
        Rectangle.save_to_file([rect_])
        with open("Rectangle.json", "rect_") as file_:
            self.assertTrue(len(file_.read()) == 53)

    def test_save_to_file_2_rectangles(self):
        rect_0 = Rectangle(12, 9, 4, 10, 7)
        rect_1 = Rectangle(4, 6, 3, 4, 5)
        Rectangle.save_to_file([rect_0, rect_1])
        with open("Rectangle.json", "rect_") as file_:
            self.assertTrue(len(file_.read()) == 105)

    def test_save_to_file_1_square(self):
        sq_ = Square(11, 8, 3, 9)
        Square.save_to_file([sq_])
        with open("Square.json", "rect_") as file_:
            self.assertTrue(len(file_.read()) == 39)

    def test_save_to_file_2_squares(self):
        sq_0 = Square(11, 8, 3, 9)
        sq_1 = Square(11, 4, 5, 6)
        Square.save_to_file([sq_0, sq_1])
        with open("Square.json", "rect_") as file_:
            self.assertTrue(len(file_.read()) == 77)

    def test_save_to_file_cls_filename(self):
        sq_ = Square(11, 7, 3, 8)
        Base.save_to_file([sq_])
        with open("Base.json", "rect_") as file_:
            self.assertTrue(len(file_.read()) == 39)

    def test_save_overwrite(self):
        sq_ = Square(9, 4, 28, 2)
        Square.save_to_file([sq_])
        sq_ = Square(11, 7, 4, 8)
        Square.save_to_file([sq_])
        with open("Square.json", "rect_") as file_:
            self.assertTrue(len(file_.read()) == 39)

    def test_save_None(self):
        Square.save_to_file(None)
        with open("Square.json", "rect_") as file_:
            self.assertEqual("[]", file_.read())

    def test_save_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "rect_") as file_:
            self.assertEqual("[]", file_.read())

    def test_save_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 4)


class TestBase_from_json(unittest.TestCase):
    """ for testing from_json_string method of Base class """

    def test_from_json_type(self):
        list_input_0 = [{"id": 91, "width": 12, "height": 7}]
        list_input_json = Rectangle.to_json_string(list_input_0)
        list_output_0 = Rectangle.from_json_string(list_input_json)
        self.assertEqual(list, type(list_output_0))

    def test_from_json_string_1_rectangle(self):
        list_input_0 = [{"id": 91, "width": 12, "height": 6, "x": 9}]
        list_input_json = Rectangle.to_json_string(list_input_0)
        list_output_0 = Rectangle.from_json_string(list_input_json)
        self.assertEqual(list_input_0, list_output_0)

    def test_from_json_string_2_rectangles(self):
        list_input_0 = [
            {"id": 91, "width": 12, "height": 6, "x": 9, "y": 8},
            {"id": 89, "width": 6, "height": 3, "x": 5, "y": 1},
        ]
        list_input_json = Rectangle.to_json_string(list_input_0)
        list_output_0 = Rectangle.from_json_string(list_input_json)
        self.assertEqual(list_input_0, list_output_0)

    def test_from_json_string_1_square(self):
        list_input_0 = [{"id": 91, "size": 12, "height": 6}]
        list_input_json = Square.to_json_string(list_input_0)
        list_output_0 = Square.from_json_string(list_input_json)
        self.assertEqual(list_input_0, list_output_0)

    def test_from_json_string_two_squares(self):
        list_input_0 = [
            {"id": 91, "size": 12, "height": 6},
            {"id": 9, "size": 3, "height": 9}
        ]
        list_input_json = Square.to_json_string(list_input_0)
        list_output_0 = Square.from_json_string(list_input_json)
        self.assertEqual(list_input_0, list_output_0)

    def test_from_json_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 4)


class TestBase_create_0(unittest.TestCase):
    """ for testing create method of Base class."""

    def test_create_rectangle_(self):
        rect_0 = Rectangle(5, 7, 3, 4, 9)
        rect_dictionary = rect_0.to_dictionary()
        rect_1 = Rectangle.create(**rect_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect_0))

    def test_create_rectangle_new(self):
        rect_0 = Rectangle(5, 7, 3, 4, 9)
        rect_dictionary = rect_0.to_dictionary()
        rect_1 = Rectangle.create(**rect_dictionary)
        self.assertEqual("[Rectangle]", str(rect_1))

    def test_create_rectangle_0(self):
        rect_0 = Rectangle(5, 7, 3, 4, 9)
        rect_dictionary = rect_0.to_dictionary()
        rect_1 = Rectangle.create(**rect_dictionary)
        self.assertIsNot(rect_0, rect_1)

    def test_create_rectangle_eq(self):
        rect_0 = Rectangle(5, 7, 3, 4, 9)
        rect_dictionary = rect_0.to_dictionary()
        rect_1 = Rectangle.create(**rect_dictionary)
        self.assertNotEqual(rect_0, rect_1)

    def test_create_square_orig(self):
        sq_0 = Square(5, 7, 3, 9)
        s1_dictionary = sq_0.to_dictionary()
        sq_1 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq_0))

    def test_create_square_new(self):
        sq_0 = Square(5, 7, 3, 9)
        s1_dictionary = sq_0.to_dictionary()
        sq_1 = Square.create(**s1_dictionary)
        self.assertEqual("[Square]", str(sq_1))

    def test_create_square_0(self):
        sq_0 = Square(5, 7, 3, 9)
        s1_dictionary = sq_0.to_dictionary()
        sq_1 = Square.create(**s1_dictionary)
        self.assertIsNot(sq_0, sq_1)

    def test_create_square_eq(self):
        sq_0 = Square(5, 7, 3, 9)
        s1_dictionary = sq_0.to_dictionary()
        sq_1 = Square.create(**s1_dictionary)
        self.assertNotEqual(sq_0, sq_1)


class TestBase_load_from_fil_0(unittest.TestCase):
    """ for testing load_from_file_method of Base class """

    @classmethod
    def tearDown(self):
        """ to delete any created files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_1_rectangle(self):
        rect_0 = Rectangle(14, 11, 6, 11, 5)
        rect_1 = Rectangle(6, 8, 9, 10, 6)
        Rectangle.save_to_file([rect_0, rect_1])
        list_rectangles_0 = Rectangle.load_from_file()
        self.assertEqual(str(rect_0), str(list_rectangles_0[0]))

    def test_load_from_file_1_rectangle(self):
        rect_0 = Rectangle(14, 11, 6, 11, 5)
        rect_1 = Rectangle(6, 8, 9, 10, 6)
        Rectangle.save_to_file([rect_0, rect_1])
        list_rectangles_0 = Rectangle.load_from_file()
        self.assertEqual(str(rect_1), str(list_rectangles_0[1]))

    def test_load_from_rectangle_0(self):
        rect_0 = Rectangle(14, 11, 6, 11, 5)
        rect_1 = Rectangle(6, 8, 9, 10, 6)
        Rectangle.save_to_file([rect_0, rect_1])
        output_0 = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output_0))

    def test_load_from_file_first_square(self):
        sq_0 = Square(9, 5, 7, 7)
        sq_1 = Square(13, 9, 6, 7)
        Square.save_to_file([sq_0, sq_1])
        list_squares_0 = Square.load_from_file()
        self.assertEqual(str(sq_0), str(list_squares_0[0]))

    def test_load_from_file_2_square(self):
        sq_0 = Square(9, 5, 7, 7)
        sq_1 = Square(13, 9, 6, 7)
        Square.save_to_file([sq_0, sq_1])
        list_squares_0 = Square.load_from_file()
        self.assertEqual(str(sq_1), str(list_squares_0[1]))

    def test_load_from_square_0(self):
        sq_0 = Square(9, 5, 7, 7)
        sq_1 = Square(13, 9, 6, 7)
        Square.save_to_file([sq_0, sq_1])
        output_0 = Square.load_from_file()
        self.assertTrue(all(type(item) == Square for item in output_0))

    def test_no_file(self):
        output_0 = Square.load_from_file()
        self.assertEqual([], output_0)

    def test_load_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 4)


class TestBase_save_to_file_csv_0(unittest.TestCase):
    """ for testing save_to_file_csv method of Base class """

    @classmethod
    def tearDown(self):
        """ to delete any created files """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_1_rectangle(self):
        rect_ = Rectangle(12, 9, 4, 10, 7)
        Rectangle.save_to_file_csv([rect_])
        with open("Rectangle.csv", "rect_") as file_:
            self.assertTrue("5,10,7,2,8", file_.read())

    def test_save_to_file_csv_2_rectangles(self):
        rect_0 = Rectangle(12, 9, 4, 10, 7)
        rect_1 = Rectangle(4, 6, 3, 4, 5)
        Rectangle.save_to_file_csv([rect_0, rect_1])
        with open("Rectangle.csv", "rect_") as file_:
            self.assertTrue("12,9,4,10,7\n4,6,3,4,5", file_.read())

    def test_save_to_file_csv_1_square(self):
        sq_ = Square(12, 9, 4, 10)
        Square.save_to_file_csv([sq_])
        with open("Square.csv", "rect_") as file_:
            self.assertTrue("8,10,7,2", file_.read())

    def test_save_to_file_csv_two_squares(self):
        sq_0 = Square(12, 9, 4, 10)
        sq_1 = Square(11, 4, 5, 6)
        Square.save_to_file_csv([sq_0, sq_1])
        with open("Square.csv", "rect_") as file_:
            self.assertTrue("8,10,7,2\n3,8,1,2", file_.read())

    def test_save_to_cls_name(self):
        sq_ = Square(12, 9, 4, 10)
        Base.save_to_file_csv([sq_])
        with open("Base.csv", "rect_") as file_:
            self.assertTrue("12,9,4,10", file_.read())

    def test_save_csv_overwrite(self):
        sq_ = Square(11, 4, 28, 4)
        Square.save_to_file_csv([sq_])
        sq_ = Square(12, 9, 4, 10)
        Square.save_to_file_csv([sq_])
        with open("Square.csv", "rect_") as file_:
            self.assertTrue("11,4,28,4", file_.read())

    def test_save_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "rect_") as file_:
            self.assertEqual("[]", file_.read())

    def test_save_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "rect_") as file_:
            self.assertEqual("[]", file_.read())

    def test_save_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_csv_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 4)


class TestBase_load_from_file_csv(unittest.TestCase):
    """ for testing load_from_file_csv method of Base class """

    @classmethod
    def tearDown(self):
        """ to delete any created files """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_csv_first_rectangle(self):
        rect_0 = Rectangle(14, 11, 6, 11, 5)
        rect_1 = Rectangle(6, 8, 9, 10, 6)
        Rectangle.save_to_file_csv([rect_0, rect_1])
        list_rectangles_0 = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect_0), str(list_rectangles_0[0]))

    def test_load_csv_2_rectangle(self):
        rect_0 = Rectangle(14, 11, 6, 11, 5)
        rect_1 = Rectangle(6, 8, 9, 10, 6)
        Rectangle.save_to_file_csv([rect_0, rect_1])
        list_rectangles_0 = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect_1), str(list_rectangles_0[1]))

    def test_load_csv_rectangle_types(self):
        rect_0 = Rectangle(14, 11, 6, 11, 5)
        rect_1 = Rectangle(6, 8, 9, 10, 6)
        Rectangle.save_to_file_csv([rect_0, rect_1])
        output_0 = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(item) == Rectangle for item in output_0))

    def test_load_csv_first_square(self):
        sq_0 = Square(9, 5, 7, 7)
        sq_1 = Square(13, 9, 6, 7)
        Square.save_to_file_csv([sq_0, sq_1])
        list_squares_0 = Square.load_from_file_csv()
        self.assertEqual(str(sq_0), str(list_squares_0[0]))

    def test_load_csv_second_square(self):
        sq_0 = Square(9, 5, 7, 7)
        sq_1 = Square(13, 9, 6, 7)
        Square.save_to_file_csv([sq_0, sq_1])
        list_squares_0 = Square.load_from_file_csv()
        self.assertEqual(str(sq_1), str(list_squares_0[1]))

    def test_load_csv_square_types(self):
        sq_0 = Square(9, 5, 7, 7)
        sq_1 = Square(13, 9, 6, 7)
        Square.save_to_file_csv([sq_0, sq_1])
        output_0 = Square.load_from_file_csv()
        self.assertTrue(all(type(item) == Square for item in output_0))

    def test_load_csv_no_file(self):
        output_0 = Square.load_from_file_csv()
        self.assertEqual([], output_0)

    def test_load_csv_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 4)


if __name__ == "__main__":
    unittest.main()
