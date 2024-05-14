#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """Postive Test"""
        test = [99, 6, 7, 18, 19]
        self.assertEqual(max_integer(test), 99)

    def test_max_middle(self):
        """Tests for the max in the middle"""
        test = [21, 54, 99, 67, 11]
        self.assertEqual(max_integer(test), 99)

    def test_max_end(self):
        """Tests max at the end"""
        test = [9, 9, 87, 1, 3, 99]
        self.assertEqual(max_integer(test), 99)

    def test_single_element(self):
        """Tests for a single element"""
        test = [99]
        self.assertEqual(max_integer(test), 99)

    def test_negative_elements(self):
        """tests negative elements"""
        test = [-5. -6, -7, -18, -19]
        self.assertEqual(max_integer(test), -5)

    def empty_list(self):
        """Tests for empty Lists"""
        test = []
        self.assertEqual(max_integer(test), None)

    def mixed_numbers(self):
        """Tests for negative and postive elements"""
        test = [1, 2, -3, -4, 50, -60]
        self.assertEqual(max_integer(test), 99)
