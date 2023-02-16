#!/usr/bin/python3
"""Rectanglecl test"""


import unittest
from models.square import Square


class TestBase(unittest.TestCase):
	def test_0(self):
		Square(1)

	def test_1(self):
		Square(1, 2)

	def test_2(self):
		Square(1, 2, 3)

	def test_3(self):
		with self.assertRaises(TypeError) as context:
			Square("1")
		self.assertTrue('width must be an integer' in str(context.exception))

	def test_4(self):
		with self.assertRaises(TypeError) as context:
			Square(1, "2")
		self.assertTrue('x must be an integer' in str(context.exception))

	def test_5(self):
		with self.assertRaises(TypeError) as context:
			Square(1, 2, "3")
		self.assertTrue('y must be an integer' in str(context.exception))

	def test_6(self):
		Square(1, 2, 3, 4)

	def test_7(self):
		with self.assertRaises(ValueError) as context:
			Square(-1)
		self.assertTrue('width must be > 0' in str(context.exception))

	def test_8(self):
		with self.assertRaises(ValueError) as context:
			Square(1, -2)
		self.assertTrue('x must be >= 0' in str(context.exception))

	def test_9(self):
		with self.assertRaises(ValueError) as context:
			Square(1, 2, -3)
		self.assertTrue('y must be >= 0' in str(context.exception))

	def test_10(self):
		with self.assertRaises(ValueError) as context:
			Square(0)
		self.assertTrue('width must be > 0' in str(context.exception))

	def test_22(self):
		Square.create(**{ 'id': 89 })

	def test_24(self):
		Square.create(**{ 'id': 89, 'size': 1 })

	def test_26(self):
		Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })

	def test_28(self):
		Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })

	def test_30(self):
		Square.save_to_file(None)

	def test_32(self):
		Square.save_to_file([])
  
	def test_34(self):
		Square.save_to_file([Square(1)])

	def test_36(self):
		Square.load_from_file()

	def test_37(self):
		Square.load_from_file()

	def test_40(self):
		Square(5)

	def test_42(self):
		Square(5, 7)

	def test_44(self):
		Square(5, 7, 2)
  
	def test_46(self):
		Square(5, 7, 2, 89)

	def test_54(self):
		Square.save_to_file(None)

	def test_56(self):
		Square.save_to_file([])

	def test_58(self):
		Square.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])
  
	def test_60(self):
		Square.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])

	def test_61(self):
		Square.create(**{ 'size': 2 })

	def test_62(self):
		Square.create(**{ 'size': 2, 'x': 1 })

	def test_63(self):
		Square.create(**{ 'size': 2, 'x': 1, 'y': 3 })

	def test_64(self):
		Square.create(**{ 'size': 2, 'x': 1, 'y': 3, 'id': 89 })

	def test_65(self):
		Square.load_from_file()

	def test_67(self):
		Square.load_from_file()

	def test_69(self):
		Square.load_from_file()