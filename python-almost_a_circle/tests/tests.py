#!/usr/bin/python3
"""This will hold a mahority if not all of my UnitTest Cases"""
import unittest
from models.base import Base


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