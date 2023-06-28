import unittest
from models.base import Base

class BaseTestInit(unittest.TestCase):
	def setUp(self):
		self.base = Base()

	def test_init(self):
		self.assertEqual(self.base.id, 3)
	
	def test_id_1(self):
		self.base = Base(12)
		self.assertEqual(self.base.id, 12)

	def test_id_2(self):
		self.assertEqual(self.base.id, 2)
	
class BaseTestStaticMethod(unittest.TestCase):
	def setUp(self):
		self.base = Base()


	def test_to_json_string(self):
		self.assertEqual(self.base.to_json_string([]), '[]')

	def test_to_json_string1(self):
		# self.assertEqual(self.base.to_json_string(['name, 0']), '[name, 0]')
		pass
	def test_from_json_string(self):
		self.assertEqual(self.base.from_json_string('[]'), [])