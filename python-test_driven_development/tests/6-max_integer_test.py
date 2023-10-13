#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_regular_list(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_negative_values(self):
        result = max_integer([1, -2, 3, -4])
        self.assertEqual(result, 3)

    def test_max_integer_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
