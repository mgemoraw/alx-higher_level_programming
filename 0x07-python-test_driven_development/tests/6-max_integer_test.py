#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestCases(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(max_integer([3, 5, 5, 7]), 7)

    def test_max(self):
        self.assertEqual(max_integer([0, 5, 2, 5]), 5)

    def test_type_error(self):
        self.assertEqual(max_integer([-2, -3, -1]), -1)
