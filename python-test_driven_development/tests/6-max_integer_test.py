#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_is_empty(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_is_negative(self):
        self.assertAlmostEqual(max_integer([-17, -7, -8, -2]), -2)

    def test_with_one(self):
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_with_begin(self):
        self.assertAlmostEqual(max_integer([3, 2, 1]), 3)

    def test_with_middle(self):
        self.assertAlmostEqual(max_integer([2, 3, 1]), 3)


if __name__ == '__main__':
    unittest.main()