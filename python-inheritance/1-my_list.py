#!/usr/bin/python3
"""Makes Sum Shake"""


class MyList(list):
    def print_sorted(self):
        """Sort() prints a lists in ascending order"""
        self.sort()
        print(self)
