import unittest

max_integer = __import__('6-max_integer').max_integer
class TestStringMethods(unittest.TestCase):
    """class testing"""

    def test_max_integer(self):
        """Postive Test"""
        test = [5, 6, 7, 18, 19]
        self.assertEqual(max_integer(test), 99)


    def max_integer(list=[]):
        """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
        """
        if len(list) == 0:
            return None
        result = list[0]
        i = 1
        while i < len(list):
            if list[i] > result:
                result = list[i]
            i += 1
        return result
