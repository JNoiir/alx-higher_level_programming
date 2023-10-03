#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 4, 2, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [4]
        self.assertEqual(max_integer(one_element), 4)

    def test_floats(self):
        """Test a list of floats."""
        floats = [4.53, 3.63, -7.183, 13.1, 9.0]
        self.assertEqual(max_integer(floats), 13.1)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [4.56, 14.5, -2, 14, 7]
        self.assertEqual(max_integer(ints_and_floats), 14.5)

    def test_string(self):
        """Test a string."""
        string = "max"
        self.assertEqual(max_integer(string), 'x')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["max", "is", "my", "namee"]
        self.assertEqual(max_integer(strings), "namee")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
