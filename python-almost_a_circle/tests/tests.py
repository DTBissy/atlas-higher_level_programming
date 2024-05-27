#!/usr/bin/python3
"""This will hold a mahority if not all of my UnitTest Cases"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_default_id_assignment(self):
        """Test the instances without an id already assigned and should
        return a 1"""
        b1 = Base()
        b2 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_stated_id_assignment(self):
        """This tests that the instance assignes to what id= is assigned to"""
        b1 = Base(id=42)
        b2 = Base(id=5)

        self.assertEqual(b1.id, 42)
        self.assertEqual(b2.id, 5)

    def test_Base_to_json_string(self):
        """Test that to_json returns 'null' when passed None"""
        result = Base.to_json_string(None)
        self.assertEqual(result, 'null')

    def test_Base_to_json_string_empty_list_exists(self):
        """This returns a empty list exists"""
        result = Base.to_json_string([])
        self.assertEqual(result, '[]')

    def test_Base_from_json(self):
        """This checks a loaded json string when None passed"""
        result = Base.from_json_string(None)
        self.assertIsNone(result)

    def test_from_Base_from_json_string_valid(self):
        """This tests if a instance is created from a valid json"""
        json_str = '{"id": 1}'
        result = Base.from_json_string(json_str)
        self.assertEqual(result, {"id": 1})

class Test_Rectangle(unittest.TestCase):
    def test_Rectangle_args_to_height_passed(self):
        """I pass in two args, width,height"""
        r1 = Rectangle(1, 2)

        self.assertEqual(r1.width, (1))
        self.assertEqual(r1.height, (2))

    def test_Rectangle_args_to_x_passed(self):
        """I pass in three args, width, height, x"""
        r1 = Rectangle(1, 2, 3)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3 )

    def test_Rectangle_args_to_y_passed(self):
        """I pass 4 args, width, height, x, y"""
        r1 = Rectangle(1, 2, 3, 4)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_Rectangle_string_width_passed(self):
        """I pass a string for width"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)

            self.assertEqual(r1.height, 2)

    def test_Rectangle_string_height_passed(self):
        """I pass a string for height"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "2")

            self.assertEqual(r1.width, 1)

    def test_Rectangle_string_x_passed(self):
        """I pass a string for x"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "3")

            self.assertEqual(r1.width, 1)
            self.assertEqual(r1.height, 2)

    def test_Rectangle_string_y_passed(self):
        """I pass a string for y"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")

            self.assertEqual(r1.width, 1)
            self.assertEqual(r1.x, 3)
            self.assertEqual(r1.height, 2)

    def test_Rectangle_args_to_id_passed(self):
        """I pass 5 args, width, height, x, y, id"""
        r1 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_Rectangle_negative_width_passed(self):
        """I pass a negative int for width"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

            self.assertEqual(r1.height, 2)

    def test_Rectangle_negative_height_passed(self):
        """I pass a negative int for height"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

            self.assertEqual(r1.width, 1)

    def test_Rectangle_for_zero_width_passed(self):
        """I pass a negative int for width"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

            self.assertEqual(r1.height, 2)

    def test_Rectangle_for_zero_height_passed(self):
        """I pass a negative int for height"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

            self.assertEqual(r1.width, 1)

    def test_Rectangle_negative_x_passed(self):
        """I pass a a negative int for x"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -3)

            self.assertEqual(r1.width, 1)
            self.assertEqual(r1.height, 2)

    def test_Rectangle_negative_y_passed(self):
        """I pass a negative int for y"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, -4)

            self.assertEqual(r1.width, 1)
            self.assertEqual(r1.x, 3)
            self.assertEqual(r1.height, 2)

    def test_area_exists(self):
        """This tests if area exists"""
        r1 = Rectangle(3, 2)
        area = r1.area()

        self.assertIsNotNone(area)
        self.assertEqual(area, 6)

    def test_str_method(self):
        """This tests the string method"""
        r1 = Rectangle(3, 2)
        str = r1.__str__()

        self.assertIsNotNone(str)
        self.assertEqual(str, "[Rectangle] (10) 0/0 - 3/2")

    def test_display_without_x_y(self):
        """This test display without x and y"""

        r1 = Rectangle(3, 2, 0, 0)
        with self.assertRaises(AssertionError):
            display = r1.display()

            self.assertIsNotNone(display)


    def test_display_without_y(self):
        """This test display without x and y"""

        r1 = Rectangle(3, 2, 1)
        r1.display()


    def test_display(self):
        """This test display without x and y"""

        r1 = Rectangle(3, 2, 1, 4)
        r1.display()

    def to_dictionary(self):
        """This tests the to_dictionary method exists"""
        r1 = Rectangle(1, 3, 4, 5)
        r1.to_dictionary()

        self.assertIsNotNone(r1.to_dictionary)
