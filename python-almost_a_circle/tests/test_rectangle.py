#!/usr/bin/python3
"""Rectanglecl test"""


import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_1(self):
        Rectangle(1, 2)

    def test_2(self):
        Rectangle(1, 2, 3)

    def test_3(self):
        Rectangle(1, 2, 3, 4)

    def test_4(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("1", 2)
        self.assertTrue('width must be an integer' in str(context.exception))

    def test_5(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, "2")
        self.assertTrue('height must be an integer' in str(context.exception))

    def test_6(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 2, "3")
        self.assertTrue('x must be an integer' in str(context.exception))

    def test_7(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, 2, 3, "4")
        self.assertTrue('y must be an integer' in str(context.exception))

    def test_8(self):
        Rectangle(1, 2, 3, 4, 5)

    def test_9(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(-1, 2)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_10(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, -2)
        self.assertTrue('height must be > 0' in str(context.exception))

    def test_11(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 2)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_12(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 0)
        self.assertTrue('height must be > 0' in str(context.exception))

    def test_13(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 2, -3)
        self.assertTrue('x must be >= 0' in str(context.exception))

    def test_14(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 2, 3, -4)
        self.assertTrue('y must be >= 0' in str(context.exception))

    def test_15(self):
        Rectangle.create(**{ 'width': 2, 'height': 3 })

    def test_16(self):
        Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12 })

    def test_17(self):
        Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12, 'y': 1 })

    def test_18(self):
        Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89 })

    def test_19(self):
        Rectangle.load_from_file()

    def test_20(self):
        Rectangle.load_from_file()
    
    def test_21(self):
        r1 = Rectangle(8, 65, 2, 10, 2)
        r2 = Rectangle(10, 2, 1, 3, 5)
        Rectangle.save_to_file([r1, r2])

    def test_22(self):
        Rectangle.save_to_file([])

    def test_23(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        dt.save_to_file(None)

    def test_24(self):
        with self.assertRaises(AttributeError) as context:
            Rectangle.to_dictionary(self)
        self.assertTrue("'TestBase' object has no attribute 'width'" in str(context.exception))

    def test_25(self):
        dt = Rectangle(10, 10)
        dt.area()
        
    def test_26(self):
        dt = Rectangle(1, 1)
        dt.display()

    def test_27(self):
        Rectangle.save_to_file(None)
        
    def test_28(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(dt.area(), 2)
    
    def test_29(self):
        dt = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(dt), '[Rectangle] (5) 3/4 - 1/2')

    def test_30(self):
        dt = Rectangle(1, 2, 3, 4)
        dt.display()
        
    def test_31(self):
        dt = Rectangle(1, 2, 3)
        dt.display()
        
    def test_32(self):
        dt = Rectangle(1, 2)
        dt.display()


        