#!/usr/bin/python3
# test_rectangle.py
"""introduces unittests for rectangle.py

Unittest classes:
    TestRectangle_instantiation_    
    TestRectangle_width_0
    TestRectangle_height_0
    TestRectangle_x_0
    TestRectangle_y_0
    TestRectangle_order_of_initi_
    TestRectangle_area_0
    TestRectangle_updt_args
    TestRectangle_updt_kwargs
    TestRectangle_to_dictionary_0
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation_0(unittest.TestCase):
    """ for testing instantiation of the Rectangle class """

    def test_rect_is_base(self):
        self.assertIsInstance(Rectangle(8, 4), Base)

    def test_no_args_0(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_1_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_2_args(self):
        rect_0 = Rectangle(12, 6)
        rect_1 = Rectangle(6, 12)
        self.assertEqual(rect_0.id, rect_1.id - 1)

    def test_3_args(self):
        rect_0 = Rectangle(6, 6, 8)
        rect_1 = Rectangle(8, 8, 6)
        self.assertEqual(rect_0.id, rect_1.id - 1)

    def test_4_args(self):
        rect_0 = Rectangle(4, 6, 7, 8)
        rect_1 = Rectangle(8, 7, 6, 4)
        self.assertEqual(rect_0.id, rect_1.id - 1)

    def test_5_args(self):
        self.assertEqual(3, Rectangle(4, 2, 0, 0, 3).id)

    def test_more_5_args(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 6, 7, 8, 9, 10)

    def test_width_private_0(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 3).__width)

    def test_height_0_private_0(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 3).__height)

    def test_x_private_0(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 3).__x)

    def test_y_private_0(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 3).__y)

    def test_width_getter_0(self):
        rect_ = Rectangle(3, 5, 5, 3, 7)
        self.assertEqual(7, rect_.width)

    def test_width_setter_0(self):
        rect_ = Rectangle(3, 5, 5, 3, 7)
        rect_.width = 9
        self.assertEqual(9, rect_.width)

    def test_height_getter_0(self):
        rect_ = Rectangle(3, 5, 5, 3, 7)
        self.assertEqual(3, rect_.height)

    def test_height_setter_0(self):
        rect_ = Rectangle(3, 5, 5, 3, 7)
        rect_.height = 9
        self.assertEqual(9, rect_.height)

    def test_x_getter_0(self):
        rect_ = Rectangle(3, 5, 5, 3, 7)
        self.assertEqual(3, rect_.x)

    def test_x_setter_0(self):
        rect_ = Rectangle(3, 5, 5, 3, 7)
        rect_.x = 9
        self.assertEqual(9, rect_.x)

    def test_y_getter_0(self):
        rect_ = Rectangle(3, 5, 5, 3, 7)
        self.assertEqual(7, rect_.y)

    def test_y_setter_0(self):
        rect_ = Rectangle(3, 5, 5, 3, 7)
        rect_.y = 9
        self.assertEqual(9, rect_.y)


class TestRectangle_width_0(unittest.TestCase):
    """ for testing initialization of Rectangle width attribute """

    def test_None_width_0(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 6)

    def test_str_width_0(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 6)

    def test_float_width_0(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(7.6, 6)

    def test_complex_width_0(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1 + 2j, 6)

    def test_list_width_0(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 6)

    def test_tuple_width_0(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 6)

    def test_dict_width_0(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 6)

    def test_bool_width_0(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 6)

    def test_width_neg_0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 6)

    def test_width_0_0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 6)


class TestRectangle_height_0(unittest.TestCase):
    """ for testing initialization of Rectangle height attribute """

    def test_None_height_0(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, None)

    def test_str_height_0(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, "invalid")

    def test_float_height_0(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, 7.6)

    def test_complex_height_0(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, 1 + 2j)

    def test_list_height_0(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, [1, 2, 3])

    def test_tuple_height_0(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, (1, 2, 3))

    def test_dict_height_0(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, {"a": 1, "b": 2})

    def test_bool_height_0(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, True)

    def test_height_neg_0(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(6, -1)

    def test_height_0_0(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(6, 0)


class TestRectangle_x_0(unittest.TestCase):
    """ for testing initialization of Rectangle x attribute """

    def test_None_x_0(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, None, 8)

    def test_str_x_0(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, "invalid", 8)

    def test_float_x_0(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, 7.6, 8)

    def test_complex_x_0(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, 1 + 2j, 8)

    def test_list_x_0(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, [1, 2, 3], 8)

    def test_tuple_x_0(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, (1, 2, 3), 8)

    def test_dict_x_0(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, {"a": 1, "b": 2}, 8)

    def test_bool_x_0(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 7, True, 8)


class TestRectangle_y_0(unittest.TestCase):
    """ for testing initialization of Rectangle y attribute """

    def test_None_y_0(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, None)

    def test_str_y_0(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, "invalid")

    def test_float_y_0(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, 7.6)

    def test_complex_y_0(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, 1 + 2j)

    def test_list_y_0(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, [1, 2, 3])

    def test_tuple_y_0(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, (1, 2, 3))

    def test_dict_y_0(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, {"a": 1, "b": 2})

    def test_bool_y_0(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 7, 8, True)


class TestRectangle_order_of_initi_0(unittest.TestCase):
    """ for testing order of instantiation """

    def test_width_height_0(self):
        rect_ = Rectangle(8, 4)
        self.assertEqual(8, rect_.width)
        self.assertEqual(4, rect_.height)

    def test_width_height_x_0(self):
        rect_ = Rectangle(8, 4, 6)
        self.assertEqual(8, rect_.width)
        self.assertEqual(4, rect_.height)
        self.assertEqual(6, rect_.x)

    def test_width_height_x_y_0(self):
        rect_ = Rectangle(8, 4, 6, 2)
        self.assertEqual(8, rect_.width)
        self.assertEqual(4, rect_.height)
        self.assertEqual(6, rect_.x)
        self.assertEqual(2, rect_.y)

class TestRectangle_area_0(unittest.TestCase):
    """ for testing the area method of the Rectangle class """

    def test_area_small_0(self):
        rect_ = Rectangle(6, 4, 0, 0, 0)
        self.assertEqual(24, rect_.area())

    def test_area_large_0(self):
        rect_ = Rectangle(799, 999, 0, 0, 1)
        self.assertEqual(798201, rect_.area())

    def test_area_changed_attributes_0(self):
        rect_ = Rectangle(7, 14, 1, 1, 1)
        rect_.width = 15
        rect_.height = 1
        self.assertEqual(105, rect_.area())

    def test_area_one_arg_0(self):
        rect_ = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect_.area(1)


class TestRectangle_stdout_0(unittest.TestCase):
    """ for testing __str__ and display methods of Rectangle class """

    @staticmethod
    def capture_stdout_0(rect_q, method):
        """ returns text printed to stdout

        Args:
            rect_q (Rectangle):  print to stdout.
            method (str): to run on rect_q.
        Returns:
            printed to stdout by calling method on sq.
        """
        capture_0 = io.StringIO()
        sys.stdout = capture_0
        if method == "print":
            print(rect_q)
        else:
            rect_q.display()
        sys.stdout = sys.__stdout__
        return capture_0

    # testing for  __str__ method
    def test_str_print_width_height_0(self):
        rect_ = Rectangle(6, 8)
        capture_0 = TestRectangle_stdout_0.capture_stdout_0(rect_, "print")
        correct_0 = "[Rectangle] ({}) 0/0 - 6/8\n".format(rect_.id)
        self.assertEqual(correct_0, capture_0.getvalue())

    def test_str_width_height_0_x(self):
        rect_ = Rectangle(7, 7, 1)
        correct_0 = "[Rectangle] ({}) 1/0 - 7/7".format(rect_.id)
        self.assertEqual(correct_0, rect_.__str__())

    def test_str_width_height_0_x_y(self):
        rect_ = Rectangle(1, 8, 2, 4)
        correct_0 = "[Rectangle] ({}) 2/4 - 1/8".format(rect_.id)
        self.assertEqual(correct_0, str(rect_))

    def test_str_width_height_0_x_y_id(self):
        rect_ = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rect_))

    def test_str_changed_attributes_0(self):
        rect_ = Rectangle(9, 7, 0, 0, [4])
        rect_.width = 15
        rect_.height = 1
        rect_.x = 8
        rect_.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rect_))

    def test_str_one_arg_0(self):
        rect_ = Rectangle(1, 2, 4, 4, 5)
        with self.assertRaises(TypeError):
            rect_.__str__(1)

    # testing for display method
    def test_display_width_height_0(self):
        rect_ = Rectangle(2, 4, 0, 0, 0)
        capture_0 = TestRectangle_stdout_0.capture_stdout(rect_, "display")
        self.assertEqual("##\n##\n##\n", capture_0.getvalue())

    def test_display_width_height_0_x(self):
        rect_ = Rectangle(5, 2, 1, 0, 1)
        capture_0 = TestRectangle_stdout_0.capture_stdout(rect_, "display")
        self.assertEqual(" ###\n ###\n", capture_0.getvalue())

    def test_display_width_height_0_y(self):
        rect_ = Rectangle(4, 5, 0, 2, 0)
        capture_0 = TestRectangle_stdout_0.capture_stdout(rect_, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture_0.getvalue())

    def test_display_width_height_0_x_y(self):
        rect_ = Rectangle(2, 4, 6, 2, 0)
        capture_0 = TestRectangle_stdout_0.capture_stdout(rect_, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture_0.getvalue())

    def test_display_1_arg(self):
        rect_ = Rectangle(5, 1, 2, 6, 7)
        with self.assertRaises(TypeError):
            rect_.display(1)


class TestRectangle_updt_args(unittest.TestCase):
    """ for testing update args method of the Rectangle class """

    # Test args
    def test_updt_args_0(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update()
        self.assertEqual("[Rectangle] (12) 12/12 - 12/12", str(rect_))

    def test_updt_args_one(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(98)
        self.assertEqual("[Rectangle] (98) 12/12 - 12/12", str(rect_))

    def test_updt_args_two(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(98, 2)
        self.assertEqual("[Rectangle] (98) 12/12 - 2/112", str(rect_))

    def test_updt_args_three(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(98, 2, 3)
        self.assertEqual("[Rectangle] (98) 12/12 - 2/3", str(rect_))

    def test_updt_args_four(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(98, 2, 3, 4)
        self.assertEqual("[Rectangle] (98) 4/12 - 2/3", str(rect_))

    def test_updt_args_five(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(98, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (98) 4/5 - 2/3", str(rect_))

    def test_updt_args_more_than_five(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(98, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (98) 4/5 - 2/3", str(rect_))

    def test_updt_args_None_id(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(None)
        correct_0 = "[Rectangle] ({}) 12/12 - 12/12".format(rect_.id)
        self.assertEqual(correct_0, str(rect_))

    def test_updt_args_None_id_and_more(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(None, 4, 5, 2)
        correct_0 = "[Rectangle] ({}) 2/12 - 4/5".format(rect_.id)
        self.assertEqual(correct_0, str(rect_))

    def test_updt_args_twice(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        rect_.update(98, 2, 3, 4, 5, 6)
        rect_.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rect_))

    def test_updt_args_invalid_width_type(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_.update(98, "invalid")

    def test_updt_args_width_zero(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_.update(98, 0)

    def test_updt_args_width_negative(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_.update(98, -5)

    def test_updt_args_invalid_height_0_type(self):
        rect_ = Rectangle(12, 12, 12, 12, 12)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_.update(98, 2, "invalid")

    def test_updt_args_height_0_zero(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(ValueError, "height must be > 0"):
        rect_.update(98, 1, 0)

def test_updt_args_height_0_negative(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(ValueError, "height must be > 0"):
        rect_.update(98, 1, -5)

def test_updt_args_invalid_x_type(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        rect_.update(98, 2, 3, "invalid")

def test_updt_args_x_negative(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(ValueError, "x must be >= 0"):
        rect_.update(98, 1, 2, -6)

def test_updt_args_invalid_y(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(TypeError, "y must be an integer"):
        rect_.update(98, 2, 3, 4, "invalid")

def test_updt_args_y_negative(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(ValueError, "y must be >= 0"):
        rect_.update(98, 1, 2, 3, -6)

def test_updt_args_width_before_height_0(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        rect_.update(98, "invalid", "invalid")

def test_updt_args_width_before_x(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        rect_.update(98, "invalid", 1, "invalid")

def test_updt_args_width_before_y(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(TypeError, "width must be an integer"):
        rect_.update(98, "invalid", 1, 2, "invalid")

def test_updt_args_height_0_before_x(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        rect_.update(98, 1, "invalid", "invalid")

def test_updt_args_height_0_before_y(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(TypeError, "height must be an integer"):
        rect_.update(98, 1, "invalid", 1, "invalid")

def test_updt_args_x_before_y(self):
    rect_ = Rectangle(8, 8, 8, 8, 8)
    with self.assertRaisesRegex(TypeError, "x must be an integer"):
        rect_.update(98, 1, 2, "invalid", "invalid")

class TestRectangle_updt_kwargs(unittest.TestCase):
    """ for testing update kwargs method of the Rectangle class """

    def test_updt_kwargs_one(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(id=1)
        self.assertEqual("[Rectangle] (1) 0/0 - 10/10", str(rect_))

    def test_updt_kwargs_two(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 0/0 - 2/10", str(rect_))

    def test_updt_kwargs_three(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 0/0 - 2/3", str(rect_))

    def test_updt_kwargs_four(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(rect_))

    def test_updt_kwargs_five(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rect_))

    def test_updt_kwargs_None_id(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(id=None)
        correct_0 = "[Rectangle] ({}) 0/0 - 10/10".format(rect_.id)
        self.assertEqual(correct_0, str(rect_))

    def test_updt_kwargs_None_id_and_more(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(id=None, height=7, y=9)
        correct_0 = "[Rectangle] ({}) 0/9 - 10/7".format(rect_.id)
        self.assertEqual(correct_0, str(rect_))

    def test_updt_kwargs_twice(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(id=89, x=1, height=2)
        rect_.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(rect_))

    def test_updt_kwargs_invalid_width_type(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_.update(width="invalid")

    def test_updt_kwargs_width_zero(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_.update(width=0)

    def test_updt_kwargs_width_negative(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_.update(width=-5)

    def test_updt_kwargs_invalid_height_0_type(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_.update(height="invalid")

    def test_updt_kwargs_height_0_zero(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect_.update(height=0)

    def test_updt_kwargs_height_0_negative(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect_.update(height=-5)

    def test_updt_kwargs_inavlid_x_type(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect_.update(x="invalid")

    def test_updt_kwargs_x_negative(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect_.update(x=-5)

    def test_updt_kwargs_invalid_y_type(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect_.update(y="invalid")

    def test_updt_kwargs_y_negative(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect_.update(y=-5)

    def test_updt_args_and_kwargs(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(98, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (98) 0/0 - 2/12", str(rect_))

    def test_updt_kwargs_wrong_keys(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 0/0 - 10/10", str(rect_))

    def test_updt_kwargs_some_wrong_keys(self):
        rect_ = Rectangle(10, 10, 10, 10, 10)
        rect_.update(height=5, id=98, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (98) 19/7 - 10/5", str(rect_))


class TestRectangle_to_dictionary_0(unittest.TestCase):
    """ for testing to_dictionary method of the Rectangle class """

    def test_to_dictionary_output_0(self):
        rect_ = Rectangle(10, 10, 0, 0, 10)
        correct_0 = {'x': 0, 'y': 0, 'id': 10, 'height': 10, 'width': 10}
        self.assertDictEqual(correct_0, rect_.to_dictionary())

    def test_to_dictionary_no_object_changes_0(self):
        rect_0 = Rectangle(10, 10, 0, 0, 10)
        rect_1 = Rectangle(10, 10, 0, 0, 10)
        rect_1.update(**rect_0.to_dictionary())
        self.assertNotEqual(rect_0, rect_1)

    def test_to_dictionary_arg_0(self):
        rect_ = Rectangle(10, 10, 0, 0, 2)
        with self.assertRaises(TypeError):
            rect_.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
