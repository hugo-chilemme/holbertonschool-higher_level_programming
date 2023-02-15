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
        Base.to_json_string([])

    def test_6(self):
        Base.save_to_file([])

    def test_7(self):
        Base.save_to_file(None)

    def test_8(self):
        Base.to_json_string([])

    def test_9(self):
        Base.to_json_string([ { 'id': 12 }])

    def test_10(self):
        Base.from_json_string(None)

    def test_11(self):
        Base.from_json_string("[]")

    def test_12(self):
        Base.from_json_string("[]")

    def test_13(self):
        Base.from_json_string('[{ "id": 89 }]')

    def test_14(self):
        Base.from_json_string('[{ "id": 89 }]')

if __name__ == '__main__':
    unittest.main()