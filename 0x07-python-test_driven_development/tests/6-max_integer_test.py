#!/usr/bin/python3
"""Tests for find_largest_value([..])."""

import unittest
find_largest_value = __import__('6-max_integer').max_integer

class TestFindLargestValue(unittest.TestCase):
    """Define tests for find_largest_value([..])."""

    def test_sorted_numbers(self):
        """Test a sorted sequence of numbers."""
        sorted_numbers = [8, 15, 22, 30]
        self.assertEqual(find_largest_value(sorted_numbers), 30)

    def test_unsorted_numbers(self):
        """Test an unsorted sequence of numbers."""
        unsorted_numbers = [8, 30, 22, 15]
        self.assertEqual(find_largest_value(unsorted_numbers), 30)

    def test_max_at_start(self):
        """Test a sequence with the maximum value at the beginning."""
        max_at_start = [30, 22, 15, 8]
        self.assertEqual(find_largest_value(max_at_start), 30)

    def test_empty_sequence(self):
        """Test an empty sequence."""
        empty_sequence = []
        self.assertEqual(find_largest_value(empty_sequence), None)

    def test_single_element_sequence(self):
        """Test a sequence with a single element."""
        single_element_sequence = [99]
        self.assertEqual(find_largest_value(single_element_sequence), 99)

    def test_float_values(self):
        """Test a sequence of floating-point numbers."""
        float_values = [3.14, 9.81, -5.55, 12.34, 7.0]
        self.assertEqual(find_largest_value(float_values), 12.34)

    def test_ints_and_floats_mixed(self):
        """Test a sequence of integers and floats."""
        ints_and_floats_mixed = [3.14, 12.5, -7, 12, 5]
        self.assertEqual(find_largest_value(ints_and_floats_mixed), 12.5)

    def test_character_string(self):
        """Test a character string."""
        character_string = "Python"
        self.assertEqual(find_largest_value(character_string), 'y')

    def test_sequence_of_strings(self):
        """Test a sequence of strings."""
        string_sequence = ["Python", "is", "awesome", "language"]
        self.assertEqual(find_largest_value(string_sequence), "awesome")

    def test_empty_character_string(self):
        """Test an empty character string."""
        self.assertEqual(find_largest_value(""), None)

if __name__ == '__main__':
    unittest.main()

