#!/usr/bin/python3
"""
unitest for max integer in a list
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """ checks codes """
    def test_max_list(self):
        """ common use """
        self.assertEqual(max_int([1, 4, 2, 3]), 4)
        """ only negative numbers """
        self.assertEqual(max_int([-4, -1, -2, -3]), -1)
        """ max first element of list """
        self.assertEqual(max_int([4, 3, 2, 3]), 4)
        """ max last element of list """
        self.assertEqual(max_int([1, 4, 2, 10]), 10)
        """ max middle element of list """
        self.assertEqual(max_int([1, 4, 5, 3, 2]), 5)
        """ list contains 1 element """
        self.assertEqual(max_int([10]), 10)

    def test_empty_list(self):
        """ empty list """
        self.assertEqual(max_int([]), None)

    def test_errors(self):
        self.assertRaises(TypeError, max_int, ["titi", 2])
        self.assertRaises(TypeError, max_int, [3, [1, 3]])


if __name__ == '__main__':
    unittest.main()
