#!/usr/bin/python3
# 6-max-integer.py
"""Unittests for maximum integer in a list"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """Define unittest for max_integer in a list[]"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [10, 7, 15, 40, 80]
        self.assertEqual(max_integer(unordered), 80)

    def test_max_at_beginning(self):
        """Test max at the beginning of list."""
        beginning = [10, 8, 6, 5, 1]
        self.assertEqual(max_integer(beginning), 10)

    def test_one_element_in_list(self):
        """Test a list with a single element"""
        element = [10]
        self.assertEqual(max_integer(element), 10)

    def test_element_in_string(self):
        """Test for max in a string"""
        Name = ["John"]
        self.assertEqual(max_integer(Name), 'o')

    def test_floats(self):
        """Test for max num in float"""
        Temprature = [37.6, 38.9, 22.4, 26.7, 10.8]
        self.assertEqual(max_integer(Temprature), 38.9)

    def test_int_float(self):
        """Test list containing ints and floats for max"""
        Average_grades = [60, 78, 89.9, 78.98, 97, 69.69]
        self.assertEqual(max_integer(Average_grades), 97)

    def test_list_of_strings(self):
        """Test list of strings for max"""
        classmates = ["John", "Marare", "Kenya"]
        self.assertEqual(max_integer(classmates), "Marare")

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)

    if __name__ == '__main__':
        unittest.main()
