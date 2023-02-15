#!/usr/bin/python3
"""Base test"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        
    def test_2(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
        
    def test_3(self):
        b1 = Base(100000)
        self.assertEqual(b1.id, 100000)

    def test_4(self):
        b1 = Base(1.1)
        self.assertEqual(b1.id, 1.1)
        
    def test_5(self):
        b1 = Base.to_json_string([])

    def test_6(self):
        b1 = Base.save_to_file([])

    def test_7(self):
        b1 = Base.save_to_file(None)



if __name__ == '__main__':
    unittest.main()