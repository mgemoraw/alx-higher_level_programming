#!/usr/bin/python3
"""
testing base module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
	"""
	testing cases for Base class
	"""
	def test_create_id(self):
		""" tests if id is created for ever initials
		"""
		base1 = Base()
		base2 = Base()
		base3 = Base()
		base4 = Base(15)
		base5 = Base(-3)
		base6 = Base(2.5)
		base7 = Base(None)
		base8 = Base("string")
		base9 = Base()

		self.assertEqual(base1.id, 1)
		self.assertEqual(base2.id, 2)
		self.assertEqual(base3.id, 3)
		self.assertEqual(base4.id, 15)
		self.assertEqual(base5.id, -3)
		self.assertEqual(base6.id, 2.5)
		self.assertEqual(base7.id, 4)
		self.assertEqual(base8.id, 'string')
		self.assertEqual(base9.id, 5)



	def test_to_json_string(self):
		self.assertEqual(Base.to_json_string([]), '[]')

	def test_to_json_string1(self):
		self.assertEqual(Base.to_json_string(None), '[]')
	
	def test_from_json_string(self):
		self.assertEqual(Base.from_json_string('[]'), [])

if __name__ == "__main__":
	unittest.main()